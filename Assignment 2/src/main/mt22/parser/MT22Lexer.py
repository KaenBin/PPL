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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0242\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\7\3\u009a\n\3\f\3\16\3\u009d\13\3\3\3\5\3\u00a0")
        buf.write("\n\3\3\4\3\4\5\4\u00a4\n\4\3\4\5\4\u00a7\n\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\7\5\u00af\n\5\f\5\16\5\u00b2\13\5\3\5\5")
        buf.write("\5\u00b5\n\5\5\5\u00b7\n\5\3\6\3\6\5\6\u00bb\n\6\3\6\3")
        buf.write("\6\3\6\7\6\u00c0\n\6\f\6\16\6\u00c3\13\6\5\6\u00c5\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00d0\n\7\3\b")
        buf.write("\3\b\7\b\u00d4\n\b\f\b\16\b\u00d7\13\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\5\t\u00de\n\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3")
        buf.write("\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\3")
        buf.write("8\38\38\39\39\39\39\39\39\39\39\39\39\39\39\39\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3")
        buf.write("@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\7")
        buf.write("B\u0203\nB\fB\16B\u0206\13B\3C\3C\3C\3C\7C\u020c\nC\f")
        buf.write("C\16C\u020f\13C\3C\3C\3C\3C\3C\3D\3D\3D\3D\7D\u021a\n")
        buf.write("D\fD\16D\u021d\13D\3D\3D\3E\6E\u0222\nE\rE\16E\u0223\3")
        buf.write("E\3E\3F\3F\3F\3G\3G\7G\u022d\nG\fG\16G\u0230\13G\3G\3")
        buf.write("G\3H\3H\7H\u0236\nH\fH\16H\u0239\13H\3H\3H\3H\3I\3I\3")
        buf.write("I\5I\u0241\nI\2\2J\3\3\5\4\7\5\t\2\13\2\r\6\17\7\21\2")
        buf.write("\23\2\25\b\27\t\31\n\33\13\35\f\37\r!\16#\17%\20\'\21")
        buf.write(")\22+\23-\24/\25\61\26\63\27\65\30\67\319\32;\33=\34?")
        buf.write("\35A\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61")
        buf.write("i\62k\63m\64o\65q\66s\67u8w9y:{;}<\177=\u0081>\u0083?")
        buf.write("\u0085@\u0087A\u0089B\u008bC\u008dD\u008fE\u0091\2\3\2")
        buf.write("\22\3\2\62\62\3\2\63;\4\2\62;aa\3\2\60\60\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\4\2\f\f$$\n\2$$))^^ddhhppttvv\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\3\2,,\4\2\f\f\17\17\5\2\n\f\16\17\"\"")
        buf.write("\4\2$$pp\3\2^^\2\u0250\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\3\u0093\3\2\2\2\5\u009f\3\2\2")
        buf.write("\2\7\u00a1\3\2\2\2\t\u00aa\3\2\2\2\13\u00b8\3\2\2\2\r")
        buf.write("\u00cf\3\2\2\2\17\u00d1\3\2\2\2\21\u00dd\3\2\2\2\23\u00df")
        buf.write("\3\2\2\2\25\u00e2\3\2\2\2\27\u00e4\3\2\2\2\31\u00e6\3")
        buf.write("\2\2\2\33\u00e8\3\2\2\2\35\u00ea\3\2\2\2\37\u00ec\3\2")
        buf.write("\2\2!\u00ee\3\2\2\2#\u00f0\3\2\2\2%\u00f2\3\2\2\2\'\u00f4")
        buf.write("\3\2\2\2)\u00f6\3\2\2\2+\u00f8\3\2\2\2-\u00fa\3\2\2\2")
        buf.write("/\u00fc\3\2\2\2\61\u00fe\3\2\2\2\63\u0100\3\2\2\2\65\u0102")
        buf.write("\3\2\2\2\67\u0104\3\2\2\29\u0107\3\2\2\2;\u010a\3\2\2")
        buf.write("\2=\u010d\3\2\2\2?\u0110\3\2\2\2A\u0112\3\2\2\2C\u0115")
        buf.write("\3\2\2\2E\u0117\3\2\2\2G\u011a\3\2\2\2I\u011d\3\2\2\2")
        buf.write("K\u0125\3\2\2\2M\u012b\3\2\2\2O\u0133\3\2\2\2Q\u013a\3")
        buf.write("\2\2\2S\u0140\3\2\2\2U\u0143\3\2\2\2W\u0148\3\2\2\2Y\u014d")
        buf.write("\3\2\2\2[\u0155\3\2\2\2]\u0159\3\2\2\2_\u0162\3\2\2\2")
        buf.write("a\u0165\3\2\2\2c\u016a\3\2\2\2e\u016e\3\2\2\2g\u0174\3")
        buf.write("\2\2\2i\u0177\3\2\2\2k\u017d\3\2\2\2m\u0186\3\2\2\2o\u018d")
        buf.write("\3\2\2\2q\u0199\3\2\2\2s\u01a6\3\2\2\2u\u01b0\3\2\2\2")
        buf.write("w\u01bb\3\2\2\2y\u01c7\3\2\2\2{\u01d4\3\2\2\2}\u01df\3")
        buf.write("\2\2\2\177\u01eb\3\2\2\2\u0081\u01f1\3\2\2\2\u0083\u0200")
        buf.write("\3\2\2\2\u0085\u0207\3\2\2\2\u0087\u0215\3\2\2\2\u0089")
        buf.write("\u0221\3\2\2\2\u008b\u0227\3\2\2\2\u008d\u022a\3\2\2\2")
        buf.write("\u008f\u0233\3\2\2\2\u0091\u0240\3\2\2\2\u0093\u0094\7")
        buf.write("j\2\2\u0094\u0095\7k\2\2\u0095\4\3\2\2\2\u0096\u00a0\t")
        buf.write("\2\2\2\u0097\u009b\t\3\2\2\u0098\u009a\t\4\2\2\u0099\u0098")
        buf.write("\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009e\u00a0\b\3\2\2\u009f\u0096\3\2\2\2\u009f\u0097\3")
        buf.write("\2\2\2\u00a0\6\3\2\2\2\u00a1\u00a3\5\5\3\2\u00a2\u00a4")
        buf.write("\5\t\5\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a6\3\2\2\2\u00a5\u00a7\5\13\6\2\u00a6\u00a5\3\2\2")
        buf.write("\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9")
        buf.write("\b\4\3\2\u00a9\b\3\2\2\2\u00aa\u00b6\t\5\2\2\u00ab\u00b7")
        buf.write("\t\2\2\2\u00ac\u00b4\t\3\2\2\u00ad\u00af\t\6\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b3\u00b5\t\3\2\2\u00b4\u00b0\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00ab\3\2\2\2\u00b6")
        buf.write("\u00ac\3\2\2\2\u00b7\n\3\2\2\2\u00b8\u00ba\t\7\2\2\u00b9")
        buf.write("\u00bb\t\b\2\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00c4\3\2\2\2\u00bc\u00c5\t\2\2\2\u00bd\u00c1\t")
        buf.write("\3\2\2\u00be\u00c0\t\6\2\2\u00bf\u00be\3\2\2\2\u00c0\u00c3")
        buf.write("\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00bc\3\2\2\2")
        buf.write("\u00c4\u00bd\3\2\2\2\u00c5\f\3\2\2\2\u00c6\u00c7\7v\2")
        buf.write("\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7w\2\2\u00c9\u00d0\7")
        buf.write("g\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7u\2\2\u00ce\u00d0\7g\2\2\u00cf\u00c6")
        buf.write("\3\2\2\2\u00cf\u00ca\3\2\2\2\u00d0\16\3\2\2\2\u00d1\u00d5")
        buf.write("\7$\2\2\u00d2\u00d4\5\21\t\2\u00d3\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7")
        buf.write("$\2\2\u00d9\u00da\b\b\4\2\u00da\20\3\2\2\2\u00db\u00de")
        buf.write("\n\t\2\2\u00dc\u00de\5\23\n\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de\22\3\2\2\2\u00df\u00e0\7^\2\2\u00e0")
        buf.write("\u00e1\t\n\2\2\u00e1\24\3\2\2\2\u00e2\u00e3\7]\2\2\u00e3")
        buf.write("\26\3\2\2\2\u00e4\u00e5\7_\2\2\u00e5\30\3\2\2\2\u00e6")
        buf.write("\u00e7\7*\2\2\u00e7\32\3\2\2\2\u00e8\u00e9\7+\2\2\u00e9")
        buf.write("\34\3\2\2\2\u00ea\u00eb\7}\2\2\u00eb\36\3\2\2\2\u00ec")
        buf.write("\u00ed\7\177\2\2\u00ed \3\2\2\2\u00ee\u00ef\7\60\2\2\u00ef")
        buf.write("\"\3\2\2\2\u00f0\u00f1\7.\2\2\u00f1$\3\2\2\2\u00f2\u00f3")
        buf.write("\7=\2\2\u00f3&\3\2\2\2\u00f4\u00f5\7<\2\2\u00f5(\3\2\2")
        buf.write("\2\u00f6\u00f7\7?\2\2\u00f7*\3\2\2\2\u00f8\u00f9\7-\2")
        buf.write("\2\u00f9,\3\2\2\2\u00fa\u00fb\7/\2\2\u00fb.\3\2\2\2\u00fc")
        buf.write("\u00fd\7,\2\2\u00fd\60\3\2\2\2\u00fe\u00ff\7\61\2\2\u00ff")
        buf.write("\62\3\2\2\2\u0100\u0101\7\'\2\2\u0101\64\3\2\2\2\u0102")
        buf.write("\u0103\7#\2\2\u0103\66\3\2\2\2\u0104\u0105\7(\2\2\u0105")
        buf.write("\u0106\7(\2\2\u01068\3\2\2\2\u0107\u0108\7~\2\2\u0108")
        buf.write("\u0109\7~\2\2\u0109:\3\2\2\2\u010a\u010b\7?\2\2\u010b")
        buf.write("\u010c\7?\2\2\u010c<\3\2\2\2\u010d\u010e\7#\2\2\u010e")
        buf.write("\u010f\7?\2\2\u010f>\3\2\2\2\u0110\u0111\7>\2\2\u0111")
        buf.write("@\3\2\2\2\u0112\u0113\7>\2\2\u0113\u0114\7?\2\2\u0114")
        buf.write("B\3\2\2\2\u0115\u0116\7@\2\2\u0116D\3\2\2\2\u0117\u0118")
        buf.write("\7@\2\2\u0118\u0119\7?\2\2\u0119F\3\2\2\2\u011a\u011b")
        buf.write("\7<\2\2\u011b\u011c\7<\2\2\u011cH\3\2\2\2\u011d\u011e")
        buf.write("\7k\2\2\u011e\u011f\7p\2\2\u011f\u0120\7v\2\2\u0120\u0121")
        buf.write("\7g\2\2\u0121\u0122\7i\2\2\u0122\u0123\7g\2\2\u0123\u0124")
        buf.write("\7t\2\2\u0124J\3\2\2\2\u0125\u0126\7h\2\2\u0126\u0127")
        buf.write("\7n\2\2\u0127\u0128\7q\2\2\u0128\u0129\7c\2\2\u0129\u012a")
        buf.write("\7v\2\2\u012aL\3\2\2\2\u012b\u012c\7d\2\2\u012c\u012d")
        buf.write("\7q\2\2\u012d\u012e\7q\2\2\u012e\u012f\7n\2\2\u012f\u0130")
        buf.write("\7g\2\2\u0130\u0131\7c\2\2\u0131\u0132\7p\2\2\u0132N\3")
        buf.write("\2\2\2\u0133\u0134\7u\2\2\u0134\u0135\7v\2\2\u0135\u0136")
        buf.write("\7t\2\2\u0136\u0137\7k\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7i\2\2\u0139P\3\2\2\2\u013a\u013b\7c\2\2\u013b\u013c")
        buf.write("\7t\2\2\u013c\u013d\7t\2\2\u013d\u013e\7c\2\2\u013e\u013f")
        buf.write("\7{\2\2\u013fR\3\2\2\2\u0140\u0141\7q\2\2\u0141\u0142")
        buf.write("\7h\2\2\u0142T\3\2\2\2\u0143\u0144\7x\2\2\u0144\u0145")
        buf.write("\7q\2\2\u0145\u0146\7k\2\2\u0146\u0147\7f\2\2\u0147V\3")
        buf.write("\2\2\2\u0148\u0149\7c\2\2\u0149\u014a\7w\2\2\u014a\u014b")
        buf.write("\7v\2\2\u014b\u014c\7q\2\2\u014cX\3\2\2\2\u014d\u014e")
        buf.write("\7k\2\2\u014e\u014f\7p\2\2\u014f\u0150\7j\2\2\u0150\u0151")
        buf.write("\7k\2\2\u0151\u0152\7t\2\2\u0152\u0153\7k\2\2\u0153\u0154")
        buf.write("\7v\2\2\u0154Z\3\2\2\2\u0155\u0156\7q\2\2\u0156\u0157")
        buf.write("\7w\2\2\u0157\u0158\7v\2\2\u0158\\\3\2\2\2\u0159\u015a")
        buf.write("\7h\2\2\u015a\u015b\7w\2\2\u015b\u015c\7p\2\2\u015c\u015d")
        buf.write("\7e\2\2\u015d\u015e\7v\2\2\u015e\u015f\7k\2\2\u015f\u0160")
        buf.write("\7q\2\2\u0160\u0161\7p\2\2\u0161^\3\2\2\2\u0162\u0163")
        buf.write("\7k\2\2\u0163\u0164\7h\2\2\u0164`\3\2\2\2\u0165\u0166")
        buf.write("\7g\2\2\u0166\u0167\7n\2\2\u0167\u0168\7u\2\2\u0168\u0169")
        buf.write("\7g\2\2\u0169b\3\2\2\2\u016a\u016b\7h\2\2\u016b\u016c")
        buf.write("\7q\2\2\u016c\u016d\7t\2\2\u016dd\3\2\2\2\u016e\u016f")
        buf.write("\7y\2\2\u016f\u0170\7j\2\2\u0170\u0171\7k\2\2\u0171\u0172")
        buf.write("\7n\2\2\u0172\u0173\7g\2\2\u0173f\3\2\2\2\u0174\u0175")
        buf.write("\7f\2\2\u0175\u0176\7q\2\2\u0176h\3\2\2\2\u0177\u0178")
        buf.write("\7d\2\2\u0178\u0179\7t\2\2\u0179\u017a\7g\2\2\u017a\u017b")
        buf.write("\7c\2\2\u017b\u017c\7m\2\2\u017cj\3\2\2\2\u017d\u017e")
        buf.write("\7e\2\2\u017e\u017f\7q\2\2\u017f\u0180\7p\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181\u0182\7k\2\2\u0182\u0183\7p\2\2\u0183\u0184")
        buf.write("\7w\2\2\u0184\u0185\7g\2\2\u0185l\3\2\2\2\u0186\u0187")
        buf.write("\7t\2\2\u0187\u0188\7g\2\2\u0188\u0189\7v\2\2\u0189\u018a")
        buf.write("\7w\2\2\u018a\u018b\7t\2\2\u018b\u018c\7p\2\2\u018cn\3")
        buf.write("\2\2\2\u018d\u018e\7t\2\2\u018e\u018f\7g\2\2\u018f\u0190")
        buf.write("\7c\2\2\u0190\u0191\7f\2\2\u0191\u0192\7K\2\2\u0192\u0193")
        buf.write("\7p\2\2\u0193\u0194\7v\2\2\u0194\u0195\7g\2\2\u0195\u0196")
        buf.write("\7i\2\2\u0196\u0197\7g\2\2\u0197\u0198\7t\2\2\u0198p\3")
        buf.write("\2\2\2\u0199\u019a\7r\2\2\u019a\u019b\7t\2\2\u019b\u019c")
        buf.write("\7k\2\2\u019c\u019d\7p\2\2\u019d\u019e\7v\2\2\u019e\u019f")
        buf.write("\7K\2\2\u019f\u01a0\7p\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2")
        buf.write("\7g\2\2\u01a2\u01a3\7i\2\2\u01a3\u01a4\7g\2\2\u01a4\u01a5")
        buf.write("\7t\2\2\u01a5r\3\2\2\2\u01a6\u01a7\7t\2\2\u01a7\u01a8")
        buf.write("\7g\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa\7f\2\2\u01aa\u01ab")
        buf.write("\7H\2\2\u01ab\u01ac\7n\2\2\u01ac\u01ad\7q\2\2\u01ad\u01ae")
        buf.write("\7c\2\2\u01ae\u01af\7v\2\2\u01aft\3\2\2\2\u01b0\u01b1")
        buf.write("\7y\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3\7k\2\2\u01b3\u01b4")
        buf.write("\7v\2\2\u01b4\u01b5\7g\2\2\u01b5\u01b6\7H\2\2\u01b6\u01b7")
        buf.write("\7n\2\2\u01b7\u01b8\7q\2\2\u01b8\u01b9\7c\2\2\u01b9\u01ba")
        buf.write("\7v\2\2\u01bav\3\2\2\2\u01bb\u01bc\7t\2\2\u01bc\u01bd")
        buf.write("\7g\2\2\u01bd\u01be\7c\2\2\u01be\u01bf\7f\2\2\u01bf\u01c0")
        buf.write("\7D\2\2\u01c0\u01c1\7q\2\2\u01c1\u01c2\7q\2\2\u01c2\u01c3")
        buf.write("\7n\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5\7c\2\2\u01c5\u01c6")
        buf.write("\7p\2\2\u01c6x\3\2\2\2\u01c7\u01c8\7r\2\2\u01c8\u01c9")
        buf.write("\7t\2\2\u01c9\u01ca\7k\2\2\u01ca\u01cb\7p\2\2\u01cb\u01cc")
        buf.write("\7v\2\2\u01cc\u01cd\7D\2\2\u01cd\u01ce\7q\2\2\u01ce\u01cf")
        buf.write("\7q\2\2\u01cf\u01d0\7n\2\2\u01d0\u01d1\7g\2\2\u01d1\u01d2")
        buf.write("\7c\2\2\u01d2\u01d3\7p\2\2\u01d3z\3\2\2\2\u01d4\u01d5")
        buf.write("\7t\2\2\u01d5\u01d6\7g\2\2\u01d6\u01d7\7c\2\2\u01d7\u01d8")
        buf.write("\7f\2\2\u01d8\u01d9\7U\2\2\u01d9\u01da\7v\2\2\u01da\u01db")
        buf.write("\7t\2\2\u01db\u01dc\7k\2\2\u01dc\u01dd\7p\2\2\u01dd\u01de")
        buf.write("\7i\2\2\u01de|\3\2\2\2\u01df\u01e0\7r\2\2\u01e0\u01e1")
        buf.write("\7t\2\2\u01e1\u01e2\7k\2\2\u01e2\u01e3\7p\2\2\u01e3\u01e4")
        buf.write("\7v\2\2\u01e4\u01e5\7U\2\2\u01e5\u01e6\7v\2\2\u01e6\u01e7")
        buf.write("\7t\2\2\u01e7\u01e8\7k\2\2\u01e8\u01e9\7p\2\2\u01e9\u01ea")
        buf.write("\7i\2\2\u01ea~\3\2\2\2\u01eb\u01ec\7u\2\2\u01ec\u01ed")
        buf.write("\7w\2\2\u01ed\u01ee\7r\2\2\u01ee\u01ef\7g\2\2\u01ef\u01f0")
        buf.write("\7t\2\2\u01f0\u0080\3\2\2\2\u01f1\u01f2\7r\2\2\u01f2\u01f3")
        buf.write("\7t\2\2\u01f3\u01f4\7g\2\2\u01f4\u01f5\7x\2\2\u01f5\u01f6")
        buf.write("\7g\2\2\u01f6\u01f7\7p\2\2\u01f7\u01f8\7v\2\2\u01f8\u01f9")
        buf.write("\7F\2\2\u01f9\u01fa\7g\2\2\u01fa\u01fb\7h\2\2\u01fb\u01fc")
        buf.write("\7c\2\2\u01fc\u01fd\7w\2\2\u01fd\u01fe\7n\2\2\u01fe\u01ff")
        buf.write("\7v\2\2\u01ff\u0082\3\2\2\2\u0200\u0204\t\13\2\2\u0201")
        buf.write("\u0203\t\f\2\2\u0202\u0201\3\2\2\2\u0203\u0206\3\2\2\2")
        buf.write("\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0084\3")
        buf.write("\2\2\2\u0206\u0204\3\2\2\2\u0207\u0208\7\61\2\2\u0208")
        buf.write("\u0209\7,\2\2\u0209\u020d\3\2\2\2\u020a\u020c\n\r\2\2")
        buf.write("\u020b\u020a\3\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3")
        buf.write("\2\2\2\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f\u020d")
        buf.write("\3\2\2\2\u0210\u0211\7,\2\2\u0211\u0212\7\61\2\2\u0212")
        buf.write("\u0213\3\2\2\2\u0213\u0214\bC\5\2\u0214\u0086\3\2\2\2")
        buf.write("\u0215\u0216\7\61\2\2\u0216\u0217\7\61\2\2\u0217\u021b")
        buf.write("\3\2\2\2\u0218\u021a\n\16\2\2\u0219\u0218\3\2\2\2\u021a")
        buf.write("\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021c\u021e\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u021f\b")
        buf.write("D\5\2\u021f\u0088\3\2\2\2\u0220\u0222\t\17\2\2\u0221\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0221\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0226\bE\5\2")
        buf.write("\u0226\u008a\3\2\2\2\u0227\u0228\13\2\2\2\u0228\u0229")
        buf.write("\bF\6\2\u0229\u008c\3\2\2\2\u022a\u022e\7$\2\2\u022b\u022d")
        buf.write("\5\21\t\2\u022c\u022b\3\2\2\2\u022d\u0230\3\2\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0231\3\2\2\2")
        buf.write("\u0230\u022e\3\2\2\2\u0231\u0232\bG\7\2\u0232\u008e\3")
        buf.write("\2\2\2\u0233\u0237\7$\2\2\u0234\u0236\5\21\t\2\u0235\u0234")
        buf.write("\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u023a\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u023a\u023b\5\u0091I\2\u023b\u023c\bH\b\2\u023c\u0090")
        buf.write("\3\2\2\2\u023d\u023e\7^\2\2\u023e\u0241\n\20\2\2\u023f")
        buf.write("\u0241\n\21\2\2\u0240\u023d\3\2\2\2\u0240\u023f\3\2\2")
        buf.write("\2\u0241\u0092\3\2\2\2\27\2\u009b\u009f\u00a3\u00a6\u00b0")
        buf.write("\u00b4\u00b6\u00ba\u00c1\u00c4\u00cf\u00d5\u00dd\u0204")
        buf.write("\u020d\u021b\u0223\u022e\u0237\u0240\t\3\3\2\3\4\3\3\b")
        buf.write("\4\b\2\2\3F\5\3G\6\3H\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTLIT = 2
    FLOATLIT = 3
    BOOL = 4
    STRINGLIT = 5
    LSB = 6
    RSB = 7
    LRB = 8
    RRB = 9
    LCB = 10
    RCB = 11
    DOT = 12
    COMMA = 13
    SEMI = 14
    COLON = 15
    ASSIGN = 16
    ADDOP = 17
    MINUSOP = 18
    MULOP = 19
    DIVOP = 20
    MODOP = 21
    NEGAOP = 22
    CONJOP = 23
    DISJOP = 24
    EQUALOP = 25
    DIFOP = 26
    LESSOP = 27
    LESSEQOP = 28
    GREATOP = 29
    GREATEQOP = 30
    CONCAT = 31
    INTEGER = 32
    FLOAT = 33
    BOOLEAN = 34
    STRING = 35
    ARRAY = 36
    OF = 37
    VOID = 38
    AUTO = 39
    INHIRIT = 40
    OUT = 41
    FUNCTION = 42
    IF = 43
    ELSE = 44
    FOR = 45
    WHILE = 46
    DO = 47
    BREAK = 48
    CONT = 49
    RT = 50
    READINT = 51
    PRINTINT = 52
    READFLOAT = 53
    WRITEFLOAT = 54
    READBOOL = 55
    PRINTBOOL = 56
    READSTR = 57
    PRINTSTR = 58
    SUPERS = 59
    PREVENTDEF = 60
    ID = 61
    BLOCK_COMMENT = 62
    LINE_COMMENT = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hi'", "'['", "']'", "'('", "')'", "'{'", "'}'", "'.'", "','", 
            "';'", "':'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'::'", "'integer'", "'float'", "'boolean'", "'string'", "'array'", 
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

    ruleNames = [ "T__0", "INTLIT", "FLOATLIT", "DECIMAL", "EXPONENT", "BOOL", 
                  "STRINGLIT", "STR_CHAR", "ESC_SEQ", "LSB", "RSB", "LRB", 
                  "RRB", "LCB", "RCB", "DOT", "COMMA", "SEMI", "COLON", 
                  "ASSIGN", "ADDOP", "MINUSOP", "MULOP", "DIVOP", "MODOP", 
                  "NEGAOP", "CONJOP", "DISJOP", "EQUALOP", "DIFOP", "LESSOP", 
                  "LESSEQOP", "GREATOP", "GREATEQOP", "CONCAT", "INTEGER", 
                  "FLOAT", "BOOLEAN", "STRING", "ARRAY", "OF", "VOID", "AUTO", 
                  "INHIRIT", "OUT", "FUNCTION", "IF", "ELSE", "FOR", "WHILE", 
                  "DO", "BREAK", "CONT", "RT", "READINT", "PRINTINT", "READFLOAT", 
                  "WRITEFLOAT", "READBOOL", "PRINTBOOL", "READSTR", "PRINTSTR", 
                  "SUPERS", "PREVENTDEF", "ID", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ESC_ILLEGAL" ]

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
            actions[1] = self.INTLIT_action 
            actions[2] = self.FLOATLIT_action 
            actions[6] = self.STRINGLIT_action 
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
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
            	
     


