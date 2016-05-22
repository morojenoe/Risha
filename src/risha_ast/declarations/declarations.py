from ..risha_ast import ASTNode, Sequence


class DeclSpecifierSeq(Sequence):
    def __init__(self):
        super().__init__()
        self.ref_qualifier = False

    def accept_print_visitor(self, visitor):
        visitor.visit_decl_specifier_seq_before(self)

    def is_ref_qualifier_present(self):
        return self.ref_qualifier

    def set_ref_qualifier(self):
        self.ref_qualifier = True
        return self


class TypeSpecifierSequence(Sequence):
    def accept_print_visitor(self, visitor):
        visitor.visit_type_specifier_sequence_before(self)


class TrailingTypeSpecifierSequence(Sequence):
    pass


class SimpleDeclaration(ASTNode):
    def __init__(self, specifiers, list_of_declarators):
        self.specifiers = specifiers
        self.list_of_declarators = list_of_declarators

    def accept_print_visitor(self, visitor):
        visitor.visit_simple_declaration_before(self)


class ConditionWithDeclaration(ASTNode):
    def __init__(self, declarator_with_specifiers, initializer):
        self.declarator_with_specifiers = declarator_with_specifiers
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_condition_with_declaration_before(self)
