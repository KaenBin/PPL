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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01b6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\7\2\u0081\n\2\f\2")
        buf.write("\16\2\u0084\13\2\3\2\5\2\u0087\n\2\3\3\3\3\5\3\u008b\n")
        buf.write("\3\3\3\5\3\u008e\n\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0096")
        buf.write("\n\4\f\4\16\4\u0099\13\4\3\4\5\4\u009c\n\4\5\4\u009e\n")
        buf.write("\4\3\5\3\5\5\5\u00a2\n\5\3\5\3\5\3\5\7\5\u00a7\n\5\f\5")
        buf.write("\16\5\u00aa\13\5\5\5\u00ac\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u00b7\n\6\3\7\3\7\7\7\u00bb\n\7\f\7\16")
        buf.write("\7\u00be\13\7\3\7\3\7\3\7\3\b\3\b\5\b\u00c5\n\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\7\67\u0177\n\67\f\67\16\67\u017a\13\67\38\38\38")
        buf.write("\38\78\u0180\n8\f8\168\u0183\138\38\38\38\38\38\39\39")
        buf.write("\39\39\79\u018e\n9\f9\169\u0191\139\39\39\3:\6:\u0196")
        buf.write("\n:\r:\16:\u0197\3:\3:\3;\3;\3;\3<\3<\7<\u01a1\n<\f<\16")
        buf.write("<\u01a4\13<\3<\3<\3=\3=\7=\u01aa\n=\f=\16=\u01ad\13=\3")
        buf.write("=\3=\3=\3>\3>\3>\5>\u01b5\n>\2\2?\3\3\5\4\7\2\t\2\13\5")
        buf.write("\r\6\17\2\21\2\23\7\25\b\27\t\31\n\33\13\35\f\37\r!\16")
        buf.write("#\17%\20\'\21)\22+\23-\24/\25\61\26\63\27\65\30\67\31")
        buf.write("9\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+],_")
        buf.write("-a.c/e\60g\61i\62k\63m\64o\65q\66s\67u8w9y:{\2\3\2\22")
        buf.write("\3\2\62\62\3\2\63;\4\2\62;aa\3\2\60\60\3\2\62;\4\2GGg")
        buf.write("g\4\2--//\4\2\f\f$$\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\3\2,,\4\2\f\f\17\17\5\2\n\f\16\17\"\"\4\2")
        buf.write("$$pp\3\2^^\2\u01c4\2\3\3\2\2\2\2\5\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\3\u0086\3\2\2\2\5\u0088\3\2\2\2")
        buf.write("\7\u0091\3\2\2\2\t\u009f\3\2\2\2\13\u00b6\3\2\2\2\r\u00b8")
        buf.write("\3\2\2\2\17\u00c4\3\2\2\2\21\u00c6\3\2\2\2\23\u00c9\3")
        buf.write("\2\2\2\25\u00cb\3\2\2\2\27\u00cd\3\2\2\2\31\u00cf\3\2")
        buf.write("\2\2\33\u00d1\3\2\2\2\35\u00d3\3\2\2\2\37\u00d5\3\2\2")
        buf.write("\2!\u00d7\3\2\2\2#\u00d9\3\2\2\2%\u00db\3\2\2\2\'\u00dd")
        buf.write("\3\2\2\2)\u00df\3\2\2\2+\u00e1\3\2\2\2-\u00e3\3\2\2\2")
        buf.write("/\u00e5\3\2\2\2\61\u00e7\3\2\2\2\63\u00e9\3\2\2\2\65\u00eb")
        buf.write("\3\2\2\2\67\u00ee\3\2\2\29\u00f1\3\2\2\2;\u00f4\3\2\2")
        buf.write("\2=\u00f7\3\2\2\2?\u00f9\3\2\2\2A\u00fc\3\2\2\2C\u00fe")
        buf.write("\3\2\2\2E\u0101\3\2\2\2G\u0104\3\2\2\2I\u010c\3\2\2\2")
        buf.write("K\u0112\3\2\2\2M\u011a\3\2\2\2O\u0121\3\2\2\2Q\u0127\3")
        buf.write("\2\2\2S\u012a\3\2\2\2U\u012f\3\2\2\2W\u0134\3\2\2\2Y\u013c")
        buf.write("\3\2\2\2[\u0140\3\2\2\2]\u0149\3\2\2\2_\u014c\3\2\2\2")
        buf.write("a\u0151\3\2\2\2c\u0155\3\2\2\2e\u015b\3\2\2\2g\u015e\3")
        buf.write("\2\2\2i\u0164\3\2\2\2k\u016d\3\2\2\2m\u0174\3\2\2\2o\u017b")
        buf.write("\3\2\2\2q\u0189\3\2\2\2s\u0195\3\2\2\2u\u019b\3\2\2\2")
        buf.write("w\u019e\3\2\2\2y\u01a7\3\2\2\2{\u01b4\3\2\2\2}\u0087\t")
        buf.write("\2\2\2~\u0082\t\3\2\2\177\u0081\t\4\2\2\u0080\177\3\2")
        buf.write("\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085")
        buf.write("\u0087\b\2\2\2\u0086}\3\2\2\2\u0086~\3\2\2\2\u0087\4\3")
        buf.write("\2\2\2\u0088\u008a\5\3\2\2\u0089\u008b\5\7\4\2\u008a\u0089")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d\3\2\2\2\u008c")
        buf.write("\u008e\5\t\5\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\u0090\b\3\3\2\u0090\6\3\2\2")
        buf.write("\2\u0091\u009d\t\5\2\2\u0092\u009e\t\2\2\2\u0093\u009b")
        buf.write("\t\3\2\2\u0094\u0096\t\6\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write("\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009c\t")
        buf.write("\3\2\2\u009b\u0097\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e")
        buf.write("\3\2\2\2\u009d\u0092\3\2\2\2\u009d\u0093\3\2\2\2\u009e")
        buf.write("\b\3\2\2\2\u009f\u00a1\t\7\2\2\u00a0\u00a2\t\b\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00ab\3\2\2\2")
        buf.write("\u00a3\u00ac\t\2\2\2\u00a4\u00a8\t\3\2\2\u00a5\u00a7\t")
        buf.write("\6\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00ab\u00a3\3\2\2\2\u00ab\u00a4\3\2\2\2")
        buf.write("\u00ac\n\3\2\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7t\2\2")
        buf.write("\u00af\u00b0\7w\2\2\u00b0\u00b7\7g\2\2\u00b1\u00b2\7h")
        buf.write("\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5")
        buf.write("\7u\2\2\u00b5\u00b7\7g\2\2\u00b6\u00ad\3\2\2\2\u00b6\u00b1")
        buf.write("\3\2\2\2\u00b7\f\3\2\2\2\u00b8\u00bc\7$\2\2\u00b9\u00bb")
        buf.write("\5\17\b\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bf\3\2\2\2")
        buf.write("\u00be\u00bc\3\2\2\2\u00bf\u00c0\7$\2\2\u00c0\u00c1\b")
        buf.write("\7\4\2\u00c1\16\3\2\2\2\u00c2\u00c5\n\t\2\2\u00c3\u00c5")
        buf.write("\5\21\t\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("\20\3\2\2\2\u00c6\u00c7\7^\2\2\u00c7\u00c8\t\n\2\2\u00c8")
        buf.write("\22\3\2\2\2\u00c9\u00ca\7]\2\2\u00ca\24\3\2\2\2\u00cb")
        buf.write("\u00cc\7_\2\2\u00cc\26\3\2\2\2\u00cd\u00ce\7*\2\2\u00ce")
        buf.write("\30\3\2\2\2\u00cf\u00d0\7+\2\2\u00d0\32\3\2\2\2\u00d1")
        buf.write("\u00d2\7}\2\2\u00d2\34\3\2\2\2\u00d3\u00d4\7\177\2\2\u00d4")
        buf.write("\36\3\2\2\2\u00d5\u00d6\7\60\2\2\u00d6 \3\2\2\2\u00d7")
        buf.write("\u00d8\7.\2\2\u00d8\"\3\2\2\2\u00d9\u00da\7=\2\2\u00da")
        buf.write("$\3\2\2\2\u00db\u00dc\7<\2\2\u00dc&\3\2\2\2\u00dd\u00de")
        buf.write("\7?\2\2\u00de(\3\2\2\2\u00df\u00e0\7-\2\2\u00e0*\3\2\2")
        buf.write("\2\u00e1\u00e2\7/\2\2\u00e2,\3\2\2\2\u00e3\u00e4\7,\2")
        buf.write("\2\u00e4.\3\2\2\2\u00e5\u00e6\7\61\2\2\u00e6\60\3\2\2")
        buf.write("\2\u00e7\u00e8\7\'\2\2\u00e8\62\3\2\2\2\u00e9\u00ea\7")
        buf.write("#\2\2\u00ea\64\3\2\2\2\u00eb\u00ec\7(\2\2\u00ec\u00ed")
        buf.write("\7(\2\2\u00ed\66\3\2\2\2\u00ee\u00ef\7~\2\2\u00ef\u00f0")
        buf.write("\7~\2\2\u00f08\3\2\2\2\u00f1\u00f2\7?\2\2\u00f2\u00f3")
        buf.write("\7?\2\2\u00f3:\3\2\2\2\u00f4\u00f5\7#\2\2\u00f5\u00f6")
        buf.write("\7?\2\2\u00f6<\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8>\3\2\2")
        buf.write("\2\u00f9\u00fa\7>\2\2\u00fa\u00fb\7?\2\2\u00fb@\3\2\2")
        buf.write("\2\u00fc\u00fd\7@\2\2\u00fdB\3\2\2\2\u00fe\u00ff\7@\2")
        buf.write("\2\u00ff\u0100\7?\2\2\u0100D\3\2\2\2\u0101\u0102\7<\2")
        buf.write("\2\u0102\u0103\7<\2\2\u0103F\3\2\2\2\u0104\u0105\7k\2")
        buf.write("\2\u0105\u0106\7p\2\2\u0106\u0107\7v\2\2\u0107\u0108\7")
        buf.write("g\2\2\u0108\u0109\7i\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7t\2\2\u010bH\3\2\2\2\u010c\u010d\7h\2\2\u010d\u010e")
        buf.write("\7n\2\2\u010e\u010f\7q\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write("\7v\2\2\u0111J\3\2\2\2\u0112\u0113\7d\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114\u0115\7q\2\2\u0115\u0116\7n\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117\u0118\7c\2\2\u0118\u0119\7p\2\2\u0119L\3")
        buf.write("\2\2\2\u011a\u011b\7u\2\2\u011b\u011c\7v\2\2\u011c\u011d")
        buf.write("\7t\2\2\u011d\u011e\7k\2\2\u011e\u011f\7p\2\2\u011f\u0120")
        buf.write("\7i\2\2\u0120N\3\2\2\2\u0121\u0122\7c\2\2\u0122\u0123")
        buf.write("\7t\2\2\u0123\u0124\7t\2\2\u0124\u0125\7c\2\2\u0125\u0126")
        buf.write("\7{\2\2\u0126P\3\2\2\2\u0127\u0128\7q\2\2\u0128\u0129")
        buf.write("\7h\2\2\u0129R\3\2\2\2\u012a\u012b\7x\2\2\u012b\u012c")
        buf.write("\7q\2\2\u012c\u012d\7k\2\2\u012d\u012e\7f\2\2\u012eT\3")
        buf.write("\2\2\2\u012f\u0130\7c\2\2\u0130\u0131\7w\2\2\u0131\u0132")
        buf.write("\7v\2\2\u0132\u0133\7q\2\2\u0133V\3\2\2\2\u0134\u0135")
        buf.write("\7k\2\2\u0135\u0136\7p\2\2\u0136\u0137\7j\2\2\u0137\u0138")
        buf.write("\7k\2\2\u0138\u0139\7t\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7v\2\2\u013bX\3\2\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7w\2\2\u013e\u013f\7v\2\2\u013fZ\3\2\2\2\u0140\u0141")
        buf.write("\7h\2\2\u0141\u0142\7w\2\2\u0142\u0143\7p\2\2\u0143\u0144")
        buf.write("\7e\2\2\u0144\u0145\7v\2\2\u0145\u0146\7k\2\2\u0146\u0147")
        buf.write("\7q\2\2\u0147\u0148\7p\2\2\u0148\\\3\2\2\2\u0149\u014a")
        buf.write("\7k\2\2\u014a\u014b\7h\2\2\u014b^\3\2\2\2\u014c\u014d")
        buf.write("\7g\2\2\u014d\u014e\7n\2\2\u014e\u014f\7u\2\2\u014f\u0150")
        buf.write("\7g\2\2\u0150`\3\2\2\2\u0151\u0152\7h\2\2\u0152\u0153")
        buf.write("\7q\2\2\u0153\u0154\7t\2\2\u0154b\3\2\2\2\u0155\u0156")
        buf.write("\7y\2\2\u0156\u0157\7j\2\2\u0157\u0158\7k\2\2\u0158\u0159")
        buf.write("\7n\2\2\u0159\u015a\7g\2\2\u015ad\3\2\2\2\u015b\u015c")
        buf.write("\7f\2\2\u015c\u015d\7q\2\2\u015df\3\2\2\2\u015e\u015f")
        buf.write("\7d\2\2\u015f\u0160\7t\2\2\u0160\u0161\7g\2\2\u0161\u0162")
        buf.write("\7c\2\2\u0162\u0163\7m\2\2\u0163h\3\2\2\2\u0164\u0165")
        buf.write("\7e\2\2\u0165\u0166\7q\2\2\u0166\u0167\7p\2\2\u0167\u0168")
        buf.write("\7v\2\2\u0168\u0169\7k\2\2\u0169\u016a\7p\2\2\u016a\u016b")
        buf.write("\7w\2\2\u016b\u016c\7g\2\2\u016cj\3\2\2\2\u016d\u016e")
        buf.write("\7t\2\2\u016e\u016f\7g\2\2\u016f\u0170\7v\2\2\u0170\u0171")
        buf.write("\7w\2\2\u0171\u0172\7t\2\2\u0172\u0173\7p\2\2\u0173l\3")
        buf.write("\2\2\2\u0174\u0178\t\13\2\2\u0175\u0177\t\f\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179n\3\2\2\2\u017a\u0178\3\2\2")
        buf.write("\2\u017b\u017c\7\61\2\2\u017c\u017d\7,\2\2\u017d\u0181")
        buf.write("\3\2\2\2\u017e\u0180\n\r\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\7")
        buf.write(",\2\2\u0185\u0186\7\61\2\2\u0186\u0187\3\2\2\2\u0187\u0188")
        buf.write("\b8\5\2\u0188p\3\2\2\2\u0189\u018a\7\61\2\2\u018a\u018b")
        buf.write("\7\61\2\2\u018b\u018f\3\2\2\2\u018c\u018e\n\16\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2")
        buf.write("\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018f\3")
        buf.write("\2\2\2\u0192\u0193\b9\5\2\u0193r\3\2\2\2\u0194\u0196\t")
        buf.write("\17\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019a\b:\5\2\u019at\3\2\2\2\u019b\u019c\13\2\2")
        buf.write("\2\u019c\u019d\b;\6\2\u019dv\3\2\2\2\u019e\u01a2\7$\2")
        buf.write("\2\u019f\u01a1\5\17\b\2\u01a0\u019f\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a5\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6\b<\7\2")
        buf.write("\u01a6x\3\2\2\2\u01a7\u01ab\7$\2\2\u01a8\u01aa\5\17\b")
        buf.write("\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ae\u01af\5{>\2\u01af\u01b0\b=\b\2\u01b0")
        buf.write("z\3\2\2\2\u01b1\u01b2\7^\2\2\u01b2\u01b5\n\20\2\2\u01b3")
        buf.write("\u01b5\n\21\2\2\u01b4\u01b1\3\2\2\2\u01b4\u01b3\3\2\2")
        buf.write("\2\u01b5|\3\2\2\2\27\2\u0082\u0086\u008a\u008d\u0097\u009b")
        buf.write("\u009d\u00a1\u00a8\u00ab\u00b6\u00bc\u00c4\u0178\u0181")
        buf.write("\u018f\u0197\u01a2\u01ab\u01b4\t\3\2\2\3\3\3\3\7\4\b\2")
        buf.write("\2\3;\5\3<\6\3=\7")
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
    BOOLEAN = 33
    STRING = 34
    ARRAY = 35
    OF = 36
    VOID = 37
    AUTO = 38
    INHIRIT = 39
    OUT = 40
    FUNCTION = 41
    IF = 42
    ELSE = 43
    FOR = 44
    WHILE = 45
    DO = 46
    BREAK = 47
    CONT = 48
    RT = 49
    ID = 50
    BLOCK_COMMENT = 51
    LINE_COMMENT = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'('", "')'", "'{'", "'}'", "'.'", "','", "';'", 
            "':'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'integer'", "'float'", "'boolean'", "'string'", "'array'", 
            "'of'", "'void'", "'auto'", "'inhirit'", "'out'", "'function'", 
            "'if'", "'else'", "'for'", "'while'", "'do'", "'break'", "'continue'", 
            "'return'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOL", "STRINGLIT", "LSB", "RSB", "LRB", 
            "RRB", "LCB", "RCB", "DOT", "COMMA", "SEMI", "COLON", "ASSIGN", 
            "ADDOP", "MINUSOP", "MULOP", "DIVOP", "MODOP", "NEGAOP", "CONJOP", 
            "DISJOP", "EQUALOP", "DIFOP", "LESSOP", "LESSEQOP", "GREATOP", 
            "GREATEQOP", "CONCAT", "INTEGER", "FLOAT", "BOOLEAN", "STRING", 
            "ARRAY", "OF", "VOID", "AUTO", "INHIRIT", "OUT", "FUNCTION", 
            "IF", "ELSE", "FOR", "WHILE", "DO", "BREAK", "CONT", "RT", "ID", 
            "BLOCK_COMMENT", "LINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTLIT", "FLOATLIT", "DECIMAL", "EXPONENT", "BOOL", "STRINGLIT", 
                  "STR_CHAR", "ESC_SEQ", "LSB", "RSB", "LRB", "RRB", "LCB", 
                  "RCB", "DOT", "COMMA", "SEMI", "COLON", "ASSIGN", "ADDOP", 
                  "MINUSOP", "MULOP", "DIVOP", "MODOP", "NEGAOP", "CONJOP", 
                  "DISJOP", "EQUALOP", "DIFOP", "LESSOP", "LESSEQOP", "GREATOP", 
                  "GREATEQOP", "CONCAT", "INTEGER", "FLOAT", "BOOLEAN", 
                  "STRING", "ARRAY", "OF", "VOID", "AUTO", "INHIRIT", "OUT", 
                  "FUNCTION", "IF", "ELSE", "FOR", "WHILE", "DO", "BREAK", 
                  "CONT", "RT", "ID", "BLOCK_COMMENT", "LINE_COMMENT", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_ILLEGAL" ]

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
            actions[57] = self.ERROR_CHAR_action 
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
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
            		if not y in '"':
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


