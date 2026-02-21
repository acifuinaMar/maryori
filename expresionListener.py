# Generated from expresion.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .expresionParser import expresionParser
else:
    from expresionParser import expresionParser

# This class defines a complete listener for a parse tree produced by expresionParser.
class expresionListener(ParseTreeListener):

    # Enter a parse tree produced by expresionParser#root.
    def enterRoot(self, ctx:expresionParser.RootContext):
        pass

    # Exit a parse tree produced by expresionParser#root.
    def exitRoot(self, ctx:expresionParser.RootContext):
        pass


    # Enter a parse tree produced by expresionParser#expr.
    def enterExpr(self, ctx:expresionParser.ExprContext):
        pass

    # Exit a parse tree produced by expresionParser#expr.
    def exitExpr(self, ctx:expresionParser.ExprContext):
        pass



del expresionParser