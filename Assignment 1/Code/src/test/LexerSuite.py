import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    
    # bkel_test_cases
    def test_bkel_testcases1(self):
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 102))
    def test_bkel_testcases2(self):    
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 103))
    def test_bkel_testcases3(self):
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 104))
    def test_bkel_testcases4(self):
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """, "He asked me: \\\"Where is John?\\\",<EOF>", 105))

    # identifiers
    def test_identifiers1(self):
        self.assertTrue(TestLexer.test("Vmjm03xvEg", "Vmjm03xvEg,<EOF>", 106))
    def test_identifiers2(self):
        self.assertTrue(TestLexer.test("7WcqYuCR0c", "7,WcqYuCR0c,<EOF>", 107))
    def test_identifiers3(self):
        self.assertTrue(TestLexer.test("yaRtCMRHjP", "yaRtCMRHjP,<EOF>", 108))
    def test_identifiers4(self):
        self.assertTrue(TestLexer.test("_4Ct9omkL7c", "_4Ct9omkL7c,<EOF>", 109))

    def test_characters_set1(self):
        self.assertTrue(TestLexer.test("Characters_Set\t\b\f\r\n ", "Characters_Set,<EOF>", 110))
    def test_characters_set2(self):
        self.assertTrue(TestLexer.test("\t\b\f\r\n Characters_Set", "Characters_Set,<EOF>", 111))
    def test_characters_set3(self):    
        self.assertTrue(TestLexer.test("Characters\t\b\f\r\n _Set", "Characters,_Set,<EOF>", 112))

    def test_comments1(self):
        self.assertTrue(TestLexer.test(" /* A C-style comment */ ", "<EOF>", 113))
    def test_comments2(self):
        self.assertTrue(TestLexer.test("abcDeF // A C++ style comment", "abcDeF,<EOF>", 114))

    def test_key_words(self):
        self.assertTrue(TestLexer.test("auto break boolean do else false float for function if integer return string true while void out continue of inherit array",
                                       "auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>", 115))
        
    def test_operators1(self):
        self.assertTrue(TestLexer.test("+ - * / % ! && || == != < <= > >= ::",
                                       "+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>", 116))
        
    def test_seperators1(self):
        self.assertTrue(TestLexer.test("( ) [ ] . , ; : { } =",
                                       "(,),[,],.,,,;,:,{,},=,<EOF>", 117))
        
    def test_integers1(self):
        self.assertTrue(TestLexer.test("1234", "1234,<EOF>", 118))
    def test_integers2(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 119))
    def test_integers3(self):
        self.assertTrue(TestLexer.test("1_72/*considered as 172 by scanner*/", "172,<EOF>", 120))
    def test_integers4(self):
        self.assertTrue(TestLexer.test("1_234_567 // considered as 1234567 by scanner", "1234567,<EOF>", 121))

    def test_float1(self):
        self.assertTrue(TestLexer.test("1.234", "1.234,<EOF>", 122))
    def test_float2(self):
        self.assertTrue(TestLexer.test("1.2e3", "1.2e3,<EOF>", 123))
    def test_float3(self):
        self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 124))
    def test_float4(self):
        self.assertTrue(TestLexer.test("1_234.567//considered as 1234.567 by scanner", "1234.567,<EOF>", 125))

    def test_string1(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t" """, "This is a string containing tab \\t,<EOF>", 126))
    def test_string2(self):    
        self.assertTrue(TestLexer.test(""" "This is an Unclosed string """, "Unclosed String: This is an Unclosed string ", 127))
    def test_string3(self):
        self.assertTrue(TestLexer.test(""" "Closed string" "Unclosed string """, "Closed string,Unclosed String: Unclosed string ", 128))
    def test_string4(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing illegal escape\n" """, """Illegal Escape In String: This is a string containing illegal escape\n\n""", 129))
    def test_string5(self):
        self.assertTrue(TestLexer.test(""" "All supported escape sequences: \\b \\f \\r \\n \\t \\' \\\\ \\\"" """, "All supported escape sequences: \\b \\f \\r \\n \\t \\' \\\\ \\\",<EOF>", 130))
    def test_string6(self):
        self.assertTrue(TestLexer.test(""" "Some non-error escapse sequences:\b \f \t \' \\ " """, "Some non-error escapse sequences:\b \f \t \' \\ ,<EOF>", 131))
    def test_string7(self):
        self.assertTrue(TestLexer.test(""" "First string" "Second string" """, "First string,Second string,<EOF>", 132))

    # test errors:
    def test_integer5(self):
        self.assertTrue(TestLexer.test("0_", "0,_,<EOF>", 133))
    def test_integer6(self):
        self.assertTrue(TestLexer.test("012_345", "0,12345,<EOF>", 134))
    def test_integer7(self):
        self.assertTrue(TestLexer.test("0_32453__345", "0,_32453__345,<EOF>", 135))
    def test_integer8(self):
        self.assertTrue(TestLexer.test("019__82_37", "0,198237,<EOF>", 136))
    def test_integer9(self):
        self.assertTrue(TestLexer.test("08-33-51-59-63", "0,8,-,33,-,51,-,59,-,63,<EOF>", 137))
    def test_integer10(self):
        self.assertTrue(TestLexer.test("1_________", "1,<EOF>", 138))

    def test_float5(self):
        self.assertTrue(TestLexer.test("213.", "213,.,<EOF>", 139))
    def test_float6(self):
        self.assertTrue(TestLexer.test(".18389", ".,18389,<EOF>", 140))
    def test_float7(self):
        self.assertTrue(TestLexer.test("12397E", "12397,E,<EOF>", 141))
    def test_float8(self):
        self.assertTrue(TestLexer.test("1203.130", "1203.13,0,<EOF>", 142))
    def test_float9(self):
        self.assertTrue(TestLexer.test("101980.E10", "101980,.,E10,<EOF>", 143))
    def test_float10(self):
        self.assertTrue(TestLexer.test("0809.10E2", "0,809.1,0E2,<EOF>", 144))
    def test_float11(self):
        self.assertTrue(TestLexer.test("12830.", "12830,.,<EOF>", 145))
    def test_float12(self):
        self.assertTrue(TestLexer.test("79843.23e", "79843.23,e,<EOF>", 146))
    def test_float13(self):
        self.assertTrue(TestLexer.test(".23e+320", ".,23e+320,<EOF>", 147))

    def test_operators2(self):
        self.assertTrue(TestLexer.test("asdgrw+ewqe", "asdgrw,+,ewqe,<EOF>", 148))
    def test_operators3(self):
        self.assertTrue(TestLexer.test("=====", "==,==,=,<EOF>", 149))
    def test_operators4(self):
        self.assertTrue(TestLexer.test("qw*pod-0=023/", "qw,*,pod,-,0,=,0,23,/,<EOF>", 150))
    def test_operators5(self):
        self.assertTrue(TestLexer.test("+-=!lolol-=", "+,-,=,!,lolol,-,=,<EOF>", 151))
    
    def test_seperators2(self):
        self.assertTrue(TestLexer.test("[a]=69", "[,a,],=,69,<EOF>", 152))
    def test_seperators3(self):
        self.assertTrue(TestLexer.test("a, b, c, d", "a,,,b,,,c,,,d,<EOF>", 153))
    def test_seperators4(self):
        self.assertTrue(TestLexer.test("eq=vsd[1]:103", "eq,=,vsd,[,1,],:,103,<EOF>", 154))
    def test_seperators5(self):
        self.assertTrue(TestLexer.test("we!=1vs9", "we,!=,1,vs9,<EOF>", 155))

    def test_string8(self):
        self.assertTrue(TestLexer.test(""" """, "<EOF>", 156))
    def test_string9(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 157))
    def test_string10(self):
        self.assertTrue(TestLexer.test(""" "This is an outside string: \\"This is an inside tring\\"" """, "This is an outside string: \\\"This is an inside tring\\\",<EOF>", 158))
    def test_string11(self):
        self.assertTrue(TestLexer.test(""" "\\n \\b \\t\\f" """, "\\n \\b \\t\\f,<EOF>", 159))
    def test_string12(self):
        self.assertTrue(TestLexer.test(""" \\n \\b \\t\\f """, "Error Token \\", 160))