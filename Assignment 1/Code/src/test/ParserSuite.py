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
            c = func("Hello","World");
            printString(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_func_decl3(self):
        input = """
        main: function void() {
            /* A C-style comment */
            a=5; // A C++ style comment
            printInt(a);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_func_decl4(self):
        input = """
        main: function void() {
            a = readInteger();
            printInteger(a);
            b = readFloat();
            printFloat(b);
            c = readBoolean();
            printBoolean(c);
            d = readString();
            printString(d);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_func_decl5(self):
        input = """
        readInteger: function integer () {
            return 1;
        }
        main: function void() {
            n = readInteger();
        }"""
        expect = "Error on line 2 col 8: readInteger"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_func_decl6(self):
        input = """
        printString: function void (a: string) {
            return;
        }
        main: function void() {
            printString("hello world!");
        }"""
        expect = "Error on line 2 col 8: printString"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_func_decl7(self):
        input = """
        main: function void() {
            x, y : integer = 5, 6;
            r : auto = (x - 5) * (x - 5) + (y - 4) * (y - 4);
            printInteger(r);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_func_decl8(self):
        input = """
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
        main: function void() {
            delta: integer = fact(3);
            inc(c, delta);
            printInteger(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_stmts1(self):
        input = """
        main: function void() {
            // Test assignment statement
            a, b, c, d: auto;
            a = 5;
            b = true;
            c = "Hello";
            d = 4.5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_stmts2(self):
        input = """
        main: function void() {
            // Test if statement
            if (true) output = 1+2*(3-4%5*(-6));
            printInteger(output);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    
    def test_stmts3(self):
        input = """
        main: function void() {
            // Test if statement
            a, b: integer = 2, 3;
            if (a > b) output = 1+2*(3-4%5*(-6));
            else output = readInteger();
            printInteger(output);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test_stmts4(self):
        input = """
        main: function void() {
            // Test for statement
            for (i = 1, i < 10, i + 1) {
                output = readInteger();
                printInteger(output);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_stmts5(self):
        input = """
        main: function void() {
            // Test while statement
            i = 1000;
            while (i >= 0) {
                printInteger(i);
                i = i / 2;
                i - 1;
            }
        }"""
        expect = "Error on line 8 col 18: -"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_stmts6(self):
        input = """
        main: function void() {
            // Test do statement
            i = 1000;
            do {
                printInteger(i);
                i = i / 3;
            }
            while (i >= 0)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_stmts7(self):
        input = """
        main: function void() {
            // Test break statement
            i = 1000;
            do {
                printInteger(i);
                i = i / 3;
                break;
            }
            while (i >= 0)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_stmts8(self):
        input = """
        main: function void() {
            // Test break statement
            i = 1000;
            do {
                printInteger(i);
                i = i / 6;
                continue;
            }
            while (i >= 0)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_stmts9(self):
        input = """
        main: function void() {
            // Test break statement
            i = 1000;
            do {
                printInteger(i);
                i = i / 4;
                if (i == 250) break;
            }
            while (i >= 0)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_stmts10(self):
        input = """
        main: function void() {
            // Test call statement
            fooaewirjp(2 + x, 4.0 / y);
            goocjaslk();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_stmts11(self):
        input = """
        main: function void() {
            // Test block statement
            r, s: integer;
            r = 5.0;
            s = r * r * myPI;
            a, b: array [51] of integer;
            a[2] = s;
            b[34] = r;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_fibonacci(self):
        input = """
        fibonacci: function integer(n: integer) {
            if (n <= 0) return 0;
            if (n == 1) return 1;
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
        main: function void() {
            printInteger(fibonacci(5));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_check(self):
        input = """

        main: function void() {
            for(i=1, i <= n, i + 1)    
                if (i <= 5) printInteger(i);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_sum(self):
        input = """
        sum: function integer(a: integer, b: integer) {
            return a + b;
        }
        main: function void() {
            printInteger(sum(4, 9));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_swap(self):
        input = """
        swap: function void(a: integer, b: integer) {
            a = a + b;
            b = a - b;
            a = a - b;
        }
        main: function void() {
            a, b: integer = 4, 9;
            swap(a, b);
            printInteger(a);
            printInteger(b);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_print_Hello(self):
        input = """
        main: function void() {
            if(printString("hello world")){}    
            return;  
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_print_triangle(self):
        input = """
        main: function void() {
            n: integer;
            for(i=1, i <= n, i + 1)    
            {    
                for(j=1, j <=n - i, j + 1)    
                {    
                    printString(" ");    
                }    
                for(k=1, k <= i, k + 1)    
                {    
                    printInteger(k);    
                }    
                for(l=i-1, l >= 1, l - 1)    
                {    
                    printInteger(l);    
                }    
                printString("\\n");    
            }    
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_print_triangle(self):
        input = """
        main: function void() {
            array
            for(i=1, i <= n, i + 1)    
            {    
                for(j=1, j <=n - i, j + 1)    
                {    
                    printString(" ");    
                }    
                for(k=1, k <= i, k + 1)    
                {    
                    printInteger(k);    
                }    
                for(l=i-1, l >= 1, l - 1)    
                {    
                    printInteger(l);    
                }    
                printString("\\n");    
            }    
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))