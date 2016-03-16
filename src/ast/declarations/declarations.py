from ..risha_ast import ASTNode, Sequence


class DeclSpecifierSeq(ASTNode):
    def __init__(self):
        self.decl_specifiers = []

    def add_decl_specifier(self, decl_specifier):
        self.decl_specifiers.append(decl_specifier)
        return self

    def accept(self, visitor):
        visitor.visit_decl_specifier_seq(self)


class TypeSpecifierSequence(Sequence):
    pass


class TrailingTypeSpecifierSequence(Sequence):
    pass


class SimpleDeclaration(ASTNode):
    def __init__(self, specifiers, list_of_declarators):
        self.specifiers = specifiers
        self.list_of_declarators = list_of_declarators

    def accept(self, visitor):
        visitor.visit_simple_declaration(self)
