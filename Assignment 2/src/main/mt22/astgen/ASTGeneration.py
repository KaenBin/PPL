from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from main.mt22.utils.AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):
    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(reduce(lambda prev, curr: prev + self.visit(curr), ctx.vardecl(), []))


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self,ctx:MT22Parser.VardeclContext):
        mptype = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return list(map(lambda x: VarDecl(x, mptype), ids))


    # Visit a parse tree produced by MT22Parser#vardecl1.
    def visitVardecl1(self, ctx:MT22Parser.Vardecl1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list1.
    def visitId_list1(self, ctx:MT22Parser.Id_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list2.
    def visitId_list2(self, ctx:MT22Parser.Id_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl2.
    def visitVardecl2(self, ctx:MT22Parser.Vardecl2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl2_2.
    def visitVardecl2_2(self, ctx:MT22Parser.Vardecl2_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl3.
    def visitVardecl3(self, ctx:MT22Parser.Vardecl3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl3_2.
    def visitVardecl3_2(self, ctx:MT22Parser.Vardecl3_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paradecl.
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_list1.
    def visitPara_list1(self, ctx:MT22Parser.Para_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_list2.
    def visitPara_list2(self, ctx:MT22Parser.Para_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para.
    def visitPara(self, ctx:MT22Parser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmts_list.
    def visitStmts_list(self, ctx:MT22Parser.Stmts_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmts.
    def visitStmts(self, ctx:MT22Parser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt2.
    def visitAssign_stmt2(self, ctx:MT22Parser.Assign_stmt2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:MT22Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt2.
    def visitFor_stmt2(self, ctx:MT22Parser.For_stmt2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_stmt.
    def visitDo_stmt(self, ctx:MT22Parser.Do_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bool_expr.
    def visitBool_expr(self, ctx:MT22Parser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt_no_semi.
    def visitCall_stmt_no_semi(self, ctx:MT22Parser.Call_stmt_no_semiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_body.
    def visitCall_body(self, ctx:MT22Parser.Call_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_list1.
    def visitCall_list1(self, ctx:MT22Parser.Call_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_list2.
    def visitCall_list2(self, ctx:MT22Parser.Call_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_body.
    def visitBlock_body(self, ctx:MT22Parser.Block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_airth.
    def visitExp_airth(self, ctx:MT22Parser.Exp_airthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_bool.
    def visitExp_bool(self, ctx:MT22Parser.Exp_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_str.
    def visitExp_str(self, ctx:MT22Parser.Exp_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_rela.
    def visitExp_rela(self, ctx:MT22Parser.Exp_relaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_ind.
    def visitExp_ind(self, ctx:MT22Parser.Exp_indContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_list1.
    def visitInt_list1(self, ctx:MT22Parser.Int_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_list2.
    def visitInt_list2(self, ctx:MT22Parser.Int_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literals.
    def visitLiterals(self, ctx:MT22Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_lit.
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_list1.
    def visitExpression_list1(self, ctx:MT22Parser.Expression_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_list2.
    def visitExpression_list2(self, ctx:MT22Parser.Expression_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr72.
    def visitArr72(self, ctx:MT22Parser.Arr72Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functions.
    def visitFunctions(self, ctx:MT22Parser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readint_func.
    def visitReadint_func(self, ctx:MT22Parser.Readint_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readfloat_func.
    def visitReadfloat_func(self, ctx:MT22Parser.Readfloat_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readbool_func.
    def visitReadbool_func(self, ctx:MT22Parser.Readbool_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readstr_func.
    def visitReadstr_func(self, ctx:MT22Parser.Readstr_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printint_func.
    def visitPrintint_func(self, ctx:MT22Parser.Printint_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printfloat_func.
    def visitPrintfloat_func(self, ctx:MT22Parser.Printfloat_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printbool_func.
    def visitPrintbool_func(self, ctx:MT22Parser.Printbool_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printstr_func.
    def visitPrintstr_func(self, ctx:MT22Parser.Printstr_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#supers.
    def visitSupers(self, ctx:MT22Parser.SupersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventdef.
    def visitPreventdef(self, ctx:MT22Parser.PreventdefContext):
        return self.visitChildren(ctx)