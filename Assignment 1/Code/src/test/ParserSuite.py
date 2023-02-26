import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_var_decl1(self):
        input = """delta: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_var_decl2(self):
        input = """x: integer = 69;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_var_decl3(self):
        input = """delta: integer = 3+8;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_var_decl4(self):
        input = """a, b, c: auto = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_var_decl5(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_var_decl6(self):
        input = """a, b, c, d: float = 1.234, 1.2e3, 7E-10, 1_234.567;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_var_decl7(self):
        input = """a, b, c, d: boolean = true, false, true, true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_var_decl8(self):
        input = """test_case_1, test_case_2: string = "All supported escape sequences: \\b \\f \\r \\n \\t \\' \\\\ \\\" ", "A string ";""";
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_var_decl9(self):
        input = """array2D, array3D: array[2,3] of integer, array[3,5,1] of boolean;""";
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_var_decl10(self):
        input = """integer, string: auto;""";
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_func_decl1(self):
        input = """c: integer = 103;
        fact: function integer (i: integer) {
            if (i == 0) return 1;
            else return i * fact(i - 1);
        }
        inc: function void(out i: integer, delta: integer) {
            i = i + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_func_decl2(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_func_decl3(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_func_decl4(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_func_decl5(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_func_decl6(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_func_decl7(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_func_decl8(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_func_decl9(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    
    def test_func_decl10(self):
        input = """
        myFunc: function string (inhirit a: string, b: string) {
            return a :: b;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
