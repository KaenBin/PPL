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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u01b9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\7\2\177\n\2\f\2\16\2\u0082")
        buf.write("\13\2\3\2\5\2\u0085\n\2\3\3\3\3\5\3\u0089\n\3\3\3\5\3")
        buf.write("\u008c\n\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0094\n\4\f\4\16")
        buf.write("\4\u0097\13\4\3\4\5\4\u009a\n\4\5\4\u009c\n\4\3\5\3\5")
        buf.write("\5\5\u00a0\n\5\3\5\3\5\3\5\7\5\u00a5\n\5\f\5\16\5\u00a8")
        buf.write("\13\5\5\5\u00aa\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u00b5\n\6\3\7\3\7\7\7\u00b9\n\7\f\7\16\7\u00bc")
        buf.write("\13\7\3\7\3\7\3\7\3\b\3\b\5\b\u00c3\n\b\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\7\66\u016d\n\66\f\66\16\66\u0170\13\66")
        buf.write("\3\67\3\67\3\67\3\67\7\67\u0176\n\67\f\67\16\67\u0179")
        buf.write("\13\67\3\67\3\67\3\67\3\67\7\67\u017f\n\67\f\67\16\67")
        buf.write("\u0182\13\67\3\67\3\67\5\67\u0186\n\67\3\67\3\67\38\3")
        buf.write("8\38\38\78\u018e\n8\f8\168\u0191\138\38\38\39\69\u0196")
        buf.write("\n9\r9\169\u0197\39\39\3:\3:\3:\3;\3;\7;\u01a1\n;\f;\16")
        buf.write(";\u01a4\13;\3;\5;\u01a7\n;\3;\3;\3<\3<\7<\u01ad\n<\f<")
        buf.write("\16<\u01b0\13<\3<\3<\3<\3=\3=\3=\5=\u01b8\n=\4\u0177\u0180")
        buf.write("\2>\3\3\5\4\7\2\t\2\13\5\r\6\17\2\21\2\23\7\25\b\27\t")
        buf.write("\31\n\33\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25")
        buf.write("\61\26\63\27\65\30\67\319\32;\33=\34?\35A\36C\37E G!I")
        buf.write("\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65")
        buf.write("q\66s\67u8w9y\2\3\2\21\3\2\62\62\3\2\63;\4\2\62;aa\3\2")
        buf.write("\60\60\3\2\62;\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\n\2")
        buf.write("$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17")
        buf.write("\17\5\2\n\f\16\17\"\"\7\3\n\f\16\17$$))^^\3\2^^\2\u01c9")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3\u0084\3")
        buf.write("\2\2\2\5\u0086\3\2\2\2\7\u008f\3\2\2\2\t\u00a9\3\2\2\2")
        buf.write("\13\u00b4\3\2\2\2\r\u00b6\3\2\2\2\17\u00c2\3\2\2\2\21")
        buf.write("\u00c4\3\2\2\2\23\u00c7\3\2\2\2\25\u00c9\3\2\2\2\27\u00cb")
        buf.write("\3\2\2\2\31\u00cd\3\2\2\2\33\u00cf\3\2\2\2\35\u00d1\3")
        buf.write("\2\2\2\37\u00d3\3\2\2\2!\u00d5\3\2\2\2#\u00d7\3\2\2\2")
        buf.write("%\u00d9\3\2\2\2\'\u00db\3\2\2\2)\u00dd\3\2\2\2+\u00df")
        buf.write("\3\2\2\2-\u00e1\3\2\2\2/\u00e3\3\2\2\2\61\u00e5\3\2\2")
        buf.write("\2\63\u00e7\3\2\2\2\65\u00e9\3\2\2\2\67\u00ec\3\2\2\2")
        buf.write("9\u00ef\3\2\2\2;\u00f2\3\2\2\2=\u00f5\3\2\2\2?\u00f7\3")
        buf.write("\2\2\2A\u00fa\3\2\2\2C\u00fc\3\2\2\2E\u00ff\3\2\2\2G\u0102")
        buf.write("\3\2\2\2I\u010a\3\2\2\2K\u0110\3\2\2\2M\u0117\3\2\2\2")
        buf.write("O\u011d\3\2\2\2Q\u0120\3\2\2\2S\u0125\3\2\2\2U\u012a\3")
        buf.write("\2\2\2W\u0132\3\2\2\2Y\u0136\3\2\2\2[\u013f\3\2\2\2]\u0142")
        buf.write("\3\2\2\2_\u0147\3\2\2\2a\u014b\3\2\2\2c\u0151\3\2\2\2")
        buf.write("e\u0154\3\2\2\2g\u015a\3\2\2\2i\u0163\3\2\2\2k\u016a\3")
        buf.write("\2\2\2m\u0185\3\2\2\2o\u0189\3\2\2\2q\u0195\3\2\2\2s\u019b")
        buf.write("\3\2\2\2u\u019e\3\2\2\2w\u01aa\3\2\2\2y\u01b7\3\2\2\2")
        buf.write("{\u0085\t\2\2\2|\u0080\t\3\2\2}\177\t\4\2\2~}\3\2\2\2")
        buf.write("\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2")
        buf.write("\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0085\b")
        buf.write("\2\2\2\u0084{\3\2\2\2\u0084|\3\2\2\2\u0085\4\3\2\2\2\u0086")
        buf.write("\u0088\5\3\2\2\u0087\u0089\5\7\4\2\u0088\u0087\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u008c\5")
        buf.write("\t\5\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d")
        buf.write("\3\2\2\2\u008d\u008e\b\3\3\2\u008e\6\3\2\2\2\u008f\u009b")
        buf.write("\t\5\2\2\u0090\u009c\t\2\2\2\u0091\u0099\t\3\2\2\u0092")
        buf.write("\u0094\t\6\2\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2")
        buf.write("\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a\t\3\2\2\u0099\u0095")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2\u009b")
        buf.write("\u0090\3\2\2\2\u009b\u0091\3\2\2\2\u009c\b\3\2\2\2\u009d")
        buf.write("\u009f\t\7\2\2\u009e\u00a0\t\b\2\2\u009f\u009e\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00aa\t")
        buf.write("\2\2\2\u00a2\u00a6\t\3\2\2\u00a3\u00a5\t\6\2\2\u00a4\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a9\u009d\3\2\2\2\u00a9\u00a2\3\2\2\2\u00aa\n\3\2\2")
        buf.write("\2\u00ab\u00ac\7v\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7")
        buf.write("w\2\2\u00ae\u00b5\7g\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b5")
        buf.write("\7g\2\2\u00b4\u00ab\3\2\2\2\u00b4\u00af\3\2\2\2\u00b5")
        buf.write("\f\3\2\2\2\u00b6\u00ba\7$\2\2\u00b7\u00b9\5\17\b\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bd\u00be\7$\2\2\u00be\u00bf\b\7\4\2\u00bf\16")
        buf.write("\3\2\2\2\u00c0\u00c3\n\t\2\2\u00c1\u00c3\5\21\t\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\20\3\2\2\2\u00c4")
        buf.write("\u00c5\7^\2\2\u00c5\u00c6\t\n\2\2\u00c6\22\3\2\2\2\u00c7")
        buf.write("\u00c8\7]\2\2\u00c8\24\3\2\2\2\u00c9\u00ca\7_\2\2\u00ca")
        buf.write("\26\3\2\2\2\u00cb\u00cc\7*\2\2\u00cc\30\3\2\2\2\u00cd")
        buf.write("\u00ce\7+\2\2\u00ce\32\3\2\2\2\u00cf\u00d0\7}\2\2\u00d0")
        buf.write("\34\3\2\2\2\u00d1\u00d2\7\177\2\2\u00d2\36\3\2\2\2\u00d3")
        buf.write("\u00d4\7\60\2\2\u00d4 \3\2\2\2\u00d5\u00d6\7.\2\2\u00d6")
        buf.write("\"\3\2\2\2\u00d7\u00d8\7=\2\2\u00d8$\3\2\2\2\u00d9\u00da")
        buf.write("\7<\2\2\u00da&\3\2\2\2\u00db\u00dc\7?\2\2\u00dc(\3\2\2")
        buf.write("\2\u00dd\u00de\7-\2\2\u00de*\3\2\2\2\u00df\u00e0\7/\2")
        buf.write("\2\u00e0,\3\2\2\2\u00e1\u00e2\7,\2\2\u00e2.\3\2\2\2\u00e3")
        buf.write("\u00e4\7\61\2\2\u00e4\60\3\2\2\2\u00e5\u00e6\7\'\2\2\u00e6")
        buf.write("\62\3\2\2\2\u00e7\u00e8\7#\2\2\u00e8\64\3\2\2\2\u00e9")
        buf.write("\u00ea\7(\2\2\u00ea\u00eb\7(\2\2\u00eb\66\3\2\2\2\u00ec")
        buf.write("\u00ed\7~\2\2\u00ed\u00ee\7~\2\2\u00ee8\3\2\2\2\u00ef")
        buf.write("\u00f0\7?\2\2\u00f0\u00f1\7?\2\2\u00f1:\3\2\2\2\u00f2")
        buf.write("\u00f3\7#\2\2\u00f3\u00f4\7?\2\2\u00f4<\3\2\2\2\u00f5")
        buf.write("\u00f6\7>\2\2\u00f6>\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8")
        buf.write("\u00f9\7?\2\2\u00f9@\3\2\2\2\u00fa\u00fb\7@\2\2\u00fb")
        buf.write("B\3\2\2\2\u00fc\u00fd\7@\2\2\u00fd\u00fe\7?\2\2\u00fe")
        buf.write("D\3\2\2\2\u00ff\u0100\7<\2\2\u0100\u0101\7<\2\2\u0101")
        buf.write("F\3\2\2\2\u0102\u0103\7k\2\2\u0103\u0104\7p\2\2\u0104")
        buf.write("\u0105\7v\2\2\u0105\u0106\7g\2\2\u0106\u0107\7i\2\2\u0107")
        buf.write("\u0108\7g\2\2\u0108\u0109\7t\2\2\u0109H\3\2\2\2\u010a")
        buf.write("\u010b\7h\2\2\u010b\u010c\7n\2\2\u010c\u010d\7q\2\2\u010d")
        buf.write("\u010e\7c\2\2\u010e\u010f\7v\2\2\u010fJ\3\2\2\2\u0110")
        buf.write("\u0111\7u\2\2\u0111\u0112\7v\2\2\u0112\u0113\7t\2\2\u0113")
        buf.write("\u0114\7k\2\2\u0114\u0115\7p\2\2\u0115\u0116\7i\2\2\u0116")
        buf.write("L\3\2\2\2\u0117\u0118\7c\2\2\u0118\u0119\7t\2\2\u0119")
        buf.write("\u011a\7t\2\2\u011a\u011b\7c\2\2\u011b\u011c\7{\2\2\u011c")
        buf.write("N\3\2\2\2\u011d\u011e\7q\2\2\u011e\u011f\7h\2\2\u011f")
        buf.write("P\3\2\2\2\u0120\u0121\7x\2\2\u0121\u0122\7q\2\2\u0122")
        buf.write("\u0123\7k\2\2\u0123\u0124\7f\2\2\u0124R\3\2\2\2\u0125")
        buf.write("\u0126\7c\2\2\u0126\u0127\7w\2\2\u0127\u0128\7v\2\2\u0128")
        buf.write("\u0129\7q\2\2\u0129T\3\2\2\2\u012a\u012b\7k\2\2\u012b")
        buf.write("\u012c\7p\2\2\u012c\u012d\7j\2\2\u012d\u012e\7k\2\2\u012e")
        buf.write("\u012f\7t\2\2\u012f\u0130\7k\2\2\u0130\u0131\7v\2\2\u0131")
        buf.write("V\3\2\2\2\u0132\u0133\7q\2\2\u0133\u0134\7w\2\2\u0134")
        buf.write("\u0135\7v\2\2\u0135X\3\2\2\2\u0136\u0137\7h\2\2\u0137")
        buf.write("\u0138\7w\2\2\u0138\u0139\7p\2\2\u0139\u013a\7e\2\2\u013a")
        buf.write("\u013b\7v\2\2\u013b\u013c\7k\2\2\u013c\u013d\7q\2\2\u013d")
        buf.write("\u013e\7p\2\2\u013eZ\3\2\2\2\u013f\u0140\7k\2\2\u0140")
        buf.write("\u0141\7h\2\2\u0141\\\3\2\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write("\u0144\7n\2\2\u0144\u0145\7u\2\2\u0145\u0146\7g\2\2\u0146")
        buf.write("^\3\2\2\2\u0147\u0148\7h\2\2\u0148\u0149\7q\2\2\u0149")
        buf.write("\u014a\7t\2\2\u014a`\3\2\2\2\u014b\u014c\7y\2\2\u014c")
        buf.write("\u014d\7j\2\2\u014d\u014e\7k\2\2\u014e\u014f\7n\2\2\u014f")
        buf.write("\u0150\7g\2\2\u0150b\3\2\2\2\u0151\u0152\7f\2\2\u0152")
        buf.write("\u0153\7q\2\2\u0153d\3\2\2\2\u0154\u0155\7d\2\2\u0155")
        buf.write("\u0156\7t\2\2\u0156\u0157\7g\2\2\u0157\u0158\7c\2\2\u0158")
        buf.write("\u0159\7m\2\2\u0159f\3\2\2\2\u015a\u015b\7e\2\2\u015b")
        buf.write("\u015c\7q\2\2\u015c\u015d\7p\2\2\u015d\u015e\7v\2\2\u015e")
        buf.write("\u015f\7k\2\2\u015f\u0160\7p\2\2\u0160\u0161\7w\2\2\u0161")
        buf.write("\u0162\7g\2\2\u0162h\3\2\2\2\u0163\u0164\7t\2\2\u0164")
        buf.write("\u0165\7g\2\2\u0165\u0166\7v\2\2\u0166\u0167\7w\2\2\u0167")
        buf.write("\u0168\7t\2\2\u0168\u0169\7p\2\2\u0169j\3\2\2\2\u016a")
        buf.write("\u016e\t\13\2\2\u016b\u016d\t\f\2\2\u016c\u016b\3\2\2")
        buf.write("\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f")
        buf.write("\3\2\2\2\u016fl\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0172")
        buf.write("\7*\2\2\u0172\u0173\7,\2\2\u0173\u0177\3\2\2\2\u0174\u0176")
        buf.write("\13\2\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017a\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u017a\u017b\7,\2\2\u017b\u0186\7")
        buf.write("+\2\2\u017c\u0180\5\33\16\2\u017d\u017f\13\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0180\3")
        buf.write("\2\2\2\u0183\u0184\5\35\17\2\u0184\u0186\3\2\2\2\u0185")
        buf.write("\u0171\3\2\2\2\u0185\u017c\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0188\b\67\5\2\u0188n\3\2\2\2\u0189\u018a\7\61")
        buf.write("\2\2\u018a\u018b\7\61\2\2\u018b\u018f\3\2\2\2\u018c\u018e")
        buf.write("\n\r\2\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0192\u0193\b8\5\2\u0193p\3\2\2\2")
        buf.write("\u0194\u0196\t\16\2\2\u0195\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199\u019a\b9\5\2\u019ar\3\2\2\2\u019b")
        buf.write("\u019c\13\2\2\2\u019c\u019d\b:\6\2\u019dt\3\2\2\2\u019e")
        buf.write("\u01a2\7$\2\2\u019f\u01a1\5\17\b\2\u01a0\u019f\3\2\2\2")
        buf.write("\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3")
        buf.write("\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a7")
        buf.write("\t\17\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("\u01a9\b;\7\2\u01a9v\3\2\2\2\u01aa\u01ae\7$\2\2\u01ab")
        buf.write("\u01ad\5\17\b\2\u01ac\u01ab\3\2\2\2\u01ad\u01b0\3\2\2")
        buf.write("\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\5y=\2\u01b2\u01b3")
        buf.write("\b<\b\2\u01b3x\3\2\2\2\u01b4\u01b5\7^\2\2\u01b5\u01b8")
        buf.write("\n\n\2\2\u01b6\u01b8\n\20\2\2\u01b7\u01b4\3\2\2\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8z\3\2\2\2\32\2\u0080\u0084\u0088\u008b")
        buf.write("\u0095\u0099\u009b\u009f\u00a6\u00a9\u00b4\u00ba\u00c2")
        buf.write("\u016e\u0177\u0180\u0185\u018f\u0197\u01a2\u01a6\u01ae")
        buf.write("\u01b7\t\3\2\2\3\3\3\3\7\4\b\2\2\3:\5\3;\6\3<\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOL = 3
    STRINGLIT = 4
    LSB = 5
    RSB = 6
    LRB = 7
    RRB = 8
    LCB = 9
    RCB = 10
    DOT = 11
    COMMA = 12
    SEMI = 13
    COLON = 14
    ASSIGN = 15
    ADDOP = 16
    MINUSOP = 17
    MULOP = 18
    DIVOP = 19
    MODOP = 20
    NEGAOP = 21
    CONJOP = 22
    DISJOP = 23
    EQUALOP = 24
    DIFOP = 25
    LESSOP = 26
    LESSEQOP = 27
    GREATOP = 28
    GREATEQOP = 29
    CONCAT = 30
    INTEGER = 31
    FLOAT = 32
    STRING = 33
    ARRAY = 34
    OF = 35
    VOID = 36
    AUTO = 37
    INHIRIT = 38
    OUT = 39
    FUNCTION = 40
    IF = 41
    ELSE = 42
    FOR = 43
    WHILE = 44
    DO = 45
    BREAK = 46
    CONT = 47
    RT = 48
    ID = 49
    BLOCK_COMMENT = 50
    LINE_COMMENT = 51
    WS = 52
    ERROR_CHAR = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'('", "')'", "'{'", "'}'", "'.'", "','", "';'", 
            "':'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'integer'", "'float'", "'string'", "'array'", "'of'", "'void'", 
            "'auto'", "'inhirit'", "'out'", "'function'", "'if'", "'else'", 
            "'for'", "'while'", "'do'", "'break'", "'continue'", "'return'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOL", "STRINGLIT", "LSB", "RSB", "LRB", 
            "RRB", "LCB", "RCB", "DOT", "COMMA", "SEMI", "COLON", "ASSIGN", 
            "ADDOP", "MINUSOP", "MULOP", "DIVOP", "MODOP", "NEGAOP", "CONJOP", 
            "DISJOP", "EQUALOP", "DIFOP", "LESSOP", "LESSEQOP", "GREATOP", 
            "GREATEQOP", "CONCAT", "INTEGER", "FLOAT", "STRING", "ARRAY", 
            "OF", "VOID", "AUTO", "INHIRIT", "OUT", "FUNCTION", "IF", "ELSE", 
            "FOR", "WHILE", "DO", "BREAK", "CONT", "RT", "ID", "BLOCK_COMMENT", 
            "LINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTLIT", "FLOATLIT", "DECIMAL", "EXPONENT", "BOOL", "STRINGLIT", 
                  "STR_CHAR", "ESC_SEQ", "LSB", "RSB", "LRB", "RRB", "LCB", 
                  "RCB", "DOT", "COMMA", "SEMI", "COLON", "ASSIGN", "ADDOP", 
                  "MINUSOP", "MULOP", "DIVOP", "MODOP", "NEGAOP", "CONJOP", 
                  "DISJOP", "EQUALOP", "DIFOP", "LESSOP", "LESSEQOP", "GREATOP", 
                  "GREATEQOP", "CONCAT", "INTEGER", "FLOAT", "STRING", "ARRAY", 
                  "OF", "VOID", "AUTO", "INHIRIT", "OUT", "FUNCTION", "IF", 
                  "ELSE", "FOR", "WHILE", "DO", "BREAK", "CONT", "RT", "ID", 
                  "BLOCK_COMMENT", "LINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL" ]

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
            actions[0] = self.INTLIT_action 
            actions[1] = self.FLOATLIT_action 
            actions[5] = self.STRINGLIT_action 
            actions[56] = self.ERROR_CHAR_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


