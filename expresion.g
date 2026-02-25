grammar expresion;

root : expr+ EOF ;

// Escritura de una gramática
expr
    : PAI expr PAD
    | expr (MUL | DIV) expr
    | expr (SUM | RES) expr
    | expr (IGUAL | NOIGUAL) expr
    | expr (MAYOR | MENOR | MENORI | MAYORI) expr
    | expr AND expr
    | expr OR expr
    | NOT expr
    | NUM
    | ID
    ;

// Operadores aritmeticos
SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;

PAI : '(' ;
PAD : ')' ;

// Operadores relacionales
IGUAL   : '==' ;
NOIGUAL : '!=' ;
MENOR   : '<' ;
MAYOR   : '>' ;
MENORI  : '<=' ;
MAYORI  : '>=' ;

// Operadores logicos
AND : '&&' ;
OR  : '||' ;
NOT : '!' ;

// Tokens
NUM : [0-9]+ ;
ID  : [a-zA-Z][a-zA-Z0-9]* ;

// Espacios en blanco
WS : [ \n\t\r]+ -> skip ;
