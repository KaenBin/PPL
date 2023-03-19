import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

# Nguyen Ngoc Hung - 2053075

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_ast_generation6(self):
        """TEST AST 06"""
        input = """main: function void () {
            printIntegers(4, 5);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printIntegers, IntegerLit(4), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_ast_generation7(self):
        """TEST AST 07"""
        input = """main: function void () {
            printNumber(4, 5.0);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printNumber, IntegerLit(4), FloatLit(5.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_ast_generation8(self):
        """TEST AST 08"""
        input = """main: function void () {
            printIntegers(4, iloveu);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printIntegers, IntegerLit(4), Id(iloveu))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_ast_generation9(self):
        """TEST AST 09"""
        input = """main: function void () {
            printIntegers(addint(4), iloveu);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printIntegers, FuncCall(addint, [IntegerLit(4)]), Id(iloveu))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_ast_generation10(self):
        """TEST AST 010"""
        input = """main: function void () {
            printString("HeeeellloWOOODRLLD");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(HeeeellloWOOODRLLD))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_ast_generation11(self):
        """TEST AST 011 - AssignStmt"""
        input = """main: function void () {
            a: integer;
            a = 5;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_ast_generation12(self):
        """TEST AST 012 - ArrayDeclare"""
        input = """main: function void () {
            x: array [3] of integer;
        }"""
            #a = {1, 2, 3};
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType))]))
])"""
        #AssignStmt(Id(a), ArrayLit([1, 2, 3]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_ast_generation13(self):
        """TEST AST 013 - AssignStmt"""
        input = """main: function void () {
            x: array [3] of integer;
            x = {1, 2, 3};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType)), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_ast_generation14(self):
        """TEST AST 014 - BinExpr"""
        input = """main: function void () {
            x: integer = 1 + 5;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_ast_generation15(self):
        """TEST AST 015 - BinExpr"""
        input = """main: function void () {
            x: boolean = 1 < 5;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, BooleanType, BinExpr(<, IntegerLit(1), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_ast_generation16(self):
        """TEST AST 016 - IfStmt"""
        input = """main: function void () {
            if (a < b) printString("a is less than b");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), CallStmt(printString, StringLit(a is less than b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315)) 

    def test_ast_generation17(self):
        """TEST AST 017 - IfStmt Else"""
        input = """main: function void () {
            if (a < b) printString("a is less than b");
            else printString("a is bigger than b");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), CallStmt(printString, StringLit(a is less than b)), CallStmt(printString, StringLit(a is bigger than b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316)) 

    def test_ast_generation18(self):
        """TEST AST 018 - ForStmt"""
        input = """main: function void () {
            for (i = 1, i < 10, i + 1){
                printInteger(i);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317)) 

    def test_ast_generation19(self):
        """TEST AST 019 - WhileStmt"""
        input = """main: function void () {
            while (i < 10) printInteger(i);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), CallStmt(printInteger, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318)) 

    def test_ast_generation20(self):
        """TEST AST 020 - DoWhileStmt"""
        input = """main: function void () {
            do {
                printInteger(i);
            } while (i < 10);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319)) 

    def test_ast_generation21(self):
        """TEST AST 021 - BreakStmt"""
        input = """main: function void () {
            do {
                printInteger(i);
                break;
            } while (i < 10);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(i)), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320)) 

    def test_ast_generation22(self):
        """TEST AST 022 - ContinueStmt"""
        input = """main: function void () {
            // print from 0 to 9 without 3
            i: integer = 0;
            do {
                if (i == 3) continue; 
                printInteger(i);
            } while (i < 10);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(3)), ContinueStmt()), CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321)) 

    def test_ast_generation23(self):
        """TEST AST 023 - returnStmt"""
        input = """
        add: function integer (a: integer, b: integer) {
            return a + b;
        }

        main: function void () {
            a: integer = add(10, 1938);
            printInteger(a);
        }"""
        expect = """Program([
	FuncDecl(add, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(add, [IntegerLit(10), IntegerLit(1938)])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322)) 

    def test_ast_generation24(self):
        """TEST AST 024 - ReturnStmt"""
        input = """
        add: function integer (inherit a: integer, inherit out b: integer) {
            return a + b;
        }

        main: function void () {
            a: integer = add(10, 1938);
            printInteger(a);
        }"""
        expect = """Program([
	FuncDecl(add, IntegerType, [InheritParam(a, IntegerType), InheritOutParam(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(add, [IntegerLit(10), IntegerLit(1938)])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323)) 

    def test_ast_generation25(self):
        """TEST AST 025 - AssignArray"""
        input = """
        main: function void () {
            a: array [3] of integer;
            a[3] = 10;
            printInteger(a[3]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(3)]), IntegerLit(10)), CallStmt(printInteger, ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324)) 

    def test_ast_generation26(self):
        """TEST AST 026 - AssignArray"""
        input = """
        main: function void () {
            a: array [2,3] of integer;
            a[0,3] = 10;
            printInteger(a[0,3]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 3], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(3)]), IntegerLit(10)), CallStmt(printInteger, ArrayCell(a, [IntegerLit(0), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325)) 

    def test_ast_generation27(self):
        """TEST AST 027"""
        input = """
        main: function void () {
            init_decl_expr: float = 3.14 + 1.2;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(init_decl_expr, FloatType, BinExpr(+, FloatLit(3.14), FloatLit(1.2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326)) 

    def test_ast_generation28(self):
        """TEST AST 028"""
        input = """
        main: function void () {
            literal_int: integer = 10;
            literal_float: float = 3.14;
            literal_bool: boolean = false;
            literal_string: string = "hello";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(literal_int, IntegerType, IntegerLit(10)), VarDecl(literal_float, FloatType, FloatLit(3.14)), VarDecl(literal_bool, BooleanType, BooleanLit(False)), VarDecl(literal_string, StringType, StringLit(hello))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327)) 

    def test_ast_generation29(self):
        """TEST AST 029"""
        input = """
        main: function void () {
            literal_array: array [2] of integer = {1, 2};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(literal_array, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328)) 

    def test_ast_generation30(self):
        """TEST AST 030"""
        input = """
        main: function void () {
            a, b, c, d, e, f, g, h, y, i, k, l: integer;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), VarDecl(d, IntegerType), VarDecl(e, IntegerType), VarDecl(f, IntegerType), VarDecl(g, IntegerType), VarDecl(h, IntegerType), VarDecl(y, IntegerType), VarDecl(i, IntegerType), VarDecl(k, IntegerType), VarDecl(l, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329)) 

    def test_ast_generation31(self):
        """TEST AST 031"""
        input = """
        main: function void () {
            a: float = 123e-123;
            writeFloat(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(1.23e-121)), CallStmt(writeFloat, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330)) 

    def test_ast_generation32(self):
        """TEST AST 032"""
        input = """
        main: function void () {
            a: integer = 0;
            for(i = 0, i < 6, i + 1) {
                a = a + i;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(6)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331)) 

    def test_ast_generation33(self):
        """TEST AST 033"""
        input = """
        main: function void () {
            a: integer = 0;
            for(i = 0, i < 6, i + 1) {
                a = a + i;
            }
            printInteger(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(6)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332)) 

    def test_ast_generation34(self):
        """TEST AST 034"""
        input = """
        main: function void () {
            a: integer = 0;
            b: integer = 6;
            for(i = 0, i < 6, i + 1) {
                a = a + i;
            }
            printInteger(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(6)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(6)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333)) 

    def test_ast_generation35(self):
        """TEST AST 035"""
        input = """
        main: function void () {
            a: integer = 0;
            b: integer = 10;
            for(i = 0, i < 6, i + 1) {
                a = a + i;
            }
            printInteger(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(10)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(6)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334)) 

    def test_ast_generation36(self):
        """TEST AST 036"""
        input = """
        main: function void () {
            a: integer = 0;
            b: integer = 6;
            for(i = 0, i < 6, i + 1) {
                a = a + i;
            }
            printInteger(a);
            printInteger(b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(6)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(6)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))])), CallStmt(printInteger, Id(a)), CallStmt(printInteger, Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335)) 

    def test_ast_generation37(self):
        """TEST AST 037"""
        input = """
        main: function void () {
            if(true) return true;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ReturnStmt(BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336)) 

    def test_ast_generation38(self):
        """TEST AST 038"""
        input = """
        main: function void () {
            if(true) return true;
            else return false;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337)) 

    def test_ast_generation39(self):
        """TEST AST 039"""
        input = """
        main: function void () {
            if(false) return false;
            else return true;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(False), ReturnStmt(BooleanLit(False)), ReturnStmt(BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338)) 

# Nguyen Ngoc Hung - 2053075

    def test_ast_generation040(self):
        """TEST AST 040"""
        input = """
        getMax: function integer (a: integer, b: integer) {
            if(a >= b) return a;
            else return b;
        }

        main: function void () {
            a = getMax(5, 40394092);
            printInteger(a);
        }"""
        expect = """Program([
	FuncDecl(getMax, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(getMax, [IntegerLit(5), IntegerLit(40394092)])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_ast_generation041(self):
        """TEST AST 041"""
        input = """
        getMin: function integer (a: integer, b: integer) {
            if(a <= b) return a;
            else return b;
        }

        main: function void () {
            a = getMin(5, 40394092);
            printInteger(a);
        }"""
        expect = """Program([
	FuncDecl(getMin, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(getMin, [IntegerLit(5), IntegerLit(40394092)])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_ast_generation042(self):
        """TEST AST 042"""
        input = """
        mul: function integer(a: integer, b: integer) {
            return a * b;
        }
        main: function void () {
            printInteger(mul(4, 5));
        }"""
        expect = """Program([
	FuncDecl(mul, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(mul, [IntegerLit(4), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_ast_generation043(self):
        """TEST AST 043"""
        input = """
        div: function integer(a: integer, b: integer) {
            return a / b;
        }
        main: function void () {
            printInteger(div(4, 2));
        }"""
        expect = """Program([
	FuncDecl(div, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(div, [IntegerLit(4), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_ast_generation044(self):
        """TEST AST 044"""
        input = """
        absMinus: function integer(a: integer, b: integer) {
            if (a >= b) return a - b;
            else return b - a;
        }
        main: function void () {
            printInteger(absMinus(4, 2));
        }"""
        expect = """Program([
	FuncDecl(absMinus, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(a), Id(b)), ReturnStmt(BinExpr(-, Id(a), Id(b))), ReturnStmt(BinExpr(-, Id(b), Id(a))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(absMinus, [IntegerLit(4), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

# Nguyen Ngoc Hung - 2053075

    def test_ast_generation045(self):
        """TEST AST 045"""
        input = """
        a, b, c, d, e, f, g, h, y, i, k, l: integer;
        """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	VarDecl(d, IntegerType)
	VarDecl(e, IntegerType)
	VarDecl(f, IntegerType)
	VarDecl(g, IntegerType)
	VarDecl(h, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(i, IntegerType)
	VarDecl(k, IntegerType)
	VarDecl(l, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_ast_generation046(self):
        """TEST AST 046"""
        input = """
        main: function void () {
            a: integer = 8;
            b: array [3] of integer;
            for(i = 0, i < 3, i + 1){
                b[i] = i + 8;
            }
            printInteger(b[2]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(8)), VarDecl(b, ArrayType([3], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(b, [Id(i)]), BinExpr(+, Id(i), IntegerLit(8)))])), CallStmt(printInteger, ArrayCell(b, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_ast_generation047(self):
        """TEST AST 047"""
        input = """
        main: function void () {
            b: array [3] of integer = {1, 2, 3};
            for(i = 0, i < 3, i + 1){
                b[i] = b[i] * 2;
            }
            printInteger(b[2]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(b, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(b, [Id(i)]), BinExpr(*, ArrayCell(b, [Id(i)]), IntegerLit(2)))])), CallStmt(printInteger, ArrayCell(b, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_ast_generation048(self):
        """TEST AST 048"""
        input = """
        main: function void () {
            printString("O_O");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(O_O))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_ast_generation049(self):
        """TEST AST 049"""
        input = """
        main: function void () {
            a: string = "Heelloo";
            b: string = "HUNG";
            a = a :: b;
            printString(a);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(Heelloo)), VarDecl(b, StringType, StringLit(HUNG)), AssignStmt(Id(a), BinExpr(::, Id(a), Id(b))), CallStmt(printString, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_ast_generation050(self):
        """TEST AST 050"""
        input = """
        main: function void () {
            a: boolean = true;
            return;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BooleanLit(True)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_ast_generation051(self):
        """TEST AST 051"""
        input = """
        main: function void () {
            a_plus_b: integer;
            a, b: integer = 10970918723479, 234868125816;
            a_plus_b = a + b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a_plus_b, IntegerType), VarDecl(a, IntegerType, IntegerLit(10970918723479)), VarDecl(b, IntegerType, IntegerLit(234868125816)), AssignStmt(Id(a_plus_b), BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_ast_generation052(self):
        """TEST AST 052"""
        input = """
        a, b: integer = 10970918723479, 234868125816;
        main: function void () {
            printBoolean(a < b);
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(10970918723479))
	VarDecl(b, IntegerType, IntegerLit(234868125816))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, BinExpr(<, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_ast_generation053(self):
        """TEST AST 053"""
        input = """
        a, b: integer = 10970918723479, 234868125816;
        main: function void () {
            printBoolean(a > b);
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(10970918723479))
	VarDecl(b, IntegerType, IntegerLit(234868125816))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, BinExpr(>, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_ast_generation054(self):
        """TEST AST 054"""
        input = """
        a, b: integer = 10970918723479, 234868125816;
        main: function void () {
            printBoolean(a >= b);
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(10970918723479))
	VarDecl(b, IntegerType, IntegerLit(234868125816))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, BinExpr(>=, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_ast_generation055(self):
        """TEST AST 055"""
        input = """
        a, b: integer = 10970918723479, 234868125816;
        main: function void () {
            printBoolean(a <= b);
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(10970918723479))
	VarDecl(b, IntegerType, IntegerLit(234868125816))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, BinExpr(<=, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_ast_generation056(self):
        """TEST AST 056"""
        input = """
        a, b: integer = 10970918723479, 234868125816;
        main: function void () {
            printBoolean(a == b);
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(10970918723479))
	VarDecl(b, IntegerType, IntegerLit(234868125816))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, BinExpr(==, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_ast_generation057(self):
        """TEST AST 057"""
        input = """
        main: function void () {
            arr: array [10] of integer;
            arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            arr[1] = arr[8] + arr[9];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), BinExpr(+, ArrayCell(arr, [IntegerLit(8)]), ArrayCell(arr, [IntegerLit(9)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_ast_generation058(self):
        """TEST AST 058"""
        input = """
        main: function void () {
            arr: array [10] of integer;
            arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            arr[1] = arr[8] * arr[9];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), BinExpr(*, ArrayCell(arr, [IntegerLit(8)]), ArrayCell(arr, [IntegerLit(9)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_ast_generation059(self):
        """TEST AST 059"""
        input = """
        main: function void () {
            arr: array [10] of integer;
            arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            arr[1] = arr[8] - arr[9];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), BinExpr(-, ArrayCell(arr, [IntegerLit(8)]), ArrayCell(arr, [IntegerLit(9)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_ast_generation060(self):
        """TEST AST 060"""
        input = """
        main: function void () {
            arr: array [10] of integer;
            arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            arr[1] = arr[8] + arr[9] + arr[0];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), BinExpr(+, BinExpr(+, ArrayCell(arr, [IntegerLit(8)]), ArrayCell(arr, [IntegerLit(9)])), ArrayCell(arr, [IntegerLit(0)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_ast_generation061(self):
        """TEST AST 061"""
        input = """
        a, b, c, d, e, f: integer = 1, 2, 3, 4, 5, 6;
        main: function void () {
            return a + b * c / d + e - f;
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(d, IntegerType, IntegerLit(4))
	VarDecl(e, IntegerType, IntegerLit(5))
	VarDecl(f, IntegerType, IntegerLit(6))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(-, BinExpr(+, BinExpr(+, Id(a), BinExpr(/, BinExpr(*, Id(b), Id(c)), Id(d))), Id(e)), Id(f)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_ast_generation062(self):
        """TEST AST 062"""
        input = """
        main: function void () {
            Hung_name: string = "Hung";
            Hung_age: integer = 2023 - 2002;
            printString(Hung_name);
            printInteger(Hung_age);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(Hung_name, StringType, StringLit(Hung)), VarDecl(Hung_age, IntegerType, BinExpr(-, IntegerLit(2023), IntegerLit(2002))), CallStmt(printString, Id(Hung_name)), CallStmt(printInteger, Id(Hung_age))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_ast_generation063(self):
        """TEST AST 063"""
        input = """
        main: function void () {
            a: float = 11e-11;
            b: float = 12.12;
            writeFloat(a + b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(1.1e-10)), VarDecl(b, FloatType, FloatLit(12.12)), CallStmt(writeFloat, BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_ast_generation064(self):
        """TEST AST 064"""
        input = """
        main: function void () {
            a: float = 11e-11;
            b: float = 12.12;
            writeFloat(a - b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(1.1e-10)), VarDecl(b, FloatType, FloatLit(12.12)), CallStmt(writeFloat, BinExpr(-, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_ast_generation065(self):
        """TEST AST 065"""
        input = """
        main: function void () {
            id_1: integer = 1;
            id_2: integer = 2;
            id_1_2: string = "1 2";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(id_1, IntegerType, IntegerLit(1)), VarDecl(id_2, IntegerType, IntegerLit(2)), VarDecl(id_1_2, StringType, StringLit(1 2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_ast_generation066(self):
        """TEST AST 066"""
        input = """
        main: function void () {
            a: integer = readInteger();
            b: integer = readInteger();
            if(a < b) printString("a less than b");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(readInteger, [])), VarDecl(b, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(<, Id(a), Id(b)), CallStmt(printString, StringLit(a less than b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_ast_generation067(self):
        """TEST AST 067"""
        input = """
        main: function void () {
            a: integer = readInteger();
            b: integer = readInteger();
            if(a > b) printString("a bigger than b");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(readInteger, [])), VarDecl(b, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(>, Id(a), Id(b)), CallStmt(printString, StringLit(a bigger than b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_ast_generation068(self):
        """TEST AST 068"""
        input = """
        main: function void () {
            a: integer = readInteger();
            b: integer = readInteger();
            if(a == b) printString("a equals b");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(readInteger, [])), VarDecl(b, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(printString, StringLit(a equals b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_ast_generation069(self):
        """TEST AST 069"""
        input = """
        main: function void () {
            a: integer = readInteger();
            b: integer = readInteger();
            if(a % b == 0) printString("a divisible by b");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(readInteger, [])), VarDecl(b, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(==, BinExpr(%, Id(a), Id(b)), IntegerLit(0)), CallStmt(printString, StringLit(a divisible by b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_ast_generation070(self):
        """TEST AST 070"""
        input = """
        main: function void () {
            a: integer = readInteger();
            b: integer = readInteger();
            if(a % b == 0) printString("a divisible by b");
            else printString("a not divisible by b");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(readInteger, [])), VarDecl(b, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(==, BinExpr(%, Id(a), Id(b)), IntegerLit(0)), CallStmt(printString, StringLit(a divisible by b)), CallStmt(printString, StringLit(a not divisible by b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_ast_generation071(self):
        """TEST AST 071"""
        input = """
        main: function void () {
            username: string = readString();
            printString("Hello " :: username);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(username, StringType, FuncCall(readString, [])), CallStmt(printString, BinExpr(::, StringLit(Hello ), Id(username)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_ast_generation072(self):
        """TEST AST 072"""
        input = """
        main: function void () {
            a: integer = -123;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, UnExpr(-, IntegerLit(123)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_ast_generation073(self):
        """TEST AST 073"""
        input = """
        main: function void () {
            a: boolean = readBoolean();
            if(!a) return false;
            return true;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, FuncCall(readBoolean, [])), IfStmt(UnExpr(!, Id(a)), ReturnStmt(BooleanLit(False))), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_ast_generation074(self):
        """TEST AST 074"""
        input = """
        main: function void () {
            a: float = readFloat();
            b: float = readFloat();
            return a > b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FuncCall(readFloat, [])), VarDecl(b, FloatType, FuncCall(readFloat, [])), ReturnStmt(BinExpr(>, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_ast_generation075(self):
        """TEST AST 075"""
        input = """
        main: function void () {
            a: float = readFloat();
            b: float = readFloat();
            return a < b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FuncCall(readFloat, [])), VarDecl(b, FloatType, FuncCall(readFloat, [])), ReturnStmt(BinExpr(<, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_ast_generation076(self):
        """TEST AST 076"""
        input = """
        main: function void () {
            a: float = readFloat();
            b: float = readFloat();
            return a == b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FuncCall(readFloat, [])), VarDecl(b, FloatType, FuncCall(readFloat, [])), ReturnStmt(BinExpr(==, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_ast_generation077(self):
        """TEST AST 077"""
        input = """
        main: function void () {
            a: array [3] of float;
            a = {1.2, 2.3, 3.4};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], FloatType)), AssignStmt(Id(a), ArrayLit([FloatLit(1.2), FloatLit(2.3), FloatLit(3.4)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_ast_generation078(self):
        """TEST AST 078"""
        input = """
        main: function void () {
            a: array [3] of float = {1.2, 2.3, 3.4};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], FloatType), ArrayLit([FloatLit(1.2), FloatLit(2.3), FloatLit(3.4)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_ast_generation079(self):
        """TEST AST 079"""
        input = """
        main: function void () {
            cars: array [3] of string = {"Volvo", "BMX", "VinFast"};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(cars, ArrayType([3], StringType), ArrayLit([StringLit(Volvo), StringLit(BMX), StringLit(VinFast)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_ast_generation080(self):
        """TEST AST 080"""
        input = """
        main: function void () {
            cars: array [3] of string; 
            cars = {"Volvo", "BMX", "VinFast"};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(cars, ArrayType([3], StringType)), AssignStmt(Id(cars), ArrayLit([StringLit(Volvo), StringLit(BMX), StringLit(VinFast)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_ast_generation081(self):
        """TEST AST 081"""
        input = """
        main: function void () {
            cars: array [3] of string; 
            cars = {"Volvo", "BMX", "VinFast"};
            printString(cars[0]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(cars, ArrayType([3], StringType)), AssignStmt(Id(cars), ArrayLit([StringLit(Volvo), StringLit(BMX), StringLit(VinFast)])), CallStmt(printString, ArrayCell(cars, [IntegerLit(0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_ast_generation082(self):
        """TEST AST 082"""
        input = """
        main: function void () {
            cars: array [3] of string; 
            cars = {"Volvo", "BMX", "VinFast"};
            for(i = 0, i < 3, i + 1) {
                printString(cars[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(cars, ArrayType([3], StringType)), AssignStmt(Id(cars), ArrayLit([StringLit(Volvo), StringLit(BMX), StringLit(VinFast)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(cars, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_ast_generation083(self):
        """TEST AST 083"""
        input = """
        main: function void () {
            input: array [3] of integer;
            input[0] = readInteger();
            input[1] = readInteger();
            input[2] = readInteger();
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(input, ArrayType([3], IntegerType)), AssignStmt(ArrayCell(input, [IntegerLit(0)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(input, [IntegerLit(1)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(input, [IntegerLit(2)]), FuncCall(readInteger, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_ast_generation084(self):
        """TEST AST 084"""
        input = """
        main: function void () {
            input: array [3] of integer;
            input[0] = readInteger();
            input[1] = readInteger();
            input[2] = readInteger();
            sum: integer = input[0] + input[1] + input[2];
            printInteger(sum);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(input, ArrayType([3], IntegerType)), AssignStmt(ArrayCell(input, [IntegerLit(0)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(input, [IntegerLit(1)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(input, [IntegerLit(2)]), FuncCall(readInteger, [])), VarDecl(sum, IntegerType, BinExpr(+, BinExpr(+, ArrayCell(input, [IntegerLit(0)]), ArrayCell(input, [IntegerLit(1)])), ArrayCell(input, [IntegerLit(2)]))), CallStmt(printInteger, Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_ast_generation085(self):
        """TEST AST 085"""
        input = """
        main: function void () {
            input: array [3] of integer;
            input[0] = readInteger();
            input[1] = readInteger();
            input[2] = readInteger();
            mul: integer = input[0] * input[1] * input[2];
            printInteger(mul);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(input, ArrayType([3], IntegerType)), AssignStmt(ArrayCell(input, [IntegerLit(0)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(input, [IntegerLit(1)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(input, [IntegerLit(2)]), FuncCall(readInteger, [])), VarDecl(mul, IntegerType, BinExpr(*, BinExpr(*, ArrayCell(input, [IntegerLit(0)]), ArrayCell(input, [IntegerLit(1)])), ArrayCell(input, [IntegerLit(2)]))), CallStmt(printInteger, Id(mul))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_ast_generation086(self):
        """TEST AST 086"""
        input = """
        main: function void () {
            neg: integer = -15;
            pos: integer = 15;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(neg, IntegerType, UnExpr(-, IntegerLit(15))), VarDecl(pos, IntegerType, IntegerLit(15))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_ast_generation087(self):
        """TEST AST 087"""
        input = """
        main: function void () {
            boolarr: array [5] of boolean;
            boolarr = {true, false, true, false, true};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(boolarr, ArrayType([5], BooleanType)), AssignStmt(Id(boolarr), ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True), BooleanLit(False), BooleanLit(True)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_ast_generation088(self):
        """TEST AST 088"""
        input = """
        main: function void () {
            boolarr: array [5] of boolean;
            boolarr = {true, false, true, false, true};
            for(i = 0, i < 5, i + 1){
                printBoolean(boolarr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(boolarr, ArrayType([5], BooleanType)), AssignStmt(Id(boolarr), ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True), BooleanLit(False), BooleanLit(True)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printBoolean, ArrayCell(boolarr, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_ast_generation089(self):
        """TEST AST 089"""
        input = """
        main: function void () {
            boolarr: array [5] of boolean;
            boolarr = {true, false, true, false, true};
            for(i = 0, i < 5, i + 1){
                if(boolarr[i]) printBoolean(boolarr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(boolarr, ArrayType([5], BooleanType)), AssignStmt(Id(boolarr), ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True), BooleanLit(False), BooleanLit(True)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(ArrayCell(boolarr, [Id(i)]), CallStmt(printBoolean, ArrayCell(boolarr, [Id(i)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_ast_generation090(self):
        """TEST AST 090"""
        input = """
        main: function void () {
            boolarr: array [5] of boolean;
            boolarr = {true, false, true, false, true};
            for(i = 0, i < 5, i + 1){
                if(!boolarr[i]) printBoolean(boolarr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(boolarr, ArrayType([5], BooleanType)), AssignStmt(Id(boolarr), ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True), BooleanLit(False), BooleanLit(True)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, ArrayCell(boolarr, [Id(i)])), CallStmt(printBoolean, ArrayCell(boolarr, [Id(i)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_ast_generation091(self):
        """TEST AST 091"""
        input = """
        main: function void () {
            boolarr: array [5] of boolean;
            boolarr[0] = readBoolean();
            boolarr[1] = readBoolean();
            boolarr[2] = readBoolean();
            boolarr[3] = readBoolean();
            boolarr[4] = readBoolean();
            for(i = 0, i < 5, i + 1){
                if(boolarr[i]) printBoolean(boolarr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(boolarr, ArrayType([5], BooleanType)), AssignStmt(ArrayCell(boolarr, [IntegerLit(0)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(1)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(2)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(3)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(4)]), FuncCall(readBoolean, [])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(ArrayCell(boolarr, [Id(i)]), CallStmt(printBoolean, ArrayCell(boolarr, [Id(i)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_ast_generation092(self):
        """TEST AST 092"""
        input = """
        main: function void () {
            boolarr: array [5] of boolean;
            boolarr[0] = readBoolean();
            boolarr[1] = readBoolean();
            boolarr[2] = readBoolean();
            boolarr[3] = readBoolean();
            boolarr[4] = readBoolean();
            for(i = 0, i < 5, i + 1){
                if(!boolarr[i]) printBoolean(boolarr[i]);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(boolarr, ArrayType([5], BooleanType)), AssignStmt(ArrayCell(boolarr, [IntegerLit(0)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(1)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(2)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(3)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(4)]), FuncCall(readBoolean, [])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, ArrayCell(boolarr, [Id(i)])), CallStmt(printBoolean, ArrayCell(boolarr, [Id(i)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_ast_generation093(self):
        """TEST AST 093"""
        input = """
        main: function void () {
            boolarr: array [5] of boolean;
            boolarr[0] = readBoolean();
            boolarr[1] = readBoolean();
            boolarr[2] = readBoolean();
            boolarr[3] = readBoolean();
            boolarr[4] = readBoolean();
            countTrue: integer = 0;
            for(i = 0, i < 5, i + 1){
                if(boolarr[i]) countTrue = countTrue + 1;
            }
            printInteger(countTrue);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(boolarr, ArrayType([5], BooleanType)), AssignStmt(ArrayCell(boolarr, [IntegerLit(0)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(1)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(2)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(3)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(4)]), FuncCall(readBoolean, [])), VarDecl(countTrue, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(ArrayCell(boolarr, [Id(i)]), AssignStmt(Id(countTrue), BinExpr(+, Id(countTrue), IntegerLit(1))))])), CallStmt(printInteger, Id(countTrue))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_ast_generation094(self):
        """TEST AST 094"""
        input = """
        main: function void () {
            boolarr: array [5] of boolean;
            boolarr[0] = readBoolean();
            boolarr[1] = readBoolean();
            boolarr[2] = readBoolean();
            boolarr[3] = readBoolean();
            boolarr[4] = readBoolean();
            countFalse: integer = 0;
            for(i = 0, i < 5, i + 1){
                if(boolarr[i]) countFalse = countFalse + 1;
            }
            printInteger(countFalse);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(boolarr, ArrayType([5], BooleanType)), AssignStmt(ArrayCell(boolarr, [IntegerLit(0)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(1)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(2)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(3)]), FuncCall(readBoolean, [])), AssignStmt(ArrayCell(boolarr, [IntegerLit(4)]), FuncCall(readBoolean, [])), VarDecl(countFalse, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(ArrayCell(boolarr, [Id(i)]), AssignStmt(Id(countFalse), BinExpr(+, Id(countFalse), IntegerLit(1))))])), CallStmt(printInteger, Id(countFalse))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_ast_generation095(self):
        """TEST AST 095"""
        input = """
        main: function void () {
            intarr: array [5] of integer;
            intarr[0] = readInteger();
            intarr[1] = readInteger();
            intarr[2] = readInteger();
            intarr[3] = readInteger();
            intarr[4] = readInteger();
            countPos: integer = 0;
            for(i = 0, i < 5, i + 1){
                if(intarr[i] > 0) countPos = countPos + 1;
            }
            printInteger(countPos);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(intarr, ArrayType([5], IntegerType)), AssignStmt(ArrayCell(intarr, [IntegerLit(0)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(intarr, [IntegerLit(1)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(intarr, [IntegerLit(2)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(intarr, [IntegerLit(3)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(intarr, [IntegerLit(4)]), FuncCall(readInteger, [])), VarDecl(countPos, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(intarr, [Id(i)]), IntegerLit(0)), AssignStmt(Id(countPos), BinExpr(+, Id(countPos), IntegerLit(1))))])), CallStmt(printInteger, Id(countPos))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

# Nguyen Ngoc Hung - 2053075

    def test_ast_generation096(self):
        """TEST AST 096"""
        input = """
        main: function void () {
            intarr: array [5] of integer;
            intarr[0] = readInteger();
            intarr[1] = readInteger();
            intarr[2] = readInteger();
            intarr[3] = readInteger();
            intarr[4] = readInteger();
            countNeg: integer = 0;
            for(i = 0, i < 5, i + 1){
                if(intarr[i] < 0) countNeg = countNeg + 1;
            }
            printInteger(countNeg);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(intarr, ArrayType([5], IntegerType)), AssignStmt(ArrayCell(intarr, [IntegerLit(0)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(intarr, [IntegerLit(1)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(intarr, [IntegerLit(2)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(intarr, [IntegerLit(3)]), FuncCall(readInteger, [])), AssignStmt(ArrayCell(intarr, [IntegerLit(4)]), FuncCall(readInteger, [])), VarDecl(countNeg, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(intarr, [Id(i)]), IntegerLit(0)), AssignStmt(Id(countNeg), BinExpr(+, Id(countNeg), IntegerLit(1))))])), CallStmt(printInteger, Id(countNeg))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_ast_generation097(self):
        """TEST AST 097"""
        input = """
        main: function void () {
            _acawe8oimklnn_SDA_A__SFA_F_AS_VAS_: string = "Complex identifier";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(_acawe8oimklnn_SDA_A__SFA_F_AS_VAS_, StringType, StringLit(Complex identifier))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_ast_generation098(self):
        """TEST AST 098"""
        input = """
        main: function void () {
            _aca: integer = 43_4342_65476_123____151;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(_aca, IntegerType, IntegerLit(43434265476123151))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_ast_generation099(self):
        """TEST AST 099"""
        input = """
        main: function void () {
            _aca: float = 43_43.42_65476_123____151;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(_aca, FloatType, FloatLit(4343.4265476123155))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_ast_generation100(self):
        """TEST AST 100"""
        input = """
        a, b, c, d: integer = readInteger(), readInteger(), readInteger(), readInteger();
        main: function void () {
            if((a < b) && (c < d)) printString("b is bigger than a, d is bigger than c");
            if((a > b) && (c > d)) printString("a is bigger than b, c is bigger than d");
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(readInteger, []))
	VarDecl(b, IntegerType, FuncCall(readInteger, []))
	VarDecl(c, IntegerType, FuncCall(readInteger, []))
	VarDecl(d, IntegerType, FuncCall(readInteger, []))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(<, Id(a), Id(b)), BinExpr(<, Id(c), Id(d))), CallStmt(printString, StringLit(b is bigger than a, d is bigger than c))), IfStmt(BinExpr(&&, BinExpr(>, Id(a), Id(b)), BinExpr(>, Id(c), Id(d))), CallStmt(printString, StringLit(a is bigger than b, c is bigger than d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

# Nguyen Ngoc Hung - 2053075