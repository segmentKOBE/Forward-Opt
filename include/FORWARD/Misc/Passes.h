//===- Passes.h - FDRA-opt pass entry points --------------------*- C++ -*-===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//
//
// This header file defines prototypes that expose pass constructors.
//
//===----------------------------------------------------------------------===//

#ifndef FORWARD_MISC_PASSES_H
#define FORWARD_MISC_PASSES_H

#include "mlir/Dialect/Func/IR/FuncOps.h"
#include "mlir/Pass/Pass.h"
#include "mlir/Pass/PassRegistry.h"
#include <memory>




namespace mlir {
class Pass;
} // namespace mlir


namespace mlir {
namespace FORWARD {

//===----------------------------------------------------------------------===//
// Misc
//===----------------------------------------------------------------------===//
std::unique_ptr<mlir::Pass> createTestPrintOpNestingPass();
#define GEN_PASS_REGISTRATION
#define GEN_PASS_DEF_TESTPRINTOPNESTING
#define GEN_PASS_DECL
#include "FORWARD/Misc/FORWARDMiscPasses.h.inc"
//===----------------------------------------------------------------------===//
// Lowerings
//===----------------------------------------------------------------------===//

// TODO: Move this pass out of the Misc directory into the Conversion directory
/// Perform lowering from std operations to LLVM dialect.
/// Exposing the options of barePtrCallConv or emitCWrappers without the need
/// to know the mlir context during pass (pipeline) creation. MLIR context is
/// obtained at runtime.
///
/// This pass is based on:
///    llvm-project/mlir/lib/Conversion/FuncToLLVM/FuncToLLVM.cpp

//===----------------------------------------------------------------------===//
// Register passes
//===----------------------------------------------------------------------===//

/// Include the auto-generated definitions for passes
// TODO: only the registration call is necessary. Move pass class decls to
// another file


} // namespace FORWARD
} // namespace mlir


#endif // FORWARD_MISC_PASSES_H
