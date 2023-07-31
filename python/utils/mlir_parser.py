#!/usr/bin/env python3
# ==============================================================================
#
# Copyright (C) 2022 Sophgo Technologies Inc.  All rights reserved.
#
# TPU-MLIR is licensed under the 2-Clause BSD License except for the
# third-party components.
#
# ==============================================================================

import sys
import mlir
import re
import tqdm
# from mlir.ir import *
from mlir.dialects import quant, linalg

class Operation:
    cache_map = {}
    def __init__(self, op, body, idx):
        self.type = Operation.type(op)
        self.loc = Operation.loc(op)
        self.name = Operation.name(op)
        self.shape = Operation.shape(op)
        self.opds = Operation.operands(op, body, idx)

        self.attrs = Operation.attrs(op)
        # self.attrs = Operation.append_attr(op, self.attrs)
        self.outputs = Operation.outputs(op)
        self.op = op
        # print("op:",op, ", str:", self.__str__())
    def __str__(self):
        return self.name + "," + self.type + "," + self.loc + "," + str(self.shape) + "," + str(
            self.opds)

    @staticmethod
    def name(op):
        if(op.attributes["idx"]!=None):
            pattern = r'["\']([^"\']*?)["\']'
            matches = re.findall(pattern, str(mlir.ir.StringAttr(op.attributes["idx"])))
            # return str(mlir.ir.StringAttr(op.attributes["idx"]))
            return matches[0]
        else:
            return op.get_asm().split('=')[0].strip()


    @staticmethod
    def outputs(op):
        loc = op.location
        if loc == "loc(unknown)":
            return None
        loc = str(loc)
        if 'loc(fused[' in loc:
            loc = eval(loc[9:-1])
        else:
            loc = [re.search(r'\"(\S+?)\"', loc).group(1)]
        return loc

    @staticmethod
    def type(op):
        return op.operation.name

    @staticmethod
    def str(value):
        return mlir.ir.StringAttr(value).value

    @staticmethod
    def bool(value):
        return mlir.ir.BoolAttr(value).value

    @staticmethod
    def int(value):
        return mlir.ir.IntegerAttr(value).value

    @staticmethod
    def int_array(value):
        return [mlir.ir.IntegerAttr(x).value for x in mlir.ir.ArrayAttr(value)]

    @staticmethod
    def fp_array(value):
        return [mlir.ir.FloatAttr(x).value for x in mlir.ir.ArrayAttr(value)]

    @staticmethod
    def attrs(op):
        arr_map = {}
        for i in range(len(op.attributes)):
            attr = op.attributes[i]
            k, v = str(attr.name), str(attr.attr)
            arr_map[k] = v
        return arr_map

    @staticmethod
    def append_attr(op, attrs):
        if len(op.results) != 1:
            return attrs
        shape_type = mlir.ir.ShapedType(op.results[0].type)
        element_type = shape_type.element_type
        if quant.UniformQuantizedType.isinstance(element_type):
            quant_type = quant.UniformQuantizedType(element_type)
            attrs["quant_scale"] = str(quant_type.scale)
            attrs["quant_zero_point"] = str(quant_type.zero_point)
        if quant.CalibratedQuantizedType.isinstance(element_type):
            quant_type = quant.CalibratedQuantizedType(element_type)
            attrs["calibrate_min"] = str(quant_type.min)
            attrs["calibrate_max"] = str(quant_type.max)
        return attrs

    @staticmethod
    def dictattr(op, field_name):
        return mlir.ir.DictAttr(op.attributes[field_name])

    @staticmethod
    def loc(op):
        return op.get_asm().split('=')[0].strip()

    @staticmethod
    def shape(op):
        shape = []
        single_data_type = ["f32", "f64", "i32", "i64", "i16", "index"]
        # print("in func shape, op :", op)
        for result in op.results:
            # print("result.type :", str(result.type))           
            if str(result.type) != 'none' \
                and str(result.type) not in single_data_type :
                shape_type = mlir.ir.ShapedType(result.type)
                shape = [shape_type.get_dim_size(i) for i in range(shape_type.rank)]
                # print("op shape:", shape_type)
                break
        return shape

    @staticmethod
    def operands(op, body, idx):
        opds = []
        # print("opname:", op.get_asm().split('=')[0].strip())
        for opd in op.operands:
            for j in reversed(range(idx)):
                prev_op = body.operations[j]
                if prev_op.results[0] == opd:
                    # print("success!")
                    if Operation.type(prev_op) not in [
                            # @xcgao: is here right?
                            # "tpu.None",
                            # "top.None",
                            # "tpu.load_weight",
                            # "tpu.weight_file",
                            "arith.constant",
                            # "tensor.pad",
                            # "tensor.empty"
                    ]:
                        opds.append(Operation.name(prev_op))
        # print(opds)
        return opds

    @staticmethod
    def operands_v2(op, body, idx):
        opds = []

        for opd in op.operands:
            if opd in Operation.cache_map:
                for i,prev_op_name in Operation.cache_map[opd]:
                    if i < idx:
                        opds.append(prev_op_name)

        return opds

    # @staticmethod
    # def dump_info(self):
    #     print("[Info] op:", self.op)
    #     self.name = Operation.name(op)
    #     self.type = Operation.type(op)
    #     self.loc = Operation.loc(op)
    #     # self.shape = Operation.shape(op)
    #     self.opds = Operation.operands_v2(op, body, idx)

    #     self.attrs = Operation.attrs(op)
    #     # self.attrs = Operation.append_attr(op, self.attrs)
    #     self.outputs = Operation.outputs(op)
    #     print("     ")

    #     return opds


