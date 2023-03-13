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

    def test_var_decl11(self):
        input = """main: function void() { printInteger(5); }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_var_decl12(self):
        input = """main: function void() { aabc: void; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_var_decl13(self):
        input = """main: function void() { bool: boolean; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_var_decl14(self):
        input = """main: function void() { b: auto; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    def test_var_decl15(self):
        input = """main: function void() { A: integer = 145; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_var_decl16(self):
        input = """main: function void() { cA: integer = 123+21*41; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_var_decl17(self):
        input = """main: function void() { BXA: integer = 123+456*789/readInteger(); }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
                        
    def test_var_decl18(self):
        input = """main: function void() { 32r8: auto = "Hello world"; }"""
        expect = "Error on line 1 col 24: 32"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_var_decl19(self):
        input = """main: function void() { 0_1239: float = 1.45; }"""
        expect = "Error on line 1 col 24: 0"
        self.assertTrue(TestParser.test(input, expect, 220))

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

    def test_print_triangle_of_alphabets(self):
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
                    printString(k);    
                }    
                for(l=i-1, l >= 1, l - 1)    
                {    
                    printString(l);    
                }    
                printString("\\n");    
            }    
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_print_triangle_of_digits(self):
        input = """
        main: function void() {
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
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_random1(self):
        input = """func: function integer() { a: integer = 124; b: float = 5345.17; printInteger(a); writeFloat(b); return 0; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_random2(self):
        input = """func: function integer() { c, d: integer = 3, 1; 0reurawn (c < d); }"""
        expect = "Error on line 1 col 49: 0"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_random3(self):
        input = """func: function integer() { a, b: integer = 7; return (a &&>= a); }"""
        expect = "Error on line 1 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_random4(self):
        input = """func: function integer() { a, b: integer = 41, 513; a = a 12 b; return (a > b); }"""
        expect = "Error on line 1 col 58: 12"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_random5(self):
        input = """main: function integer() {}}"""
        expect = "Error on line 1 col 27: }"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_random6(self):
        input = """
        main: function void() {
            count: integer = 0; 
            for(i == 13, i < 230, i * 2) 
                {count = count + i;}
            printInteger(count);
        }"""
        expect = "Error on line 4 col 18: =="
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_random7(self):
        input = """random: function auto() { return %41; }"""
        expect = "Error on line 1 col 33: %"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_random8(self):
        input = """checkFloat: funcqwion boolean(num: integer) { if(num > 0) return true; else return false;}"""
        expect = "Error on line 1 col 12: funcqwion"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_random9(self):
        input = """ewaf: integer = 3, 5, 2;"""
        expect = "Error on line 1 col 17: ,"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_random10(self):
        input = """
        fact: function integer (n: int) 
        {   if (n == 0) return 1; 
            else return n * fact(n - 1);} 
        main: function void()
        {
            a: integer = fact(352); 
            printInteger(a);
        }"""
        expect = "Error on line 2 col 35: int"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_random11(self):
        input = """
         main: function void()
        {
            for(i = 0, i < 14, i + 2) 
            {   if(x = 10) break; 
                else printInteger(i);}
        }"""
        expect = "Error on line 5 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_random12(self):
        input = """
        main: function void()
        {
            x: integer = 50; do { x = x - 1;  while (x > 0);
        }"""
        expect = "Error on line 4 col 59: ;"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_random13(self):
        input = """
        main: function void()
        {
            for(i = 0, i < 6 i + 1) 
                {printInteger(i);}
        }"""
        expect = "Error on line 4 col 29: i"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_random14(self):
        input = """printHello: function void() {printString"HelloWorld");}"""
        expect = "Error on line 1 col 40: HelloWorld"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_random15(self):
        input = """min: function float a: float, b: float) { if(a <= b) return a; else return b; }"""
        expect = "Error on line 1 col 20: a"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_random16(self):
        input = """main: function void() {{}"""
        expect = "Error on line 1 col 23: {"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_random17(self):
        input = """max: function integer(c: integer, d: integer) 
                    {   if( >= d) return c; 
                        else return d; }"""
        expect = "Error on line 2 col 28: >="
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_random18(self):
        input = """add: function floatt(a: float, b: float) { return a + b; }"""
        expect = "Error on line 1 col 14: floatt"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_random19(self):
        input = """main: function void() { aB, A, E, e: integer = 1, 2, 3, 4, 8; }"""
        expect = "Error on line 1 col 57: ,"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_random20(self):
        input = """main: function void() { a1, a2, a4, 2a, vba: integer = 1, 2, 3; }"""
        expect = "Error on line 1 col 36: 2"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_random21(self):
        input = """main: function void() { a, b, c: bool = 1, 2, 3, 4, 5; }"""
        expect = "Error on line 1 col 33: bool"
        self.assertTrue(TestParser.test(input, expect, 269))
        
    def test_random22(self):
        input = """main: function void() { a, b, c, d, e,f ,g , h, q: auto = 1, 3, 4, 5, 12; }"""
        expect = "Error on line 1 col 72: ;"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_random23(self):
        input = """main: function void() { a: integer, b: float;; }"""
        expect = "Error on line 1 col 34: ,"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_random24(self):
        input = """
         main: function void()
        {
            for(i = 0, i < 14, i + 2) 
                printInteger(i % 3);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_random25(self):
        input = """
         main: function void()
        {
            for(i = 0, i < 4, i + 2) 
            {
                printInteger(readInteger());
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_random26(self):
        input = """
         main: function void()
        {
            x: integer = 1;
            while (x != 0)
                x = readInteger();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_random27(self):
        input = """
         main: function void()
        {
            x: integer;
            do {
                x = readInteger();
            } while (x != 0)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_random28(self):
        input = """
         main: function void()
        {
            printString("Phan Mai Tan Loi");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_random29(self):
        input = """
         main: function void()
        {
            x: boolean;
            x = readBoolean();
            if (!x) return "False";
            else return "True";;;
        }"""
        expect = "Error on line 7 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_random30(self):
        input = """
        main: function void()
        {
            x: boolean;
            x = readBoolean();
            if (x) return return "True";
            else return "False";
        }"""
        expect = "Error on line 6 col 26: return"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_random31(self):
        input = """
         main: function void()
        {
            printInteger(31*(13-42+readInteger()));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_random32(self):
        input = """
         main: function void()
        {
            a: integer = 9; 
            b: float = 51.67; 
            printInteger(a); 
            printFloat(b);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_random33(self):
        input = """main: function void() { printInteger(5); }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_random34(self):
        input = """main: function void() { aabc: void; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_random35(self):
        input = """main: function void() { bool: boolean; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_random36(self):
        input = """main: function void() { b: auto; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
        
    def test_random37(self):
        input = """main: function void() { A: integer = 145; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_random38(self):
        input = """
         main: function void()
        {
            a: integer = 9; 
            b: float = 51.67; 
            printInteger(a); 
            printFloat(b);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_random39(self):
        input = """
         main: function void()
        {
            printSring(readString()::"EOF");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_random40(self):
        input = """
         main: function void()
        {
            printBoolean(!readBoolean());
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_random41(self):
        input = """
         main: function void()
        {
            printFloat(987+654*321/readFloat());
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_random42(self):
        input = """
         main: function void()
        {
            preventDefault();
            preventDefault();
            preventDefault();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_random43(self):
        input = """
         main: function void()
        {
            /* I am HCMUT K20 */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_random44(self):
        input = """
         main: function void()
        {
            // Please give me good grade
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_random45(self):
        input = """
         main: function void()
        {
            preventDefault()
            preventDefault()
            preventDefault()
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_random46(self):
        input = """
         main: function void()
        {
            sentence: string = "Antlr4 is the best tool";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_random47(self):
        input = """
         main: function void()
        {
            sentence: string = "Visual Studio Code is the best IDE";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
        
    def test_random48(self):
        input = """
        main: function void(){
            n = readInt();
            if ( n % 2 == 0){
                printInt(n);
                printString(" is even!");
            }
            else{
                printInt(n);
                printString(" is odd!");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))  
        
    def test_random49(self):
        input = """
         main: function void()
        {
            if (if (true) return true) printString("Hello everyone");
        }"""
        expect = "Error on line 4 col 16: if"
        self.assertTrue(TestParser.test(input, expect, 297))    
        
    def test_random50(self):
        input = """
        draw: function integer(){

            printString("Enter a positive integer: ");
            num: integer = readInteger();

            // run a loop from 1 to 10
            // print the multiplication table
            for (i = 1, i <= 10, i+1) {
                printInt(n);
                printString(" * ");
                printInt(i);
                printString(" = ");
                n = n*i;
                printInt(n);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))  
        
    def test_random51(self):
        input = """
         main: function void()
        {
            printString("I'm dying both outside and inside /* (T_T) */");            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))                  

    def test_random52(self):
        input = """
         main: function void()
        {
            /* (-_-) (@_@) */
            // (*o*) (X_X)
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300)) 