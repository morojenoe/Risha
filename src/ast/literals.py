from .risha_ast import ASTNode


class BooleanLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit_boolean_literal(self)


class IntegerLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit_integer_literal(self)


class CharacterLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit_character_literal(self)


class StringLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit_string_literal(self)


class FloatingNumberLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit_floating_literal(self)
