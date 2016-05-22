from .risha_ast import ASTNode, Sequence


class ForLoop(ASTNode):
    def __init__(self, for_init_statement, condition, expression, statement):
        self.for_init_statement = for_init_statement
        self.condition = condition
        self.expression = expression
        self.statement = statement

    def accept_print_visitor(self, visitor):
        visitor.visit_for_before(self)


class StatementSequence(Sequence):
    pass


class CompoundStatement(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def accept_print_visitor(self, visitor):
        visitor.visit_compound_statement_before(self)


class IfStatement(ASTNode):
    def __init__(self, condition, statement, else_statement):
        self.condition = condition
        self.statement = statement
        self.else_statement = else_statement

    def accept_print_visitor(self, visitor):
        visitor.visit_if_before(self)


class StatementExpression(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_statement_expression_before(self)


class WhileLoop(ASTNode):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement

    def accept_print_visitor(self, visitor):
        visitor.visit_while_loop_before(self)


class DoWhileLoop(ASTNode):
    def __init__(self, statement, expression):
        self.statement = statement
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_do_while_loop_before(self)


class RangeForLoop(ASTNode):
    def __init__(self, declaration, initializer, statement):
        self.declaration = declaration
        self.initializer = initializer
        self.statement = statement

    def accept_print_visitor(self, visitor):
        visitor.visit_range_for_loop_before(self)


class BreakStatement(ASTNode):
    def accept_print_visitor(self, visitor):
        visitor.visit_break_before(self)


class ContinueStatement(ASTNode):
    def accept_print_visitor(self, visitor):
        visitor.visit_continue_before(self)


class ReturnStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_return_before(self)
