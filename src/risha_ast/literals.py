from .risha_ast import ASTNode


class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept_print_visitor(self, visitor):
        visitor.visit_literal_before(self)


class BooleanLiteral(Literal):
    pass


class IntegerLiteral(Literal):
    pass


class CharacterLiteral(Literal):
    pass


class StringLiteral(Literal):
    pass


class FloatingNumberLiteral(Literal):
    pass
