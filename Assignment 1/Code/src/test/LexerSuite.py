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
        
    def test_operators(self):
        self.assertTrue(TestLexer.test("+ - * / % ! && || == != < <= > >= ::",
                                       "+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>", 116))
        
    def test_seperators(self):
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
        # self.assertTrue(TestLexer.test(""" "This is a string containing illegal escape\n" """, """Illegal Escape In String: This is a string containing illegal escape\n\n""", 129))
    def test_string4(self):
        self.assertTrue(TestLexer.test(""" "All supported escape sequences: \\b \\f \\r \\n \\t \\' \\\\ \\\"" """, "All supported escape sequences: \\b \\f \\r \\n \\t \\' \\\\ \\\",<EOF>", 130))
        # self.assertTrue(TestLexer.test(""" "Non-error escapse sequences: \b \f \r \t \' " """, "All supported escape sequences: \\b \\f \\r \\n \\t \\' \\\\ \\\",<EOF>", 131))
    def test_string5(self):
        self.assertTrue(TestLexer.test(""" "First string" "Second string" """, "First string,Second string,<EOF>", 132))