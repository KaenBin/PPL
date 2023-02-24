# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("\u00b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\5\4")
        buf.write(">\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7J\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5")
        buf.write("\nY\n\n\3\13\3\13\3\13\3\13\3\13\5\13`\n\13\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16p\n\16\3\17\3\17\3\17\5\17u\n\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u008e")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u0095\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u009d\n\26\f\26\16\26\u00a0")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00aa")
        buf.write("\n\27\3\30\3\30\3\30\3\30\5\30\u00b0\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u00b7\n\31\3\31\2\3*\32\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\4\3\2\3\4\3")
        buf.write("\2\23\24\2\u00b2\2\62\3\2\2\2\49\3\2\2\2\6=\3\2\2\2\b")
        buf.write("?\3\2\2\2\nA\3\2\2\2\fI\3\2\2\2\16K\3\2\2\2\20P\3\2\2")
        buf.write("\2\22X\3\2\2\2\24_\3\2\2\2\26a\3\2\2\2\30d\3\2\2\2\32")
        buf.write("o\3\2\2\2\34t\3\2\2\2\36x\3\2\2\2 |\3\2\2\2\"\u0081\3")
        buf.write("\2\2\2$\u0084\3\2\2\2&\u008d\3\2\2\2(\u0094\3\2\2\2*\u0096")
        buf.write("\3\2\2\2,\u00a9\3\2\2\2.\u00af\3\2\2\2\60\u00b6\3\2\2")
        buf.write("\2\62\63\5\4\3\2\63\64\7\2\2\3\64\3\3\2\2\2\65\66\5\6")
        buf.write("\4\2\66\67\5\4\3\2\67:\3\2\2\28:\5\6\4\29\65\3\2\2\29")
        buf.write("8\3\2\2\2:\5\3\2\2\2;>\5\n\6\2<>\5\16\b\2=;\3\2\2\2=<")
        buf.write("\3\2\2\2>\7\3\2\2\2?@\t\2\2\2@\t\3\2\2\2AB\5\b\5\2BC\5")
        buf.write("\f\7\2CD\7\n\2\2D\13\3\2\2\2EF\7\25\2\2FG\7\t\2\2GJ\5")
        buf.write("\f\7\2HJ\7\25\2\2IE\3\2\2\2IH\3\2\2\2J\r\3\2\2\2KL\5\b")
        buf.write("\5\2LM\7\25\2\2MN\5\20\t\2NO\5\30\r\2O\17\3\2\2\2PQ\7")
        buf.write("\13\2\2QR\5\22\n\2RS\7\f\2\2S\21\3\2\2\2TU\5\26\f\2UV")
        buf.write("\5\24\13\2VY\3\2\2\2WY\3\2\2\2XT\3\2\2\2XW\3\2\2\2Y\23")
        buf.write("\3\2\2\2Z[\7\n\2\2[\\\5\26\f\2\\]\5\24\13\2]`\3\2\2\2")
        buf.write("^`\3\2\2\2_Z\3\2\2\2_^\3\2\2\2`\25\3\2\2\2ab\5\b\5\2b")
        buf.write("c\5\f\7\2c\27\3\2\2\2de\7\r\2\2ef\5\32\16\2fg\7\16\2\2")
        buf.write("g\31\3\2\2\2hi\5\n\6\2ij\5\32\16\2jp\3\2\2\2kl\5\34\17")
        buf.write("\2lm\5\32\16\2mp\3\2\2\2np\3\2\2\2oh\3\2\2\2ok\3\2\2\2")
        buf.write("on\3\2\2\2p\33\3\2\2\2qu\5\36\20\2ru\5 \21\2su\5\"\22")
        buf.write("\2tq\3\2\2\2tr\3\2\2\2ts\3\2\2\2uv\3\2\2\2vw\7\n\2\2w")
        buf.write("\35\3\2\2\2xy\7\25\2\2yz\7\17\2\2z{\5&\24\2{\37\3\2\2")
        buf.write("\2|}\7\25\2\2}~\7\13\2\2~\177\5.\30\2\177\u0080\7\f\2")
        buf.write("\2\u0080!\3\2\2\2\u0081\u0082\7\20\2\2\u0082\u0083\5&")
        buf.write("\24\2\u0083#\3\2\2\2\u0084\u0085\7\r\2\2\u0085\u0086\5")
        buf.write("&\24\2\u0086\u0087\7\16\2\2\u0087%\3\2\2\2\u0088\u0089")
        buf.write("\5(\25\2\u0089\u008a\7\21\2\2\u008a\u008b\5&\24\2\u008b")
        buf.write("\u008e\3\2\2\2\u008c\u008e\5(\25\2\u008d\u0088\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\'\3\2\2\2\u008f\u0090\5*\26")
        buf.write("\2\u0090\u0091\7\22\2\2\u0091\u0092\5(\25\2\u0092\u0095")
        buf.write("\3\2\2\2\u0093\u0095\5*\26\2\u0094\u008f\3\2\2\2\u0094")
        buf.write("\u0093\3\2\2\2\u0095)\3\2\2\2\u0096\u0097\b\26\1\2\u0097")
        buf.write("\u0098\5,\27\2\u0098\u009e\3\2\2\2\u0099\u009a\f\4\2\2")
        buf.write("\u009a\u009b\t\3\2\2\u009b\u009d\5,\27\2\u009c\u0099\3")
        buf.write("\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f+\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00aa")
        buf.write("\7\7\2\2\u00a2\u00aa\7\b\2\2\u00a3\u00aa\7\25\2\2\u00a4")
        buf.write("\u00aa\5 \21\2\u00a5\u00a6\7\13\2\2\u00a6\u00a7\5&\24")
        buf.write("\2\u00a7\u00a8\7\f\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a1")
        buf.write("\3\2\2\2\u00a9\u00a2\3\2\2\2\u00a9\u00a3\3\2\2\2\u00a9")
        buf.write("\u00a4\3\2\2\2\u00a9\u00a5\3\2\2\2\u00aa-\3\2\2\2\u00ab")
        buf.write("\u00ac\5&\24\2\u00ac\u00ad\5\60\31\2\u00ad\u00b0\3\2\2")
        buf.write("\2\u00ae\u00b0\3\2\2\2\u00af\u00ab\3\2\2\2\u00af\u00ae")
        buf.write("\3\2\2\2\u00b0/\3\2\2\2\u00b1\u00b2\7\t\2\2\u00b2\u00b3")
        buf.write("\5&\24\2\u00b3\u00b4\5\60\31\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b7\3\2\2\2\u00b6\u00b1\3\2\2\2\u00b6\u00b5\3\2\2\2")
        buf.write("\u00b7\61\3\2\2\2\179=IX_ot\u008d\u0094\u009e\u00a9\u00af")
        buf.write("\u00b6")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "';'", 
                     "'('", "')'", "'{'", "'}'", "'='", "'return'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "BOOL", "STRING", "INTOP", 
                      "FLOATOP", "COMMA", "SEMI", "LRB", "RRB", "LCB", "RCB", 
                      "EQUAL", "RT", "ADDOP", "MINUSOP", "MULOP", "DIVOP", 
                      "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_var_type = 3
    RULE_vardecl = 4
    RULE_id_list = 5
    RULE_funcdecl = 6
    RULE_paradecl = 7
    RULE_para_list1 = 8
    RULE_para_list2 = 9
    RULE_para = 10
    RULE_body = 11
    RULE_var_stmts = 12
    RULE_stmts = 13
    RULE_assign = 14
    RULE_call = 15
    RULE_return_stmt = 16
    RULE_array = 17
    RULE_expr = 18
    RULE_expr1 = 19
    RULE_expr2 = 20
    RULE_operand = 21
    RULE_expr_list1 = 22
    RULE_expr_list2 = 23

    ruleNames =  [ "program", "decls", "decl", "var_type", "vardecl", "id_list", 
                   "funcdecl", "paradecl", "para_list1", "para_list2", "para", 
                   "body", "var_stmts", "stmts", "assign", "call", "return_stmt", 
                   "array", "expr", "expr1", "expr2", "operand", "expr_list1", 
                   "expr_list2" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    BOOL=3
    STRING=4
    INTOP=5
    FLOATOP=6
    COMMA=7
    SEMI=8
    LRB=9
    RRB=10
    LCB=11
    RCB=12
    EQUAL=13
    RT=14
    ADDOP=15
    MINUSOP=16
    MULOP=17
    DIVOP=18
    ID=19
    WS=20
    ERROR_CHAR=21
    UNCLOSE_STRING=22
    ILLEGAL_ESCAPE=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.decls()
            self.state = 49
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.decl()
                self.state = 52
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MT22Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_var_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = MT22Parser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==MT22Parser.INT or _la==MT22Parser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(MT22Parser.Var_typeContext,0)


        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.var_type()
            self.state = 64
            self.id_list()
            self.state = 65
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MT22Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_id_list)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(MT22Parser.ID)
                self.state = 68
                self.match(MT22Parser.COMMA)
                self.state = 69
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(MT22Parser.Var_typeContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def paradecl(self):
            return self.getTypedRuleContext(MT22Parser.ParadeclContext,0)


        def body(self):
            return self.getTypedRuleContext(MT22Parser.BodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.var_type()
            self.state = 74
            self.match(MT22Parser.ID)
            self.state = 75
            self.paradecl()
            self.state = 76
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParadeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def para_list1(self):
            return self.getTypedRuleContext(MT22Parser.Para_list1Context,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paradecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParadecl" ):
                return visitor.visitParadecl(self)
            else:
                return visitor.visitChildren(self)




    def paradecl(self):

        localctx = MT22Parser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paradecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MT22Parser.LRB)
            self.state = 79
            self.para_list1()
            self.state = 80
            self.match(MT22Parser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_list1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(MT22Parser.ParaContext,0)


        def para_list2(self):
            return self.getTypedRuleContext(MT22Parser.Para_list2Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_para_list1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list1" ):
                return visitor.visitPara_list1(self)
            else:
                return visitor.visitChildren(self)




    def para_list1(self):

        localctx = MT22Parser.Para_list1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_para_list1)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INT, MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.para()
                self.state = 83
                self.para_list2()
                pass
            elif token in [MT22Parser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_list2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def para(self):
            return self.getTypedRuleContext(MT22Parser.ParaContext,0)


        def para_list2(self):
            return self.getTypedRuleContext(MT22Parser.Para_list2Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_para_list2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list2" ):
                return visitor.visitPara_list2(self)
            else:
                return visitor.visitChildren(self)




    def para_list2(self):

        localctx = MT22Parser.Para_list2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_para_list2)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(MT22Parser.SEMI)
                self.state = 89
                self.para()
                self.state = 90
                self.para_list2()
                pass
            elif token in [MT22Parser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(MT22Parser.Var_typeContext,0)


        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MT22Parser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.var_type()
            self.state = 96
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def var_stmts(self):
            return self.getTypedRuleContext(MT22Parser.Var_stmtsContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MT22Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MT22Parser.LCB)
            self.state = 99
            self.var_stmts()
            self.state = 100
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def var_stmts(self):
            return self.getTypedRuleContext(MT22Parser.Var_stmtsContext,0)


        def stmts(self):
            return self.getTypedRuleContext(MT22Parser.StmtsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_var_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_stmts" ):
                return visitor.visitVar_stmts(self)
            else:
                return visitor.visitChildren(self)




    def var_stmts(self):

        localctx = MT22Parser.Var_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var_stmts)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INT, MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.vardecl()
                self.state = 103
                self.var_stmts()
                pass
            elif token in [MT22Parser.RT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.stmts()
                self.state = 106
                self.var_stmts()
                pass
            elif token in [MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def assign(self):
            return self.getTypedRuleContext(MT22Parser.AssignContext,0)


        def call(self):
            return self.getTypedRuleContext(MT22Parser.CallContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = MT22Parser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 111
                self.assign()
                pass

            elif la_ == 2:
                self.state = 112
                self.call()
                pass

            elif la_ == 3:
                self.state = 113
                self.return_stmt()
                pass


            self.state = 116
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MT22Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MT22Parser.ID)
            self.state = 119
            self.match(MT22Parser.EQUAL)
            self.state = 120
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def expr_list1(self):
            return self.getTypedRuleContext(MT22Parser.Expr_list1Context,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = MT22Parser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(MT22Parser.ID)
            self.state = 123
            self.match(MT22Parser.LRB)
            self.state = 124
            self.expr_list1()
            self.state = 125
            self.match(MT22Parser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RT(self):
            return self.getToken(MT22Parser.RT, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MT22Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MT22Parser.RT)
            self.state = 128
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MT22Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MT22Parser.LCB)
            self.state = 131
            self.expr()
            self.state = 132
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MT22Parser.Expr1Context,0)


        def ADDOP(self):
            return self.getToken(MT22Parser.ADDOP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.expr1()
                self.state = 135
                self.match(MT22Parser.ADDOP)
                self.state = 136
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def MINUSOP(self):
            return self.getToken(MT22Parser.MINUSOP, 0)

        def expr1(self):
            return self.getTypedRuleContext(MT22Parser.Expr1Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr1)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.expr2(0)
                self.state = 142
                self.match(MT22Parser.MINUSOP)
                self.state = 143
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def MULOP(self):
            return self.getToken(MT22Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MT22Parser.DIVOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 151
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 152
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.MULOP or _la==MT22Parser.DIVOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 153
                    self.operand() 
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTOP(self):
            return self.getToken(MT22Parser.INTOP, 0)

        def FLOATOP(self):
            return self.getToken(MT22Parser.FLOATOP, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def call(self):
            return self.getTypedRuleContext(MT22Parser.CallContext,0)


        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operand)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(MT22Parser.INTOP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(MT22Parser.FLOATOP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.match(MT22Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.match(MT22Parser.LRB)
                self.state = 164
                self.expr()
                self.state = 165
                self.match(MT22Parser.RRB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_list1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def expr_list2(self):
            return self.getTypedRuleContext(MT22Parser.Expr_list2Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr_list1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list1" ):
                return visitor.visitExpr_list1(self)
            else:
                return visitor.visitChildren(self)




    def expr_list1(self):

        localctx = MT22Parser.Expr_list1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_list1)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTOP, MT22Parser.FLOATOP, MT22Parser.LRB, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.expr()
                self.state = 170
                self.expr_list2()
                pass
            elif token in [MT22Parser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_list2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def expr_list2(self):
            return self.getTypedRuleContext(MT22Parser.Expr_list2Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr_list2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list2" ):
                return visitor.visitExpr_list2(self)
            else:
                return visitor.visitChildren(self)




    def expr_list2(self):

        localctx = MT22Parser.Expr_list2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr_list2)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(MT22Parser.COMMA)
                self.state = 176
                self.expr()
                self.state = 177
                self.expr_list2()
                pass
            elif token in [MT22Parser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




