from .risha_ast import ASTNode
from .sequence import Sequence


class ForLoop(ASTNode):
    def __init__(self, for_init_statement, condition, expression, statement,
                 row, col):
        super().__init__(row, col)
        self.for_init_statement = for_init_statement
        self.condition = condition
        self.expression = expression
        self.statement = statement

    def accept_print_visitor(self, visitor):
        visitor.visit_for_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_for_before(self)
        self.for_init_statement.accept_before_after(visitor)
        if self.condition is not None:
            self.condition.accept_before_after(visitor)
        if self.expression is not None:
            self.expression.accept_before_after(visitor)
        self.statement.accept_before_after(visitor)
        visitor.visit_for_after(self)


class StatementSequence(Sequence):
    pass


class CompoundStatement(ASTNode):
    def __init__(self, statements, row, col):
        super().__init__(row, col)
        self.statements = statements

    def accept_print_visitor(self, visitor):
        visitor.visit_compound_statement_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_compound_statement_before(self)
        if self.statements is not None:
            self.statements.accept_before_after(visitor)
        visitor.visit_compound_statement_after(self)


class IfStatement(ASTNode):
    def __init__(self, condition, statement, else_statement, row, col):
        super().__init__(row, col)
        self.condition = condition
        self.statement = statement
        self.else_statement = else_statement

    def accept_print_visitor(self, visitor):
        visitor.visit_if_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_if_before(self)
        self.condition.accept_before_after(visitor)
        self.statement.accept_before_after(visitor)
        if self.else_statement is not None:
            self.else_statement.accept_before_after(visitor)
        visitor.visit_if_after(self)


class StatementExpression(ASTNode):
    def __init__(self, expression, row, col):
        super().__init__(row, col)
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_statement_expression_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_statement_expression_before(self)
        if self.expression is not None:
            self.expression.accept_before_after(visitor)
        visitor.visit_statement_expression_after(self)


class WhileLoop(ASTNode):
    def __init__(self, condition, statement, row, col):
        super().__init__(row, col)
        self.condition = condition
        self.statement = statement

    def accept_print_visitor(self, visitor):
        visitor.visit_while_loop_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_while_loop_before(self)
        self.condition.accept_before_after(visitor)
        self.statement.accept_before_after(visitor)
        visitor.visit_while_loop_after(self)


class DoWhileLoop(ASTNode):
    def __init__(self, statement, expression, row, col):
        super().__init__(row, col)
        self.statement = statement
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_do_while_loop_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_do_while_loop_before(self)
        self.statement.accept_before_after(visitor)
        self.expression.accept_before_after(visitor)
        visitor.visit_do_while_loop_after(self)


class RangeForLoop(ASTNode):
    def __init__(self, declaration, initializer, statement, row, col):
        super().__init__(row, col)
        self.declaration = declaration
        self.initializer = initializer
        self.statement = statement

    def accept_print_visitor(self, visitor):
        visitor.visit_range_for_loop_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_range_for_loop_before(self)
        self.declaration.accept_before_after(visitor)
        self.initializer.accept_before_after(visitor)
        self.statement.accept_before_after(visitor)
        visitor.visit_range_for_loop_after(self)


class BreakStatement(ASTNode):
    def accept_print_visitor(self, visitor):
        visitor.visit_break_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_break_before(self)
        visitor.visit_break_after(self)


class ContinueStatement(ASTNode):
    def accept_print_visitor(self, visitor):
        visitor.visit_continue_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_continue_before(self)
        visitor.visit_continue_after(self)


class ReturnStatement(ASTNode):
    def __init__(self, expression, row, col):
        super().__init__(row, col)
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_return_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_return_before(self)
        if self.expression is not None:
            self.expression.accept_before_after(visitor)
        visitor.visit_return_after(self)
