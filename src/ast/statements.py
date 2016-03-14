from .risha_ast import ASTNode


class ForLoop(ASTNode):
    def __init__(self, for_init_statement, condition, expression, statement):
        self.for_init_statement = for_init_statement
        self.condition = condition
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        visitor.visit_for(self)


class CompoundStatement(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        visitor.visit_compound_statement(self)


class IfStatement(ASTNode):
    def __init__(self, condition, statement, else_statement):
        self.condition = condition
        self.statement = statement
        self.else_statement = else_statement

    def accept(self, visitor):
        visitor.visit_if(self)


class StatementExpression(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_expression_statement(self)
