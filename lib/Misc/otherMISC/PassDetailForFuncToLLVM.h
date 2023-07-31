//===- PassDetailForStdToLLVM.h - Conversion Pass class details --- C++ -*-===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//
//
// This is required by the StandardToLLVM pass.
//
//===----------------------------------------------------------------------===//

#ifndef MISC_CONVERSION_PASSDETAIL_H_
#define MISC_CONVERSION_PASSDETAIL_H_

#include "mlir/Pass/Pass.h"

#include "mlir/Conversion/GPUToROCDL/Runtimes.h"
#include "mlir/IR/BuiltinOps.h"
#include "mlir/IR/FunctionInterfaces.h"

namespace mlir {
class AffineDialect;

// Forward declaration from Dialect.h
template <typename ConcreteDialect>
void registerDialect(DialectRegistry &registry);

namespace acc {
class OpenACCDialect;
} // namespace acc

namespace arith {
class ArithmeticDialect;
} // namespace arith

namespace cf {
class ControlFlowDialect;
} // namespace cf

namespace complex {
class ComplexDialect;
} // namespace complex

namespace gpu {
class GPUDialect;
class GPUModuleOp;
} // namespace gpu

namespace func {
class FuncDialect;
} // namespace func

namespace linalg {
class LinalgDialect;
} // namespace linalg

namespace LLVM {
class LLVMDialect;
} // namespace LLVM

namespace nvgpu {
class NVGPUDialect;
}

namespace NVVM {
class NVVMDialect;
} // namespace NVVM

namespace math {
class MathDialect;
} // namespace math

namespace memref {
class MemRefDialect;
} // namespace memref

namespace omp {
class OpenMPDialect;
} // namespace omp

namespace pdl_interp {
class PDLInterpDialect;
} // namespace pdl_interp

namespace ROCDL {
class ROCDLDialect;
} // namespace ROCDL

namespace scf {
class SCFDialect;
} // namespace scf

namespace spirv {
class SPIRVDialect;
} // namespace spirv

namespace tensor {
class TensorDialect;
} // namespace tensor

namespace tosa {
class TosaDialect;
} // namespace tosa

namespace vector {
class VectorDialect;
} // namespace vector

namespace arm_neon {
class ArmNeonDialect;
} // namespace arm_neon

#define GEN_PASS_CLASSES
#include "mlir/Conversion/Passes.h.inc"

} // namespace mlir

#endif // MISC_CONVERSION_PASSDETAIL_H_
