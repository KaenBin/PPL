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
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        else:
            return StringType()


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self,ctx:MT22Parser.VardeclContext):
        if ctx.vardecl1():
            return self.visit(ctx.vardecl1())
        elif ctx.vardecl2():
            return self.visit(ctx.vardecl2())
        else:
            return self.visit(ctx.vardecl3())


    # Visit a parse tree produced by MT22Parser#vardecl_type.
    def visitVardecl_type(self, ctx:MT22Parser.Vardecl_typeContext):
        if ctx.var_type():
            return self.visit(ctx.var_type())
        elif ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.array_type())
            

    # Visit a parse tree produced by MT22Parser#vardecl1.
    def visitVardecl1(self, ctx:MT22Parser.Vardecl1Context):
        return list(map(lambda x: VarDecl(x, self.visit(ctx.vardecl_type())), self.visit(ctx.id_list())))


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return list(map(lambda x: x.getText(), ctx.ID()))


    # Visit a parse tree produced by MT22Parser#vardecl2.
    def visitVardecl2(self, ctx:MT22Parser.Vardecl2Context):
        return list(map(lambda x, y: VarDecl(ctx.ID().getText(), x, self.visit(ctx.exp())), self.visit(ctx.Vardecl2_2())))


    # Visit a parse tree produced by MT22Parser#vardecl2_2.
    def visitVardecl2_2(self, ctx:MT22Parser.Vardecl2_2Context):
        if ctx.COLON():
            return list(map(lambda x: x, self.visit(ctx.vardecl_type())))
        return self.visit(ctx.Vardecl2_2())


    # Visit a parse tree produced by MT22Parser#vardecl3.
    def visitVardecl3(self, ctx:MT22Parser.Vardecl3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl3_2.
    def visitVardecl3_2(self, ctx:MT22Parser.Vardecl3_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        if ctx.VOID():
            func_type = VoidType()
        elif ctx.AUTO():
            func_type = AutoType()
        else:
            func_type = self.visit(ctx.var_type())
        if ctx.INHIRIT():
            if ctx.ID():
                inhirit = ctx.ID().getText()
            else:
                inhirit = self.visit(ctx.functions())
        else:
            inhirit = None
        return list(map(lambda x: FuncDecl(ctx.ID().getText(), func_type, x, inhirit, self.visit(ctx.block_stmt())), self.visit(ctx.paradecl())))


    # Visit a parse tree produced by MT22Parser#paradecl.
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_list.
    def visitPara_list(self, ctx:MT22Parser.Para_listContext):
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
        if ctx.CONCAT():
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinExpr(ctx.CONCAT().getText(), left, right)
        return self.visit(ctx.exp1())


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        if ctx.EQUALOP():
            return BinExpr(ctx.CONCAT().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.DIFOP():
            return BinExpr(ctx.DIFOP().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.LESSOP():
            return BinExpr(ctx.LESSOP().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.GREATOP():
            return BinExpr(ctx.GREATOP().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.LESSEQOP():
            return BinExpr(ctx.LESSEQOP().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.GREATEQOP():
            return BinExpr(ctx.GREATEQOP().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2())


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        if ctx.CONJOP():
            return BinExpr(ctx.CONJOP().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        elif ctx.DISJOP():
            return BinExpr(ctx.DISJOP().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        else: 
            return self.visit(ctx.exp3())


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        if ctx.ADDOP():
            return BinExpr(ctx.ADDOP().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.MINUSOP():
            return BinExpr(ctx.MINUSOP().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        else: 
            return self.visit(ctx.exp4())


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        if ctx.MULOP():
            return BinExpr(ctx.MULOP().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.DIVOP():
            return BinExpr(ctx.DIVOP().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.MODOP():
            return BinExpr(ctx.MODOP().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        else: 
            return self.visit(ctx.exp5())


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        if ctx.NEGAOP():
            return UnExpr(ctx.NEGAOP().getText(), self.visit(ctx.exp5()))
        return self.visit(ctx.exp6())

    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        if ctx.MINUSOP():
            return UnExpr(ctx.MINUSOP().getText(), self.visit(ctx.exp6()))
        return self.visit(ctx.exp7())


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        # if ctx.LSB():
        #     if ctx.expresion_list():
        #         return self.visit(ctx.expression_list())
        #     else:
        #         return self.visit(ctx.exp_ind())
        return self.visit(ctx.operands())


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        if ctx.atom_type():
            return self.visit(ctx.atom_type())
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.LRB():
            return self.visit(ctx.exp())
        else:
            return self.visit(ctx.call_stmt_no_semi())

    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        if ctx.AUTO():
            return ArrayType(self.visit(ctx.int_list), AutoType())
        else:
            return ArrayType(self.visit(ctx.int_list), self.visit(ctx.atom_type()))


    # Visit a parse tree produced by MT22Parser#int_list.
    def visitInt_list(self, ctx:MT22Parser.Int_listContext):
        if ctx.INTLIT():
            return [int(x) for x in self.visit(ctx.INTLIT())]
        return []


    # Visit a parse tree produced by MT22Parser#atom_type.
    def visitAtom_type(self, ctx:MT22Parser.Atom_typeContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOL():
            return BooleanLit(ctx.BOOL().getText () == 'true')
        else:
            return StringLit(ctx.STRINGLIT().getText())
        

    # Visit a parse tree produced by MT22Parser#array_lit.
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return ArrayLit(self.visit(ctx.expression_list()))


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        if ctx.exp():
            return [x for x in self.visit(ctx.exp())]
        return []


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