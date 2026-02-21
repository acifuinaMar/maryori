# Generated from expresion.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .expresionParser import expresionParser
else:
    from expresionParser import expresionParser

# This class defines a complete generic visitor for a parse tree produced by expresionParser.

class expresionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by expresionParser#root.
    def visitRoot(self, ctx:expresionParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expresionParser#expr.
    def visitExpr(self, ctx:expresionParser.ExprContext):
        return self.visitChildren(ctx)



del expresionParser