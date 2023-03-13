# Generated from d:\University\2022-2023\Semester 2\Principle of Programming Language\Assignment\Assignment 2\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u023d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\7\2\u0095")
        buf.write("\n\2\f\2\16\2\u0098\13\2\3\2\5\2\u009b\n\2\3\3\3\3\5\3")
        buf.write("\u009f\n\3\3\3\5\3\u00a2\n\3\3\3\3\3\3\4\3\4\3\4\3\4\7")
        buf.write("\4\u00aa\n\4\f\4\16\4\u00ad\13\4\3\4\5\4\u00b0\n\4\5\4")
        buf.write("\u00b2\n\4\3\5\3\5\5\5\u00b6\n\5\3\5\3\5\3\5\7\5\u00bb")
        buf.write("\n\5\f\5\16\5\u00be\13\5\5\5\u00c0\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6\u00cb\n\6\3\7\3\7\7\7\u00cf\n")
        buf.write("\7\f\7\16\7\u00d2\13\7\3\7\3\7\3\7\3\b\3\b\5\b\u00d9\n")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\38\38\38\38\38\38\38\38\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3")
        buf.write("?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3A\3")
        buf.write("A\7A\u01fe\nA\fA\16A\u0201\13A\3B\3B\3B\3B\7B\u0207\n")
        buf.write("B\fB\16B\u020a\13B\3B\3B\3B\3B\3B\3C\3C\3C\3C\7C\u0215")
        buf.write("\nC\fC\16C\u0218\13C\3C\3C\3D\6D\u021d\nD\rD\16D\u021e")
        buf.write("\3D\3D\3E\3E\3E\3F\3F\7F\u0228\nF\fF\16F\u022b\13F\3F")
        buf.write("\3F\3G\3G\7G\u0231\nG\fG\16G\u0234\13G\3G\3G\3G\3H\3H")
        buf.write("\3H\5H\u023c\nH\2\2I\3\3\5\4\7\2\t\2\13\5\r\6\17\2\21")
        buf.write("\2\23\7\25\b\27\t\31\n\33\13\35\f\37\r!\16#\17%\20\'\21")
        buf.write(")\22+\23-\24/\25\61\26\63\27\65\30\67\319\32;\33=\34?")
        buf.write("\35A\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61")
        buf.write("i\62k\63m\64o\65q\66s\67u8w9y:{;}<\177=\u0081>\u0083?")
        buf.write("\u0085@\u0087A\u0089B\u008bC\u008dD\u008f\2\3\2\22\3\2")
        buf.write("\62\62\3\2\63;\4\2\62;aa\3\2\60\60\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\4\2\f\f$$\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\3\2,,\4\2\f\f\17\17\5\2\n\f\16\17\"\"\4\2$$pp")
        buf.write("\3\2^^\2\u024b\2\3\3\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u009a\3\2\2\2\5\u009c\3\2\2\2\7\u00a5\3\2\2\2\t\u00b3")
        buf.write("\3\2\2\2\13\u00ca\3\2\2\2\r\u00cc\3\2\2\2\17\u00d8\3\2")
        buf.write("\2\2\21\u00da\3\2\2\2\23\u00dd\3\2\2\2\25\u00df\3\2\2")
        buf.write("\2\27\u00e1\3\2\2\2\31\u00e3\3\2\2\2\33\u00e5\3\2\2\2")
        buf.write("\35\u00e7\3\2\2\2\37\u00e9\3\2\2\2!\u00eb\3\2\2\2#\u00ed")
        buf.write("\3\2\2\2%\u00ef\3\2\2\2\'\u00f1\3\2\2\2)\u00f3\3\2\2\2")
        buf.write("+\u00f5\3\2\2\2-\u00f7\3\2\2\2/\u00f9\3\2\2\2\61\u00fb")
        buf.write("\3\2\2\2\63\u00fd\3\2\2\2\65\u00ff\3\2\2\2\67\u0102\3")
        buf.write("\2\2\29\u0105\3\2\2\2;\u0108\3\2\2\2=\u010b\3\2\2\2?\u010d")
        buf.write("\3\2\2\2A\u0110\3\2\2\2C\u0112\3\2\2\2E\u0115\3\2\2\2")
        buf.write("G\u0118\3\2\2\2I\u0120\3\2\2\2K\u0126\3\2\2\2M\u012e\3")
        buf.write("\2\2\2O\u0135\3\2\2\2Q\u013b\3\2\2\2S\u013e\3\2\2\2U\u0143")
        buf.write("\3\2\2\2W\u0148\3\2\2\2Y\u0150\3\2\2\2[\u0154\3\2\2\2")
        buf.write("]\u015d\3\2\2\2_\u0160\3\2\2\2a\u0165\3\2\2\2c\u0169\3")
        buf.write("\2\2\2e\u016f\3\2\2\2g\u0172\3\2\2\2i\u0178\3\2\2\2k\u0181")
        buf.write("\3\2\2\2m\u0188\3\2\2\2o\u0194\3\2\2\2q\u01a1\3\2\2\2")
        buf.write("s\u01ab\3\2\2\2u\u01b6\3\2\2\2w\u01c2\3\2\2\2y\u01cf\3")
        buf.write("\2\2\2{\u01da\3\2\2\2}\u01e6\3\2\2\2\177\u01ec\3\2\2\2")
        buf.write("\u0081\u01fb\3\2\2\2\u0083\u0202\3\2\2\2\u0085\u0210\3")
        buf.write("\2\2\2\u0087\u021c\3\2\2\2\u0089\u0222\3\2\2\2\u008b\u0225")
        buf.write("\3\2\2\2\u008d\u022e\3\2\2\2\u008f\u023b\3\2\2\2\u0091")
        buf.write("\u009b\t\2\2\2\u0092\u0096\t\3\2\2\u0093\u0095\t\4\2\2")
        buf.write("\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u0096")
        buf.write("\3\2\2\2\u0099\u009b\b\2\2\2\u009a\u0091\3\2\2\2\u009a")
        buf.write("\u0092\3\2\2\2\u009b\4\3\2\2\2\u009c\u009e\5\3\2\2\u009d")
        buf.write("\u009f\5\7\4\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a1\3\2\2\2\u00a0\u00a2\5\t\5\2\u00a1\u00a0\3")
        buf.write("\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4")
        buf.write("\b\3\3\2\u00a4\6\3\2\2\2\u00a5\u00b1\t\5\2\2\u00a6\u00b2")
        buf.write("\t\2\2\2\u00a7\u00af\t\3\2\2\u00a8\u00aa\t\6\2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3")
        buf.write("\2\2\2\u00ae\u00b0\t\3\2\2\u00af\u00ab\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00a6\3\2\2\2\u00b1")
        buf.write("\u00a7\3\2\2\2\u00b2\b\3\2\2\2\u00b3\u00b5\t\7\2\2\u00b4")
        buf.write("\u00b6\t\b\2\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00bf\3\2\2\2\u00b7\u00c0\t\2\2\2\u00b8\u00bc\t")
        buf.write("\3\2\2\u00b9\u00bb\t\6\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be")
        buf.write("\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00b7\3\2\2\2")
        buf.write("\u00bf\u00b8\3\2\2\2\u00c0\n\3\2\2\2\u00c1\u00c2\7v\2")
        buf.write("\2\u00c2\u00c3\7t\2\2\u00c3\u00c4\7w\2\2\u00c4\u00cb\7")
        buf.write("g\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00cb\7g\2\2\u00ca\u00c1")
        buf.write("\3\2\2\2\u00ca\u00c5\3\2\2\2\u00cb\f\3\2\2\2\u00cc\u00d0")
        buf.write("\7$\2\2\u00cd\u00cf\5\17\b\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\7")
        buf.write("$\2\2\u00d4\u00d5\b\7\4\2\u00d5\16\3\2\2\2\u00d6\u00d9")
        buf.write("\n\t\2\2\u00d7\u00d9\5\21\t\2\u00d8\u00d6\3\2\2\2\u00d8")
        buf.write("\u00d7\3\2\2\2\u00d9\20\3\2\2\2\u00da\u00db\7^\2\2\u00db")
        buf.write("\u00dc\t\n\2\2\u00dc\22\3\2\2\2\u00dd\u00de\7]\2\2\u00de")
        buf.write("\24\3\2\2\2\u00df\u00e0\7_\2\2\u00e0\26\3\2\2\2\u00e1")
        buf.write("\u00e2\7*\2\2\u00e2\30\3\2\2\2\u00e3\u00e4\7+\2\2\u00e4")
        buf.write("\32\3\2\2\2\u00e5\u00e6\7}\2\2\u00e6\34\3\2\2\2\u00e7")
        buf.write("\u00e8\7\177\2\2\u00e8\36\3\2\2\2\u00e9\u00ea\7\60\2\2")
        buf.write("\u00ea \3\2\2\2\u00eb\u00ec\7.\2\2\u00ec\"\3\2\2\2\u00ed")
        buf.write("\u00ee\7=\2\2\u00ee$\3\2\2\2\u00ef\u00f0\7<\2\2\u00f0")
        buf.write("&\3\2\2\2\u00f1\u00f2\7?\2\2\u00f2(\3\2\2\2\u00f3\u00f4")
        buf.write("\7-\2\2\u00f4*\3\2\2\2\u00f5\u00f6\7/\2\2\u00f6,\3\2\2")
        buf.write("\2\u00f7\u00f8\7,\2\2\u00f8.\3\2\2\2\u00f9\u00fa\7\61")
        buf.write("\2\2\u00fa\60\3\2\2\2\u00fb\u00fc\7\'\2\2\u00fc\62\3\2")
        buf.write("\2\2\u00fd\u00fe\7#\2\2\u00fe\64\3\2\2\2\u00ff\u0100\7")
        buf.write("(\2\2\u0100\u0101\7(\2\2\u0101\66\3\2\2\2\u0102\u0103")
        buf.write("\7~\2\2\u0103\u0104\7~\2\2\u01048\3\2\2\2\u0105\u0106")
        buf.write("\7?\2\2\u0106\u0107\7?\2\2\u0107:\3\2\2\2\u0108\u0109")
        buf.write("\7#\2\2\u0109\u010a\7?\2\2\u010a<\3\2\2\2\u010b\u010c")
        buf.write("\7>\2\2\u010c>\3\2\2\2\u010d\u010e\7>\2\2\u010e\u010f")
        buf.write("\7?\2\2\u010f@\3\2\2\2\u0110\u0111\7@\2\2\u0111B\3\2\2")
        buf.write("\2\u0112\u0113\7@\2\2\u0113\u0114\7?\2\2\u0114D\3\2\2")
        buf.write("\2\u0115\u0116\7<\2\2\u0116\u0117\7<\2\2\u0117F\3\2\2")
        buf.write("\2\u0118\u0119\7k\2\2\u0119\u011a\7p\2\2\u011a\u011b\7")
        buf.write("v\2\2\u011b\u011c\7g\2\2\u011c\u011d\7i\2\2\u011d\u011e")
        buf.write("\7g\2\2\u011e\u011f\7t\2\2\u011fH\3\2\2\2\u0120\u0121")
        buf.write("\7h\2\2\u0121\u0122\7n\2\2\u0122\u0123\7q\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7v\2\2\u0125J\3\2\2\2\u0126\u0127")
        buf.write("\7d\2\2\u0127\u0128\7q\2\2\u0128\u0129\7q\2\2\u0129\u012a")
        buf.write("\7n\2\2\u012a\u012b\7g\2\2\u012b\u012c\7c\2\2\u012c\u012d")
        buf.write("\7p\2\2\u012dL\3\2\2\2\u012e\u012f\7u\2\2\u012f\u0130")
        buf.write("\7v\2\2\u0130\u0131\7t\2\2\u0131\u0132\7k\2\2\u0132\u0133")
        buf.write("\7p\2\2\u0133\u0134\7i\2\2\u0134N\3\2\2\2\u0135\u0136")
        buf.write("\7c\2\2\u0136\u0137\7t\2\2\u0137\u0138\7t\2\2\u0138\u0139")
        buf.write("\7c\2\2\u0139\u013a\7{\2\2\u013aP\3\2\2\2\u013b\u013c")
        buf.write("\7q\2\2\u013c\u013d\7h\2\2\u013dR\3\2\2\2\u013e\u013f")
        buf.write("\7x\2\2\u013f\u0140\7q\2\2\u0140\u0141\7k\2\2\u0141\u0142")
        buf.write("\7f\2\2\u0142T\3\2\2\2\u0143\u0144\7c\2\2\u0144\u0145")
        buf.write("\7w\2\2\u0145\u0146\7v\2\2\u0146\u0147\7q\2\2\u0147V\3")
        buf.write("\2\2\2\u0148\u0149\7k\2\2\u0149\u014a\7p\2\2\u014a\u014b")
        buf.write("\7j\2\2\u014b\u014c\7k\2\2\u014c\u014d\7t\2\2\u014d\u014e")
        buf.write("\7k\2\2\u014e\u014f\7v\2\2\u014fX\3\2\2\2\u0150\u0151")
        buf.write("\7q\2\2\u0151\u0152\7w\2\2\u0152\u0153\7v\2\2\u0153Z\3")
        buf.write("\2\2\2\u0154\u0155\7h\2\2\u0155\u0156\7w\2\2\u0156\u0157")
        buf.write("\7p\2\2\u0157\u0158\7e\2\2\u0158\u0159\7v\2\2\u0159\u015a")
        buf.write("\7k\2\2\u015a\u015b\7q\2\2\u015b\u015c\7p\2\2\u015c\\")
        buf.write("\3\2\2\2\u015d\u015e\7k\2\2\u015e\u015f\7h\2\2\u015f^")
        buf.write("\3\2\2\2\u0160\u0161\7g\2\2\u0161\u0162\7n\2\2\u0162\u0163")
        buf.write("\7u\2\2\u0163\u0164\7g\2\2\u0164`\3\2\2\2\u0165\u0166")
        buf.write("\7h\2\2\u0166\u0167\7q\2\2\u0167\u0168\7t\2\2\u0168b\3")
        buf.write("\2\2\2\u0169\u016a\7y\2\2\u016a\u016b\7j\2\2\u016b\u016c")
        buf.write("\7k\2\2\u016c\u016d\7n\2\2\u016d\u016e\7g\2\2\u016ed\3")
        buf.write("\2\2\2\u016f\u0170\7f\2\2\u0170\u0171\7q\2\2\u0171f\3")
        buf.write("\2\2\2\u0172\u0173\7d\2\2\u0173\u0174\7t\2\2\u0174\u0175")
        buf.write("\7g\2\2\u0175\u0176\7c\2\2\u0176\u0177\7m\2\2\u0177h\3")
        buf.write("\2\2\2\u0178\u0179\7e\2\2\u0179\u017a\7q\2\2\u017a\u017b")
        buf.write("\7p\2\2\u017b\u017c\7v\2\2\u017c\u017d\7k\2\2\u017d\u017e")
        buf.write("\7p\2\2\u017e\u017f\7w\2\2\u017f\u0180\7g\2\2\u0180j\3")
        buf.write("\2\2\2\u0181\u0182\7t\2\2\u0182\u0183\7g\2\2\u0183\u0184")
        buf.write("\7v\2\2\u0184\u0185\7w\2\2\u0185\u0186\7t\2\2\u0186\u0187")
        buf.write("\7p\2\2\u0187l\3\2\2\2\u0188\u0189\7t\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7c\2\2\u018b\u018c\7f\2\2\u018c\u018d")
        buf.write("\7K\2\2\u018d\u018e\7p\2\2\u018e\u018f\7v\2\2\u018f\u0190")
        buf.write("\7g\2\2\u0190\u0191\7i\2\2\u0191\u0192\7g\2\2\u0192\u0193")
        buf.write("\7t\2\2\u0193n\3\2\2\2\u0194\u0195\7r\2\2\u0195\u0196")
        buf.write("\7t\2\2\u0196\u0197\7k\2\2\u0197\u0198\7p\2\2\u0198\u0199")
        buf.write("\7v\2\2\u0199\u019a\7K\2\2\u019a\u019b\7p\2\2\u019b\u019c")
        buf.write("\7v\2\2\u019c\u019d\7g\2\2\u019d\u019e\7i\2\2\u019e\u019f")
        buf.write("\7g\2\2\u019f\u01a0\7t\2\2\u01a0p\3\2\2\2\u01a1\u01a2")
        buf.write("\7t\2\2\u01a2\u01a3\7g\2\2\u01a3\u01a4\7c\2\2\u01a4\u01a5")
        buf.write("\7f\2\2\u01a5\u01a6\7H\2\2\u01a6\u01a7\7n\2\2\u01a7\u01a8")
        buf.write("\7q\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa\7v\2\2\u01aar\3")
        buf.write("\2\2\2\u01ab\u01ac\7y\2\2\u01ac\u01ad\7t\2\2\u01ad\u01ae")
        buf.write("\7k\2\2\u01ae\u01af\7v\2\2\u01af\u01b0\7g\2\2\u01b0\u01b1")
        buf.write("\7H\2\2\u01b1\u01b2\7n\2\2\u01b2\u01b3\7q\2\2\u01b3\u01b4")
        buf.write("\7c\2\2\u01b4\u01b5\7v\2\2\u01b5t\3\2\2\2\u01b6\u01b7")
        buf.write("\7t\2\2\u01b7\u01b8\7g\2\2\u01b8\u01b9\7c\2\2\u01b9\u01ba")
        buf.write("\7f\2\2\u01ba\u01bb\7D\2\2\u01bb\u01bc\7q\2\2\u01bc\u01bd")
        buf.write("\7q\2\2\u01bd\u01be\7n\2\2\u01be\u01bf\7g\2\2\u01bf\u01c0")
        buf.write("\7c\2\2\u01c0\u01c1\7p\2\2\u01c1v\3\2\2\2\u01c2\u01c3")
        buf.write("\7r\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5\7k\2\2\u01c5\u01c6")
        buf.write("\7p\2\2\u01c6\u01c7\7v\2\2\u01c7\u01c8\7D\2\2\u01c8\u01c9")
        buf.write("\7q\2\2\u01c9\u01ca\7q\2\2\u01ca\u01cb\7n\2\2\u01cb\u01cc")
        buf.write("\7g\2\2\u01cc\u01cd\7c\2\2\u01cd\u01ce\7p\2\2\u01cex\3")
        buf.write("\2\2\2\u01cf\u01d0\7t\2\2\u01d0\u01d1\7g\2\2\u01d1\u01d2")
        buf.write("\7c\2\2\u01d2\u01d3\7f\2\2\u01d3\u01d4\7U\2\2\u01d4\u01d5")
        buf.write("\7v\2\2\u01d5\u01d6\7t\2\2\u01d6\u01d7\7k\2\2\u01d7\u01d8")
        buf.write("\7p\2\2\u01d8\u01d9\7i\2\2\u01d9z\3\2\2\2\u01da\u01db")
        buf.write("\7r\2\2\u01db\u01dc\7t\2\2\u01dc\u01dd\7k\2\2\u01dd\u01de")
        buf.write("\7p\2\2\u01de\u01df\7v\2\2\u01df\u01e0\7U\2\2\u01e0\u01e1")
        buf.write("\7v\2\2\u01e1\u01e2\7t\2\2\u01e2\u01e3\7k\2\2\u01e3\u01e4")
        buf.write("\7p\2\2\u01e4\u01e5\7i\2\2\u01e5|\3\2\2\2\u01e6\u01e7")
        buf.write("\7u\2\2\u01e7\u01e8\7w\2\2\u01e8\u01e9\7r\2\2\u01e9\u01ea")
        buf.write("\7g\2\2\u01ea\u01eb\7t\2\2\u01eb~\3\2\2\2\u01ec\u01ed")
        buf.write("\7r\2\2\u01ed\u01ee\7t\2\2\u01ee\u01ef\7g\2\2\u01ef\u01f0")
        buf.write("\7x\2\2\u01f0\u01f1\7g\2\2\u01f1\u01f2\7p\2\2\u01f2\u01f3")
        buf.write("\7v\2\2\u01f3\u01f4\7F\2\2\u01f4\u01f5\7g\2\2\u01f5\u01f6")
        buf.write("\7h\2\2\u01f6\u01f7\7c\2\2\u01f7\u01f8\7w\2\2\u01f8\u01f9")
        buf.write("\7n\2\2\u01f9\u01fa\7v\2\2\u01fa\u0080\3\2\2\2\u01fb\u01ff")
        buf.write("\t\13\2\2\u01fc\u01fe\t\f\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write("\u0200\u0082\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0203\7")
        buf.write("\61\2\2\u0203\u0204\7,\2\2\u0204\u0208\3\2\2\2\u0205\u0207")
        buf.write("\n\r\2\2\u0206\u0205\3\2\2\2\u0207\u020a\3\2\2\2\u0208")
        buf.write("\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020b\3\2\2\2")
        buf.write("\u020a\u0208\3\2\2\2\u020b\u020c\7,\2\2\u020c\u020d\7")
        buf.write("\61\2\2\u020d\u020e\3\2\2\2\u020e\u020f\bB\5\2\u020f\u0084")
        buf.write("\3\2\2\2\u0210\u0211\7\61\2\2\u0211\u0212\7\61\2\2\u0212")
        buf.write("\u0216\3\2\2\2\u0213\u0215\n\16\2\2\u0214\u0213\3\2\2")
        buf.write("\2\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u0216\3\2\2\2\u0219")
        buf.write("\u021a\bC\5\2\u021a\u0086\3\2\2\2\u021b\u021d\t\17\2\2")
        buf.write("\u021c\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021c\3")
        buf.write("\2\2\2\u021e\u021f\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0221")
        buf.write("\bD\5\2\u0221\u0088\3\2\2\2\u0222\u0223\13\2\2\2\u0223")
        buf.write("\u0224\bE\6\2\u0224\u008a\3\2\2\2\u0225\u0229\7$\2\2\u0226")
        buf.write("\u0228\5\17\b\2\u0227\u0226\3\2\2\2\u0228\u022b\3\2\2")
        buf.write("\2\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022c")
        buf.write("\3\2\2\2\u022b\u0229\3\2\2\2\u022c\u022d\bF\7\2\u022d")
        buf.write("\u008c\3\2\2\2\u022e\u0232\7$\2\2\u022f\u0231\5\17\b\2")
        buf.write("\u0230\u022f\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0232\u0233\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0232")
        buf.write("\3\2\2\2\u0235\u0236\5\u008fH\2\u0236\u0237\bG\b\2\u0237")
        buf.write("\u008e\3\2\2\2\u0238\u0239\7^\2\2\u0239\u023c\n\20\2\2")
        buf.write("\u023a\u023c\n\21\2\2\u023b\u0238\3\2\2\2\u023b\u023a")
        buf.write("\3\2\2\2\u023c\u0090\3\2\2\2\27\2\u0096\u009a\u009e\u00a1")
        buf.write("\u00ab\u00af\u00b1\u00b5\u00bc\u00bf\u00ca\u00d0\u00d8")
        buf.write("\u01ff\u0208\u0216\u021e\u0229\u0232\u023b\t\3\2\2\3\3")
        buf.write("\3\3\7\4\b\2\2\3E\5\3F\6\3G\7")
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
    READINT = 50
    PRINTINT = 51
    READFLOAT = 52
    WRITEFLOAT = 53
    READBOOL = 54
    PRINTBOOL = 55
    READSTR = 56
    PRINTSTR = 57
    SUPERS = 58
    PREVENTDEF = 59
    ID = 60
    BLOCK_COMMENT = 61
    LINE_COMMENT = 62
    WS = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'('", "')'", "'{'", "'}'", "'.'", "','", "';'", 
            "':'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'integer'", "'float'", "'boolean'", "'string'", "'array'", 
            "'of'", "'void'", "'auto'", "'inhirit'", "'out'", "'function'", 
            "'if'", "'else'", "'for'", "'while'", "'do'", "'break'", "'continue'", 
            "'return'", "'readInteger'", "'printInteger'", "'readFloat'", 
            "'writeFloat'", "'readBoolean'", "'printBoolean'", "'readString'", 
            "'printString'", "'super'", "'preventDefault'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOL", "STRINGLIT", "LSB", "RSB", "LRB", 
            "RRB", "LCB", "RCB", "DOT", "COMMA", "SEMI", "COLON", "ASSIGN", 
            "ADDOP", "MINUSOP", "MULOP", "DIVOP", "MODOP", "NEGAOP", "CONJOP", 
            "DISJOP", "EQUALOP", "DIFOP", "LESSOP", "LESSEQOP", "GREATOP", 
            "GREATEQOP", "CONCAT", "INTEGER", "FLOAT", "BOOLEAN", "STRING", 
            "ARRAY", "OF", "VOID", "AUTO", "INHIRIT", "OUT", "FUNCTION", 
            "IF", "ELSE", "FOR", "WHILE", "DO", "BREAK", "CONT", "RT", "READINT", 
            "PRINTINT", "READFLOAT", "WRITEFLOAT", "READBOOL", "PRINTBOOL", 
            "READSTR", "PRINTSTR", "SUPERS", "PREVENTDEF", "ID", "BLOCK_COMMENT", 
            "LINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTLIT", "FLOATLIT", "DECIMAL", "EXPONENT", "BOOL", "STRINGLIT", 
                  "STR_CHAR", "ESC_SEQ", "LSB", "RSB", "LRB", "RRB", "LCB", 
                  "RCB", "DOT", "COMMA", "SEMI", "COLON", "ASSIGN", "ADDOP", 
                  "MINUSOP", "MULOP", "DIVOP", "MODOP", "NEGAOP", "CONJOP", 
                  "DISJOP", "EQUALOP", "DIFOP", "LESSOP", "LESSEQOP", "GREATOP", 
                  "GREATEQOP", "CONCAT", "INTEGER", "FLOAT", "BOOLEAN", 
                  "STRING", "ARRAY", "OF", "VOID", "AUTO", "INHIRIT", "OUT", 
                  "FUNCTION", "IF", "ELSE", "FOR", "WHILE", "DO", "BREAK", 
                  "CONT", "RT", "READINT", "PRINTINT", "READFLOAT", "WRITEFLOAT", 
                  "READBOOL", "PRINTBOOL", "READSTR", "PRINTSTR", "SUPERS", 
                  "PREVENTDEF", "ID", "BLOCK_COMMENT", "LINE_COMMENT", "WS", 
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
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
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
            	
     


