grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (vardecl | funcdecl)+ EOF ;

var_type: INTEGER | FLOAT | BOOL | STRING | VOID;

// Variable declarations
vardecl: vardecl1 | vardecl2;

vardecl1: id_list1 COLON var_type SEMI;
id_list1: ID id_list2 | ;
id_list2: COMMA ID id_list2 | ;

vardecl2: ID vardecl2_2 exp SEMI;
vardecl2_2: COMMA ID vardecl2_2 exp COMMA | (COLON var_type ASSIGN);
// Function declarations
funcdecl: ID COLON FUNCTION var_type paradecl block_stmt ;	
paradecl: LRB para_list1 RRB;
para_list1: para para_list2 | ;
para_list2: COMMA para para_list2 | ;
para: OUT? ID COLON var_type;

stmts_list: stmts | block_stmt | (LCB stmts+ RCB);
stmts:assign_stmt 
	| if_stmt
	| for_stmt
	| while_stmt
	| do_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt;

assign_stmt: assign_lhs ASSIGN exp SEMI;
assign_lhs: (ID | exp_ind);

if_stmt: IF LRB exp RRB stmts_list (ELSE stmts_list)?;

for_stmt: FOR LRB assign_lhs ASSIGN exp COMMA bool_expr COMMA ID exp_airth INTLIT RRB;


while_stmt: WHILE LRB bool_expr RRB stmts | block_stmt;
do_stmt: DO block_stmt WHILE bool_expr SEMI;
bool_expr: ID exp_bool | exp_rela INTLIT;

break_stmt: BREAK SEMI;
continue_stmt: CONT SEMI;
return_stmt: RT exp SEMI;

call_stmt: ID call_body SEMI;
call_stmt_no_semi: ID call_body;
call_body: LRB call_list1 RRB;
call_list1: exp call_list2 | ;
call_list2: COMMA exp call_list2 | ;

block_stmt: LCB block_body RCB;
block_body: (stmts | vardecl)*;

// Expressions

exp_airth: ADDOP | MINUSOP | MULOP | DIVOP | MODOP;
exp_bool: NEGAOP | CONJOP | DISJOP;
exp_str: CONCAT;
exp_rela: EQUALOP | DIFOP | LESSOP | LESSEQOP | GREATOP | GREATEQOP;
exp_ind: ID expression_list1;

exp: exp1 CONCAT exp1 | exp1;
exp1: exp2 (EQUALOP | DIFOP | LESSOP | GREATOP | LESSEQOP | GREATEQOP) exp2 | exp2;
exp2: exp2 (CONJOP | DISJOP) exp3 | exp3;
exp3: exp3 (ADDOP | MINUSOP) exp4 | exp4;
exp4: exp4 (MULOP | DIVOP | MODOP) exp5 | exp5;
exp5: NEGAOP exp5 | exp6;
exp6: MINUSOP exp6 | exp7;
exp7: COMMA exp7 | literals | var_type | ID | call_stmt_no_semi;

// 4. Type system and values

// Literals
literals: INTLIT | FLOATLIT | BOOL | STRINGLIT;

// array: LCB expression_list1 RCB ;
expression_list1: expression expression_list2 | ;
expression_list2: COMMA expression expression_list2 | ;
expression: INTLIT | FLOATLIT | BOOL | STRINGLIT;

INTLIT: [0] | ([1-9][0-9_]*) {self.text = self.text.replace('_','')};
FLOATLIT: INTLIT DECIMAL? EXPONENT? {self.text = self.text.replace('_','')};
fragment DECIMAL: [.] ([0] | ([1-9]([0-9]* [1-9])?));
fragment EXPONENT: [eE] [-+]? [0] | ([1-9][0-9]*);
BOOL: 'true' | 'false';
STRINGLIT: '"' (STR_CHAR)* '"' {self.text = self.text[1:-1]};
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;
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

// ID
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip comments
BLOCK_COMMENT: ('(*' .*? '*)') -> skip ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;

// Skip spaces, tabs, backspaces, form feeds, carriage returns, newlines
WS : [ \t\b\f\r\n]+ -> skip ;

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;