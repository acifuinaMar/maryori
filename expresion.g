grammar expresion;

root : expr+ EOF ;

// Escritura de una gramática
expr
    : PAI expr PAD
    | expr (MUL | DIV) expr
    | expr (SUM | RES) expr
    | NUM
    | expr (IGUAL | NOIGUAL) expr 
    | expr (MAYOR | MENOR) expr 
    | expr (MENORI | MAYORI) expr
    ;

// Operadores aritmeticos
SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;
PAI : '(' ;
PAD : ')' ;
NUM : [0-9]+;

//Operadores relacionales
IGUAL : '=';
NOIGUAL: '!=';
MENOR: '<';
MAYOR: '>';
MENORI: '<=';
MAYORI: '=>';


// Manejo de los espacios en blanco
WS : [ \n\t\r]+ -> skip ;
