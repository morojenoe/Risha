from ..risha_ast import ASTNode, Sequence


class DeclSpecifierSeq(Sequence):
    def __init__(self):
        super().__init__()
        self.ref_qualifier = False

    def accept(self, visitor):
        visitor.visit_decl_specifier_seq(self)

    def is_ref_qualifier_present(self):
        return self.ref_qualifier

    def set_ref_qualifier(self):
        self.ref_qualifier = True
        return self


class TypeSpecifierSequence(Sequence):
    def accept(self, visitor):
        visitor.visit_type_specifier_sequence(self)


class TrailingTypeSpecifierSequence(Sequence):
    pass


class SimpleDeclaration(ASTNode):
    def __init__(self, specifiers, list_of_declarators):
        self.specifiers = specifiers
        self.list_of_declarators = list_of_declarators

    def accept(self, visitor):
        visitor.visit_simple_declaration(self)


class ConditionWithDeclaration(ASTNode):
    def __init__(self, declarator_with_specifiers, initializer):
        self.declarator_with_specifiers = declarator_with_specifiers
        self.initializer = initializer

    def accept(self, visitor):
        visitor.visit_condition_with_declaration(self)