class MlirParser:

    def __init__(self, mlir_file):
        with open(mlir_file, 'r') as f:
            context = f.read()

        self.ctx = mlir.ir.Context()
        self.ctx.allow_unregistered_dialects = True
        self.module = mlir.ir.Module.parse(context, self.ctx)
        # print("ctx:", self.ctx)
        
        if(len(self.module.body.operations)==1):
            self.main_func = self.module.body.operations[0]
            self.body = self.main_func.regions[0].blocks[0]            
        elif(len(self.module.body.operations)==2):
            ## Module has a mutable @global_seed op
            self.main_func = self.module.body.operations[1]
            self.body = self.main_func.regions[0].blocks[0]
        else :
            assert(0 and "[Error] Module has more than 2 operations!")
        # print("body:")
        # print(self.body)
        # print("body:",self.body)
        # self.attrs = Operation.attrs(self.module.operation)
        #self.module_name = eval(self.attrs['module.name'])
        #self.module_state = eval(self.attrs['module.state'])
        # self.module_weight_file = eval(self.attrs['module.weight_file'])
        # self.module_chip = eval(self.attrs['module.chip'])
        self.ops = []
        self.computing_ops = []
        self.const_ops = []
        self.return_op = None

        cache_map = {}
        # print()
        for i in tqdm.trange(len(self.body.operations)):
            tmpop = self.body.operations[i]
            # print(".", end='')
            if len(tmpop.results) > 0:
                cache_map.setdefault(tmpop.results[0],[]).append([i, Operation.name(tmpop)])

        # print("----")
        Operation.cache_map = cache_map
        # print("cache_map:", cache_map)

        print(" Build self-defined class for every operation:")
        for i in tqdm.trange(len(self.body.operations)-1): # skip the last return op
            # print("op:", self.body.operations[i])
            op = self.body.operations[i]
            operation = Operation(op, self.body, i)
            self.ops.append(operation)
            optype = Operation.type(op)
            if optype in ["func.return"]:
                continue
            elif optype in ["arith.constant", "tosa.const"]:
                self.const_ops.append(operation)
            else:
                self.computing_ops.append(operation)
            # print("operation:", optype)

        self.inputs = list(self.main_func.arguments)
        self.input_username_dic = {}
        self.get_input_username_dic()
        # print("func: ",self.main_func.arguments[0])
        # print("input: ", self.inputs[0].type)
        # for op in self.ops:
        #     print(op.type)
        #     if op.type == 'top.Input':
        #         self.inputs.append(op)

    def get_op_name_list(self):
        return [op.name for op in self.ops]

    def get_computing_op_name_list(self):
        return [op.name for op in self.computing_ops]

    def get_const_op_name_list(self):
        return [op.name for op in self.const_ops]

    def get_input_num(self):
        return len(self.inputs)

    def get_input_op_by_idx(self, idx):
        # return self.inputs[idx].op
        return self.inputs[idx]

    def get_input_shape_by_idx(self, idx):
        # return Operation.shape(self.inputs[0].op)[0]
        return mlir._mlir_libs._mlir.ir.ShapedType(self.inputs[idx].type)

    def get_batch_size(self):
        # return Operation.shape(self.inputs[0].op)[0]
        shape_args = mlir._mlir_libs._mlir.ir.ShapedType(self.inputs[0].type)
        return shape_args.shape[0]

    def get_pre_op_by_op_name(self, op_name):
        op_input_tensor = []
        # this_op = self.get_op_by_op_name(op_name)
        for input_arg in self.inputs:
            print("this_op:",op_name)
            print("input_arg:",self.input_username_dic[input_arg])
            if op_name in self.input_username_dic[input_arg]:
                op_input_tensor.append(input_arg)

        for op in self.ops:
            if op.name == op_name:
                # print("op.opds", op.opds)
                for opd in op.opds:
                    # if opd in self.get_op_name_list():
                    op_input_tensor.append(opd)
        return op_input_tensor

    def get_next_op_by_op_name(self, op_name):
        op_output_tensor = []
        for op in self.ops:
            if op_name in op.opds:
                if op.name in self.get_op_name_list():
                    op_output_tensor.append(op.name)
        return op_output_tensor

    ## LJH DEFINE
    @staticmethod
    def get_users_type_by_op_name(op_name, all_ops_list, all_op_name_list):
        op_output_tensor = []
        for operation in all_ops_list:
            if operation.type == "linalg.generic":
                # print("linalg GenericOp!")
                generic_block = operation.op.regions[0].blocks[0]
                for op_in_block in generic_block:
                    # print("op_in_block:",op_in_block)  
                    for operand_value in op_in_block.operands:
                        operand = operand_value.owner
                        # print("  operand:",operand)
                        if not isinstance(operand, mlir.ir.Block) \
                            and Operation.name(operand) == op_name :
                            op_output_tensor.append(operation.type)

                            # print(" found a generic:  not block operand:",operand, ", type:", type(operand))
                        # if(operand)
                # for(op)
            if op_name in operation.opds:
                if operation.name in all_op_name_list:
                    op_output_tensor.append(operation.type)
        return op_output_tensor

    def get_input_username_dic(self):
        for input_arg in self.inputs:
            self.input_username_dic[input_arg]=[]
            for op in self.body.operations:
                # print("input_arg:", input_arg)
                # print("op:", op)
                # print("operands:", op.operands)                
                if input_arg in op.operands:
                    self.input_username_dic[input_arg].append(Operation.name(op))
            # print("-------------input_user_dic[input_arg]:", self.input_user_dic[input_arg][0])                 

                    
        

    def get_user_count_by_op_name(self, op_name):

        count = 0
        for op in self.ops:
            if op_name in op.opds:
                count += 1
        return count

    def get_use_count_by_op_name(self, op_name):
        count = 0
        for op in self.ops:
            count += op.opds.count(op_name)
        return count

    def get_outputs_by_op_name(self, op_name):
        for op in self.ops:
            if op.name == op_name:
                return op.outputs
        return None

    def get_op_by_op_name(self, op_name):
        for op in self.ops:
            if op.name == op_name:
                return op
        return None

    def get_opds_by_op_name(self, op_name):
        for op in self.ops:
            if op.name == op_name:
                return op.opds
        return None

    def get_op_type_by_op_name(self, op_name):
        for op in self.ops:
            if op.name == op_name:
                return op.type
        return None

    # the func is to get a dict with output names and corresponding shapes
    def get_output_op_names_n_shapes(self):
        if not self.return_op:
            return []
        outputs = {}
        for op in self.body.operations:
            if op == self.return_op:
                continue
            for opd in self.return_op.operands:
                if opd in op.results:
                    shape_type = mlir.ir.ShapedType(opd.type)
                    shape = [shape_type.get_dim_size(i) for i in range(shape_type.rank)]
                    name = Operation.name(op)
                    outputs[name] = shape
        return outputs

    def get_middle_op_names_n_shape_type(self):
        middles = {}
        for i in range(len(self.body.operations)):
            op = self.body.operations[i]
            type = Operation.type(op)
            if type in ['top.None', 'top.Input', 'func.return']:
                continue
            shape_type = mlir.ir.ShapedType(op.results[0].type)
            name = Operation.name(op)
            middles[name] = shape_type
        return middles

    def get_initializer_op_names_n_shape_type(self):

        initializer = {}
        for i in range(len(self.body.operations)):
            op = self.body.operations[i]
            type = Operation.type(op)
            if type != 'top.Weight':
                continue
            shape_type = mlir.ir.ShapedType(op.results[0].type)
            name = Operation.name(op)
            initializer[name] = shape_type
        return initializer



if __name__ == '__main__':
    parser = MlirParser(sys.argv[1])
    print(parser.module)
