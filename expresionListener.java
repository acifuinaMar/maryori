// Generated from expresion.g by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link expresionParser}.
 */
public interface expresionListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link expresionParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(expresionParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link expresionParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(expresionParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link expresionParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(expresionParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link expresionParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(expresionParser.ExprContext ctx);
}