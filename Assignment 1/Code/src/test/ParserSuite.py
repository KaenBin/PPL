import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        
    def test_variable_declaration(self):
        input = """delta: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        input = """x: integer = 65;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
        input = """delta: integer = 3+2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 206))
        
    def test_function_declaration(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
