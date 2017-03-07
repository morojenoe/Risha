from .risha_ast import ASTNode


class Literal(ASTNode):
    def __init__(self, value, row, col):
        super().__init__(row, col)
        self.value = value

    def accept_print_visitor(self, visitor):
        visitor.visit_literal_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_literal_before(self)
        visitor.visit_literal_after(self)


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
