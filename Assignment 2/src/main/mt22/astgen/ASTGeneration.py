from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(reduce(lambda prev, curr: prev + self.visit(ctx.getChild(curr)), range(ctx.getChildCount() - 1), []))


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
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#vardecl_type.
    def visitVardecl_type(self, ctx:MT22Parser.Vardecl_typeContext):
        if ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.getChild(0))
            

    # Visit a parse tree produced by MT22Parser#vardecl1.
    def visitVardecl1(self, ctx:MT22Parser.Vardecl1Context):
        return list(map(lambda x: VarDecl(x, self.visit(ctx.vardecl_type())), self.visit(ctx.id_list())))


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return list(map(lambda x: x.getText(), ctx.ID()))


    # Visit a parse tree produced by MT22Parser#vardecl2.
    def visitVardecl2(self, ctx:MT22Parser.Vardecl2Context):
        def get_ID(ctx):
            if ctx.vardecl_type():
                return [ctx.ID().getText()]
            else:
                return [ctx.ID().getText()] + get_ID(ctx.vardecl2())
        def get_exp(ctx):
            if ctx.vardecl_type():
                return [self.visit(ctx.exp())]
            else:
                return [self.visit(ctx.exp())] + get_exp(ctx.vardecl2())
        def get_var_type(ctx):
            if ctx.vardecl_type():
                return self.visit(ctx.vardecl_type())
            else:
                return get_var_type(ctx.vardecl2())
        return list(map(lambda x, y: VarDecl(x, get_var_type(ctx), y), get_ID(ctx), get_exp(ctx)[::-1]))


    # Visit a parse tree produced by MT22Parser#vardecl3.
    def visitVardecl3(self, ctx:MT22Parser.Vardecl3Context):
        def get_ID(ctx):
            if ctx.COLON():
                return [ctx.ID().getText()]
            else:
                return [ctx.ID().getText()] + get_ID(ctx.vardecl3())
        def get_array(ctx):
            if ctx.COLON():
                return [self.visit(ctx.array_type())]
            else:
                return [self.visit(ctx.array_type())] + get_array(ctx.vardecl3())
        return list(map(lambda x, y: VarDecl(x, y), get_ID(ctx), get_array(ctx)[::-1]))


    # Visit a parse tree produced by MT22Parser#func_ids.
    def visitFunc_ids(self, ctx:MT22Parser.Func_idsContext):
        return ctx.getChild(0)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        if ctx.VOID():
            func_type = VoidType()
        elif ctx.AUTO():
            func_type = AutoType()
        else:
            func_type = self.visit(ctx.var_type())
        if ctx.INHERIT():
            inherit = self.visit(ctx.func_ids())
        else:
            inherit = None
        return [FuncDecl(ctx.ID().getText(), func_type, self.visit(ctx.paradecl()), inherit, self.visit(ctx.block_stmt()))]


    # Visit a parse tree produced by MT22Parser#paradecl.
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        return self.visit(ctx.para_list())


    # Visit a parse tree produced by MT22Parser#para_list.
    def visitPara_list(self, ctx:MT22Parser.Para_listContext):
        return [self.visit(x) for x in ctx.para()]


    # Visit a parse tree produced by MT22Parser#para.
    def visitPara(self, ctx:MT22Parser.ParaContext):
        if ctx.VOID():
            para_type = VoidType()
        elif ctx.AUTO():
            para_type = AutoType()
        else:
            para_type = self.visit(ctx.var_type())
        if ctx.OUT():
            out_check = True
        else:
            out_check = False
        if ctx.INHERIT():
            inherit_check = True
        else:
            inherit_check = False
        return ParamDecl(ctx.ID().getText(), para_type, out_check, inherit_check)


    # Visit a parse tree produced by MT22Parser#stmts_list.
    def visitStmts_list(self, ctx:MT22Parser.Stmts_listContext):
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#stmts.
    def visitStmts(self, ctx:MT22Parser.StmtsContext):
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visit(ctx.assign_stmt2())


    # Visit a parse tree produced by MT22Parser#assign_stmt2.
    def visitAssign_stmt2(self, ctx:MT22Parser.Assign_stmt2Context):
        def get_lhs(ctx):
            if ctx.ASSIGN():
                return [self.visit(ctx.assign_lhs())]
            else:
                return [self.visit(ctx.assign_lhs())] + get_lhs(ctx.assign_stmt2())
        def get_exp(ctx):
            if ctx.ASSIGN():
                return [self.visit(ctx.exp())]
            else:
                return [self.visit(ctx.exp())] + get_exp(ctx.assign_stmt2())
        return list(map(lambda x, y: AssignStmt(x, y), get_lhs(ctx), get_exp(ctx)[::-1]))


    # Visit a parse tree produced by MT22Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:MT22Parser.Assign_lhsContext):
        if ctx.ID():
            return ctx.ID().getText()
        else:
            return ctx.exp_ind()


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        if ctx.ELSE():
            else_stmts = self.visit(ctx.stmts(1))
        else:
            else_stmts = None
        return [IfStmt(self.visit(ctx.exp()), self.visit(ctx.stmts(0)), else_stmts)]


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return ForStmt(self.visit(ctx.assign_stmt2()), self.visit(ctx.expression_list(0)), self.visit(ctx.expression_list(1)), self.visit(ctx.stmts_list()))


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return WhileStmt(self.visit(ctx.bool_expr()), self.visit(ctx.stmts_list()))


    # Visit a parse tree produced by MT22Parser#do_stmt.
    def visitDo_stmt(self, ctx:MT22Parser.Do_stmtContext):
        return DoWhileStmt(self.visit(ctx.bool_expr()), self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by MT22Parser#bool_expr.
    def visitBool_expr(self, ctx:MT22Parser.Bool_exprContext):
        # return self.visitChildren(ctx)
        return


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        if ctx.exp():
            expr = self.visit(ctx.exp())
        else:
            expr = None
        return ReturnStmt(expr)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visit(ctx.call_stmt_no_semi())


    # Visit a parse tree produced by MT22Parser#call_stmt_no_semi.
    def visitCall_stmt_no_semi(self, ctx:MT22Parser.Call_stmt_no_semiContext):
        if ctx.ID():
            return CallStmt(ctx.ID().getText(), self.visit(ctx.call_body()))
        return self.visit(ctx.functions())


    # Visit a parse tree produced by MT22Parser#call_body.
    def visitCall_body(self, ctx:MT22Parser.Call_bodyContext):
        return [self.visit(x) for x in ctx.exp()]


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return BlockStmt(self.visit(ctx.block_body()))


    # Visit a parse tree produced by MT22Parser#block_body.
    def visitBlock_body(self, ctx:MT22Parser.Block_bodyContext):
        return [self.visit(ctx.getChild(x)) for x in range(ctx.getChildCount())]


    # Visit a parse tree produced by MT22Parser#exp_airth.
    def visitExp_airth(self, ctx:MT22Parser.Exp_airthContext):
        if ctx.ADDOP():
            return self.visit(ctx.ADDOP())
        elif ctx.MINUSOP():
            return self.visit(ctx.MINUSOP())
        elif ctx.MULOP():
            return self.visit(ctx.MULOP())
        elif ctx.DIVOP():
            return self.visit(ctx.DIVOP())
        else:
            return self.visit(ctx.MODOP())


    # Visit a parse tree produced by MT22Parser#exp_bool.
    def visitExp_bool(self, ctx:MT22Parser.Exp_boolContext):
        if ctx.NEGAOP():
            return self.visit(ctx.NEGAOP())
        elif ctx.CONJOP():
            return self.visit(ctx.CONJOP())
        else:
            return self.visit(ctx.DISJOP())
        

    # Visit a parse tree produced by MT22Parser#exp_str.
    def visitExp_str(self, ctx:MT22Parser.Exp_strContext):
        return self.visit(ctx.CONCAT())


    # Visit a parse tree produced by MT22Parser#exp_rela.
    def visitExp_rela(self, ctx:MT22Parser.Exp_relaContext):
        if ctx.EQUALOP():
            return self.visit(ctx.EQUALOP())
        elif ctx.DIFOP():
            return self.visit(ctx.DIFOP())
        elif ctx.LESSOP():
            return self.visit(ctx.LESSOP())
        elif ctx.LESSEQOP():
            return self.visit(ctx.LESSEQOP())
        elif ctx.GREATOP():
            return self.visit(ctx.GREATOP())
        else:
            return self.visit(ctx.GREATEQOP())
        

    # Visit a parse tree produced by MT22Parser#exp_ind.
    def visitExp_ind(self, ctx:MT22Parser.Exp_indContext):
        return ctx.ID().getText() + self.visit(ctx.expression_list())


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        if ctx.CONCAT():
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinExpr(ctx.CONCAT().getText(), left, right)
        return self.visit(ctx.exp1(0))


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        if ctx.EQUALOP():
            return BinExpr(ctx.EQUALOP().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
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
            return self.visit(ctx.exp2(0))


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
        if ctx.LSB():
            if ctx.expresion_list():
                return self.visit(ctx.expression_list())
            else:
                return self.visit(ctx.exp_ind())
        return self.visit(ctx.operands())


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        if ctx.ID():
            return ctx.ID().getText()
        else:
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#array_cell.
    def visitArray_cell(self, ctx:MT22Parser.Array_cellContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.expression_list()))
    

    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        if ctx.AUTO():
            return ArrayType(self.visit(ctx.expression_list()), AutoType())
        else:
            return ArrayType(self.visit(ctx.expression_list()), self.visit(ctx.var_type()))


    # Visit a parse tree produced by MT22Parser#int_list.
    def visitInt_list(self, ctx:MT22Parser.Int_listContext):
        if ctx.INTLIT():
            return [int(x.getText()) for x in ctx.INTLIT()]
        return []


    # Visit a parse tree produced by MT22Parser#atom_type.
    def visitAtom_type(self, ctx:MT22Parser.Atom_typeContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOL():
            return BooleanLit(ctx.BOOL().getText() == 'true')
        else:
            return StringLit(ctx.STRINGLIT().getText())
        

    # Visit a parse tree produced by MT22Parser#array_lit.
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return ArrayLit(self.visit(ctx.expression_list()))


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        if ctx.exp():
            return [self.visit(x) for x in ctx.exp()]
        return []


    # Visit a parse tree produced by MT22Parser#functions.
    def visitFunctions(self, ctx:MT22Parser.FunctionsContext):
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#readint_func.
    def visitReadint_func(self, ctx:MT22Parser.Readint_funcContext):
        return CallStmt(ctx.READINT(), [])


    # Visit a parse tree produced by MT22Parser#readfloat_func.
    def visitReadfloat_func(self, ctx:MT22Parser.Readfloat_funcContext):
        return CallStmt(ctx.READFLOAT(), [])


    # Visit a parse tree produced by MT22Parser#readbool_func.
    def visitReadbool_func(self, ctx:MT22Parser.Readbool_funcContext):
        return CallStmt(ctx.READBOOL(), [])


    # Visit a parse tree produced by MT22Parser#readstr_func.
    def visitReadstr_func(self, ctx:MT22Parser.Readstr_funcContext):
        return CallStmt(ctx.READSTR(), [])


    # Visit a parse tree produced by MT22Parser#printint_func.
    def visitPrintint_func(self, ctx:MT22Parser.Printint_funcContext):
        return CallStmt(ctx.PRINTINT(), [self.visit(ctx.exp())])


    # Visit a parse tree produced by MT22Parser#printfloat_func.
    def visitPrintfloat_func(self, ctx:MT22Parser.Printfloat_funcContext):
        return CallStmt(ctx.WRITEFLOAT(), [self.visit(ctx.exp())])


    # Visit a parse tree produced by MT22Parser#printbool_func.
    def visitPrintbool_func(self, ctx:MT22Parser.Printbool_funcContext):
        return CallStmt(ctx.PRINTBOOL(), [self.visit(ctx.exp())])


    # Visit a parse tree produced by MT22Parser#printstr_func.
    def visitPrintstr_func(self, ctx:MT22Parser.Printstr_funcContext):
        return CallStmt(ctx.PRINTSTR(), [self.visit(ctx.exp())])


    # Visit a parse tree produced by MT22Parser#supers.
    def visitSupers(self, ctx:MT22Parser.SupersContext):
        return CallStmt(ctx.SUPERS(), [self.visit(ctx.expression_list())])


    # Visit a parse tree produced by MT22Parser#preventdef.
    def visitPreventdef(self, ctx:MT22Parser.PreventdefContext):
        return CallStmt(ctx.PREVENTDEF(), [])