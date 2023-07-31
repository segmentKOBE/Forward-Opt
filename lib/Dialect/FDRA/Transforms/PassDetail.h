//===- PassDetail.h --------------------- --------------------*- C++ -*-===//
//===----------------------------------------------------------------------===//

#ifndef DIALECT_FDRA_TRANSFORMS_PASSDETAIL_Test_H_
#define DIALECT_FDRA_TRANSFORMS_PASSDETAIL_Test_H_

#include "mlir/IR/BuiltinOps.h"
#include "mlir/Pass/Pass.h"
#include "mlir/Dialect/SCF/IR/SCF.h"

namespace mlir {

namespace arith {
class ArithmeticDialect;
class AffineDialect;
} // namespace Tensor
// #include "soda/Dialect/MyTest/IR/MyTest.h"
#define GEN_PASS_CLASSES
#include "RAAA/Dialect/FDRA/Transforms/Passes.h.inc"

} // end namespace mlir

#endif // DIALECT_FDRA_TRANSFORMS_PASSDETAIL_Test_H_
