# Generated from expresion.g by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,46,2,0,7,0,2,1,7,1,1,0,4,0,6,8,0,11,0,12,0,7,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,41,8,1,10,
        1,12,1,44,9,1,1,1,0,1,2,2,0,2,0,4,1,0,3,4,1,0,1,2,1,0,7,8,1,0,9,
        12,53,0,5,1,0,0,0,2,20,1,0,0,0,4,6,3,2,1,0,5,4,1,0,0,0,6,7,1,0,0,
        0,7,5,1,0,0,0,7,8,1,0,0,0,8,9,1,0,0,0,9,10,5,0,0,1,10,1,1,0,0,0,
        11,12,6,1,-1,0,12,13,5,5,0,0,13,14,3,2,1,0,14,15,5,6,0,0,15,21,1,
        0,0,0,16,17,5,15,0,0,17,21,3,2,1,3,18,21,5,16,0,0,19,21,5,17,0,0,
        20,11,1,0,0,0,20,16,1,0,0,0,20,18,1,0,0,0,20,19,1,0,0,0,21,42,1,
        0,0,0,22,23,10,9,0,0,23,24,7,0,0,0,24,41,3,2,1,10,25,26,10,8,0,0,
        26,27,7,1,0,0,27,41,3,2,1,9,28,29,10,7,0,0,29,30,7,2,0,0,30,41,3,
        2,1,8,31,32,10,6,0,0,32,33,7,3,0,0,33,41,3,2,1,7,34,35,10,5,0,0,
        35,36,5,13,0,0,36,41,3,2,1,6,37,38,10,4,0,0,38,39,5,14,0,0,39,41,
        3,2,1,5,40,22,1,0,0,0,40,25,1,0,0,0,40,28,1,0,0,0,40,31,1,0,0,0,
        40,34,1,0,0,0,40,37,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,
        0,0,0,43,3,1,0,0,0,44,42,1,0,0,0,4,7,20,40,42
    ]

class expresionParser ( Parser ):

    grammarFileName = "expresion.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", 
                     "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "SUM", "RES", "MUL", "DIV", "PAI", "PAD", 
                      "IGUAL", "NOIGUAL", "MENOR", "MAYOR", "MENORI", "MAYORI", 
                      "AND", "OR", "NOT", "NUM", "ID", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    SUM=1
    RES=2
    MUL=3
    DIV=4
    PAI=5
    PAD=6
    IGUAL=7
    NOIGUAL=8
    MENOR=9
    MAYOR=10
    MENORI=11
    MAYORI=12
    AND=13
    OR=14
    NOT=15
    NUM=16
    ID=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(expresionParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.ExprContext)
            else:
                return self.getTypedRuleContext(expresionParser.ExprContext,i)


        def getRuleIndex(self):
            return expresionParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = expresionParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.expr(0)
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 229408) != 0)):
                    break

            self.state = 9
            self.match(expresionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAI(self):
            return self.getToken(expresionParser.PAI, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expresionParser.ExprContext)
            else:
                return self.getTypedRuleContext(expresionParser.ExprContext,i)


        def PAD(self):
            return self.getToken(expresionParser.PAD, 0)

        def NOT(self):
            return self.getToken(expresionParser.NOT, 0)

        def NUM(self):
            return self.getToken(expresionParser.NUM, 0)

        def ID(self):
            return self.getToken(expresionParser.ID, 0)

        def MUL(self):
            return self.getToken(expresionParser.MUL, 0)

        def DIV(self):
            return self.getToken(expresionParser.DIV, 0)

        def SUM(self):
            return self.getToken(expresionParser.SUM, 0)

        def RES(self):
            return self.getToken(expresionParser.RES, 0)

        def IGUAL(self):
            return self.getToken(expresionParser.IGUAL, 0)

        def NOIGUAL(self):
            return self.getToken(expresionParser.NOIGUAL, 0)

        def MAYOR(self):
            return self.getToken(expresionParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(expresionParser.MENOR, 0)

        def MENORI(self):
            return self.getToken(expresionParser.MENORI, 0)

        def MAYORI(self):
            return self.getToken(expresionParser.MAYORI, 0)

        def AND(self):
            return self.getToken(expresionParser.AND, 0)

        def OR(self):
            return self.getToken(expresionParser.OR, 0)

        def getRuleIndex(self):
            return expresionParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = expresionParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 12
                self.match(expresionParser.PAI)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(expresionParser.PAD)
                pass
            elif token in [15]:
                self.state = 16
                self.match(expresionParser.NOT)
                self.state = 17
                self.expr(3)
                pass
            elif token in [16]:
                self.state = 18
                self.match(expresionParser.NUM)
                pass
            elif token in [17]:
                self.state = 19
                self.match(expresionParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 40
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = expresionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 23
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 24
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = expresionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 26
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 27
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = expresionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 29
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = expresionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = expresionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        self.match(expresionParser.AND)
                        self.state = 36
                        self.expr(6)
                        pass

                    elif la_ == 6:
                        localctx = expresionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 38
                        self.match(expresionParser.OR)
                        self.state = 39
                        self.expr(5)
                        pass

             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         




