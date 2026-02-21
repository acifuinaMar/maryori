from antlr4 import *
from expresionLexer import expresionLexer
from expresionParser import expresionParser

input_stream = FileStream('entrada.txt', encoding='utf-8')
lexer = expresionLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = expresionParser(token_stream)

tree = parser.root()
print(tree.toStringTree(recog=parser))