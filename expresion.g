grammar expresion;

root : expr+ EOF ;

// Escritura de una gramática
expr
    : PAI expr PAD
    | expr (MUL | DIV) expr
    | expr (SUM | RES) expr
    | NUM
    ;

// Operadores
SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;
PAI : '(' ;
PAD : ')' ;
NUM : [0-9]+ ;

// Manejo de los espacios en blanco
WS : [ \n\t\r]+ -> skip ;