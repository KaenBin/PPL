// 2052158

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (array_lit | vardecl | funcdecl | stmts | exp)+ EOF ;

var_type: INTEGER | FLOAT | BOOLEAN | STRING | VOID | AUTO | array_type;

// Variable declarations
vardecl: vardecl1 | vardecl2 | vardecl3;

vardecl1: id_list COLON var_type SEMI;
id_list: ID (COMMA ID)* | ;

vardecl2: ID vardecl2_2 exp SEMI;
vardecl2_2: (COMMA ID vardecl2_2 exp COMMA) | (COLON var_type ASSIGN);

vardecl3: ID vardecl3_2 array_type SEMI;
vardecl3_2: (COMMA ID vardecl3_2 array_type COMMA) | COLON;

// Function declarations
funcdecl: ID COLON FUNCTION var_type paradecl block_stmt ;	
paradecl: LRB para_list RRB;
para_list: para (COMMA para)* | ;
para: INHIRIT? OUT? ID COLON var_type;

stmts_list: stmts | block_stmt | exp;
stmts:assign_stmt 
	| if_stmt
	| for_stmt
	| while_stmt
	| do_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt
	| functions;

assign_stmt: assign_lhs assign_stmt2 exp SEMI;
assign_stmt2: (COMMA assign_lhs assign_stmt2 COMMA) | ASSIGN;
assign_lhs: ID | exp_ind;

if_stmt: IF LRB exp RRB stmts_list (ELSE stmts_list)?;

for_stmt: FOR LRB assign_lhs ASSIGN exp COMMA exp COMMA exp RRB stmts_list;
// for_stmt2: COMMA assign_lhs for_stmt2 COMMA | ASSIGN;

while_stmt: WHILE LRB bool_expr RRB stmts_list;
do_stmt: DO block_stmt WHILE LRB bool_expr RRB;
bool_expr: (ID | INTLIT) (exp_bool | exp_rela) (ID | INTLIT);

break_stmt: BREAK SEMI;
continue_stmt: CONT SEMI;
return_stmt: RT exp? SEMI;

call_stmt: ((ID call_body) | functions) SEMI;
call_stmt_no_semi: (ID call_body) | functions;
call_body: LRB call_list RRB;
call_list: exp (COMMA exp)* | ;

block_stmt: LCB block_body RCB;
block_body: (stmts | exp)*;

// Expressions

exp_airth: ADDOP | MINUSOP | MULOP | DIVOP | MODOP;
exp_bool: NEGAOP | CONJOP | DISJOP;
exp_str: CONCAT;
exp_rela: EQUALOP | DIFOP | LESSOP | LESSEQOP | GREATOP | GREATEQOP;
exp_ind: ID LSB expression_list RSB;

exp: exp1 CONCAT exp1 | exp1;
exp1: exp2 (EQUALOP | DIFOP | LESSOP | GREATOP | LESSEQOP | GREATEQOP) exp2 | exp2;
exp2: exp2 (CONJOP | DISJOP) exp3 | exp3;
exp3: exp3 (ADDOP | MINUSOP) exp4 | exp4;
exp4: exp4 (MULOP | DIVOP | MODOP) exp5 | exp5;
exp5: NEGAOP exp5 | exp6;
exp6: MINUSOP exp6 | exp7;
exp7: operands | (LSB (expression_list | exp_ind) RSB);
operands: literals | ID | call_stmt_no_semi | (LRB exp RRB);

// 4. Type system and values
array_type: ARRAY LSB int_list RSB OF literals;
int_list: INTLIT (COMMA INTLIT)* | ;

// Literals
literals: INTLIT | FLOATLIT | BOOL | STRINGLIT | VOID | AUTO;

array_lit: LCB expression_list RCB ;
expression_list: exp (COMMA exp)* | ;

INTLIT: [0] | ([1-9][0-9_]*) {self.text = self.text.replace('_','')};
FLOATLIT: INTLIT DECIMAL? EXPONENT? {self.text = self.text.replace('_','')};
fragment DECIMAL: [.] ([0] | ([1-9]([0-9]* [1-9])?));
fragment EXPONENT: [eE] [-+]? ([0] | ([1-9][0-9]*));
BOOL: 'true' | 'false';
STRINGLIT: '"' (STR_CHAR)* '"' {self.text = self.text[1:-1]};
fragment STR_CHAR: ~[\n"] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [btnfr"'\\] ;

// Seperators:
LSB: '[';
RSB: ']';
LRB: '(';
RRB: ')';
LCB: '{';
RCB: '}';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
ASSIGN: '=';

// Operators:
ADDOP: '+';
MINUSOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
NEGAOP: '!';
CONJOP: '&&';
DISJOP: '||';
EQUALOP: '==';
DIFOP: '!='; 
LESSOP: '<';
LESSEQOP: '<=';
GREATOP: '>';
GREATEQOP: '>=';
CONCAT: '::';

// Keywords
INTEGER: 'integer';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';
ARRAY: 'array';
OF: 'of';
VOID: 'void';
AUTO: 'auto';

INHIRIT: 'inhirit';
OUT: 'out';
FUNCTION: 'function';

IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
DO: 'do';
BREAK: 'break';
CONT: 'continue';
RT: 'return';

// Functions
functions: 	readint_func
		|	readfloat_func
		|	readbool_func
		|	readstr_func
		|	printint_func
		|	printfloat_func
		|	printbool_func
		|	printstr_func
		|	supers
		|	preventdef;

readint_func: READINT LRB RRB;
readfloat_func: READFLOAT LRB RRB;
readbool_func: READBOOL LRB RRB;
readstr_func: READSTR LRB RRB;
printint_func: PRINTINT LRB exp RRB;
printfloat_func: WRITEFLOAT LRB exp RRB;
printbool_func: PRINTBOOL LRB exp RRB;
printstr_func: PRINTSTR LRB exp RRB;
supers: SUPERS LRB expression_list RRB;
preventdef: PREVENTDEF LRB RRB;

READINT:'readInteger';
PRINTINT:'printInteger';
READFLOAT:'readFloat';
WRITEFLOAT:'writeFloat';
READBOOL: 'readBoolean';
PRINTBOOL:'printBoolean';
READSTR: 'readString';
PRINTSTR:'printString';
SUPERS:'super';
PREVENTDEF:'preventDefault';

// ID
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip comments
BLOCK_COMMENT: ('/*' ~[*]* '*/') -> skip ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;

// Skip spaces, tabs, backspaces, form feeds, carriage returns, newlines
WS : [ \t\b\f\r\n]+ -> skip ;

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR*
	{
		y = str(self.text)
		if not y in '"':
			raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};
fragment ESC_ILLEGAL: '\\' ~[n"] | ~'\\' ;