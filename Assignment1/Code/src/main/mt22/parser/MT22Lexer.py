# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u00d6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\7\2;\n\2\f")
        buf.write("\2\16\2>\13\2\3\2\5\2A\n\2\3\3\3\3\3\3\3\3\7\3G\n\3\f")
        buf.write("\3\16\3J\13\3\3\3\5\3M\n\3\5\3O\n\3\3\4\3\4\5\4S\n\4\3")
        buf.write("\4\3\4\3\4\7\4X\n\4\f\4\16\4[\13\4\5\4]\n\4\3\5\3\5\5")
        buf.write("\5a\n\5\3\5\5\5d\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6o\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0087")
        buf.write("\n\7\f\7\16\7\u008a\13\7\3\7\5\7\u008d\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u009a\n\b\3\t\6\t")
        buf.write("\u009d\n\t\r\t\16\t\u009e\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\6\27\u00c3\n\27\r\27\16\27\u00c4")
        buf.write("\3\30\6\30\u00c8\n\30\r\30\16\30\u00c9\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\2\2\34\3\3\5")
        buf.write("\2\7\2\t\4\13\5\r\2\17\6\21\7\23\b\25\t\27\n\31\13\33")
        buf.write("\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63")
        buf.write("\30\65\31\3\2\13\3\2\62\62\3\2\63;\4\2\62;aa\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\3\2$$\4\2C\\c|\5\2\n\f\16\17\"\"\2\u00eb")
        buf.write("\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\3@\3\2\2\2\5N\3\2\2\2\7\\\3\2\2\2\t^\3\2\2")
        buf.write("\2\13n\3\2\2\2\r\u008c\3\2\2\2\17\u0099\3\2\2\2\21\u009c")
        buf.write("\3\2\2\2\23\u00a0\3\2\2\2\25\u00a4\3\2\2\2\27\u00a6\3")
        buf.write("\2\2\2\31\u00a8\3\2\2\2\33\u00aa\3\2\2\2\35\u00ac\3\2")
        buf.write("\2\2\37\u00ae\3\2\2\2!\u00b0\3\2\2\2#\u00b2\3\2\2\2%\u00b9")
        buf.write("\3\2\2\2\'\u00bb\3\2\2\2)\u00bd\3\2\2\2+\u00bf\3\2\2\2")
        buf.write("-\u00c2\3\2\2\2/\u00c7\3\2\2\2\61\u00cd\3\2\2\2\63\u00d0")
        buf.write("\3\2\2\2\65\u00d3\3\2\2\2\67A\t\2\2\28<\t\3\2\29;\t\4")
        buf.write("\2\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2")
        buf.write("><\3\2\2\2?A\b\2\2\2@\67\3\2\2\2@8\3\2\2\2A\4\3\2\2\2")
        buf.write("BC\7\60\2\2CO\t\2\2\2DL\t\3\2\2EG\t\5\2\2FE\3\2\2\2GJ")
        buf.write("\3\2\2\2HF\3\2\2\2HI\3\2\2\2IK\3\2\2\2JH\3\2\2\2KM\t\3")
        buf.write("\2\2LH\3\2\2\2LM\3\2\2\2MO\3\2\2\2NB\3\2\2\2ND\3\2\2\2")
        buf.write("O\6\3\2\2\2PR\t\6\2\2QS\t\7\2\2RQ\3\2\2\2RS\3\2\2\2ST")
        buf.write("\3\2\2\2T]\t\2\2\2UY\t\3\2\2VX\t\5\2\2WV\3\2\2\2X[\3\2")
        buf.write("\2\2YW\3\2\2\2YZ\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2\\P\3\2\2")
        buf.write("\2\\U\3\2\2\2]\b\3\2\2\2^`\5\3\2\2_a\5\5\3\2`_\3\2\2\2")
        buf.write("`a\3\2\2\2ac\3\2\2\2bd\5\7\4\2cb\3\2\2\2cd\3\2\2\2d\n")
        buf.write("\3\2\2\2ef\7v\2\2fg\7t\2\2gh\7w\2\2ho\7g\2\2ij\7h\2\2")
        buf.write("jk\7c\2\2kl\7n\2\2lm\7u\2\2mo\7g\2\2ne\3\2\2\2ni\3\2\2")
        buf.write("\2o\f\3\2\2\2pq\7^\2\2qr\7$\2\2rs\3\2\2\2st\5\r\7\2tu")
        buf.write("\7^\2\2uv\7$\2\2v\u0087\3\2\2\2wx\7^\2\2x\u0087\7d\2\2")
        buf.write("yz\7^\2\2z\u0087\7h\2\2{|\7^\2\2|\u0087\7t\2\2}~\7^\2")
        buf.write("\2~\u0087\7p\2\2\177\u0080\7^\2\2\u0080\u0087\7v\2\2\u0081")
        buf.write("\u0082\7^\2\2\u0082\u0087\7)\2\2\u0083\u0084\7^\2\2\u0084")
        buf.write("\u0087\7^\2\2\u0085\u0087\n\b\2\2\u0086p\3\2\2\2\u0086")
        buf.write("w\3\2\2\2\u0086y\3\2\2\2\u0086{\3\2\2\2\u0086}\3\2\2\2")
        buf.write("\u0086\177\3\2\2\2\u0086\u0081\3\2\2\2\u0086\u0083\3\2")
        buf.write("\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008d\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u0088\3\2\2\2")
        buf.write("\u008c\u008b\3\2\2\2\u008d\16\3\2\2\2\u008e\u008f\7$\2")
        buf.write("\2\u008f\u009a\5\r\7\2\u0090\u0091\7^\2\2\u0091\u0092")
        buf.write("\7$\2\2\u0092\u0093\3\2\2\2\u0093\u0094\5\r\7\2\u0094")
        buf.write("\u0095\7^\2\2\u0095\u0096\7$\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0098\7$\2\2\u0098\u009a\3\2\2\2\u0099\u008e\3\2\2\2")
        buf.write("\u0099\u0090\3\2\2\2\u009a\20\3\2\2\2\u009b\u009d\t\5")
        buf.write("\2\2\u009c\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\22\3\2\2\2\u00a0\u00a1")
        buf.write("\5\21\t\2\u00a1\u00a2\7\60\2\2\u00a2\u00a3\5\21\t\2\u00a3")
        buf.write("\24\3\2\2\2\u00a4\u00a5\7.\2\2\u00a5\26\3\2\2\2\u00a6")
        buf.write("\u00a7\7=\2\2\u00a7\30\3\2\2\2\u00a8\u00a9\7*\2\2\u00a9")
        buf.write("\32\3\2\2\2\u00aa\u00ab\7+\2\2\u00ab\34\3\2\2\2\u00ac")
        buf.write("\u00ad\7}\2\2\u00ad\36\3\2\2\2\u00ae\u00af\7\177\2\2\u00af")
        buf.write(" \3\2\2\2\u00b0\u00b1\7?\2\2\u00b1\"\3\2\2\2\u00b2\u00b3")
        buf.write("\7t\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6")
        buf.write("\7w\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7p\2\2\u00b8$\3")
        buf.write("\2\2\2\u00b9\u00ba\7-\2\2\u00ba&\3\2\2\2\u00bb\u00bc\7")
        buf.write("/\2\2\u00bc(\3\2\2\2\u00bd\u00be\7,\2\2\u00be*\3\2\2\2")
        buf.write("\u00bf\u00c0\7\61\2\2\u00c0,\3\2\2\2\u00c1\u00c3\t\t\2")
        buf.write("\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5.\3\2\2\2\u00c6\u00c8")
        buf.write("\t\n\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00cc\b\30\3\2\u00cc\60\3\2\2\2\u00cd\u00ce\13")
        buf.write("\2\2\2\u00ce\u00cf\b\31\4\2\u00cf\62\3\2\2\2\u00d0\u00d1")
        buf.write("\13\2\2\2\u00d1\u00d2\b\32\5\2\u00d2\64\3\2\2\2\u00d3")
        buf.write("\u00d4\13\2\2\2\u00d4\u00d5\b\33\6\2\u00d5\66\3\2\2\2")
        buf.write("\25\2<@HLNRY\\`cn\u0086\u0088\u008c\u0099\u009e\u00c4")
        buf.write("\u00c9\7\3\2\2\b\2\2\3\31\3\3\32\4\3\33\5")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    BOOL = 3
    STRING = 4
    INTOP = 5
    FLOATOP = 6
    COMMA = 7
    SEMI = 8
    LRB = 9
    RRB = 10
    LCB = 11
    RCB = 12
    EQUAL = 13
    RT = 14
    ADDOP = 15
    MINUSOP = 16
    MULOP = 17
    DIVOP = 18
    ID = 19
    WS = 20
    ERROR_CHAR = 21
    UNCLOSE_STRING = 22
    ILLEGAL_ESCAPE = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "'('", "')'", "'{'", "'}'", "'='", "'return'", 
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "BOOL", "STRING", "INTOP", "FLOATOP", "COMMA", 
            "SEMI", "LRB", "RRB", "LCB", "RCB", "EQUAL", "RT", "ADDOP", 
            "MINUSOP", "MULOP", "DIVOP", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INT", "DECIMAL", "EXPONENT", "FLOAT", "BOOL", "SUBSTR", 
                  "STRING", "INTOP", "FLOATOP", "COMMA", "SEMI", "LRB", 
                  "RRB", "LCB", "RCB", "EQUAL", "RT", "ADDOP", "MINUSOP", 
                  "MULOP", "DIVOP", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INT_action 
            actions[23] = self.ERROR_CHAR_action 
            actions[24] = self.UNCLOSE_STRING_action 
            actions[25] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text)
     


