from ..risha_ast import ASTNode
from ..sequence import Sequence


class ReferenceQualifier:
    def __init__(self):
        self._reference_qualifier = False

    @property
    def reference_qualifier(self):
        return self._reference_qualifier

    @reference_qualifier.setter
    def reference_qualifier(self, value):
        self._reference_qualifier = value


class DeclSpecifierSeq(Sequence, ReferenceQualifier):
    def accept_print_visitor(self, visitor):
        visitor.visit_decl_specifier_seq_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_decl_specifier_seq_before(self)
        for decl_specifier in self._elements:
            if not isinstance(decl_specifier, str):
                decl_specifier.accept_before_after(visitor)
        visitor.visit_decl_specifier_seq_after(self)


class TypeSpecifierSequence(Sequence, ReferenceQualifier):
    def accept_print_visitor(self, visitor):
        visitor.visit_type_specifier_sequence_before(self)


class TrailingTypeSpecifierSequence(Sequence):
    pass


class SimpleDeclaration(ASTNode):
    def __init__(self, specifiers, declarators, need_a_semicolon=True):
        self._specifiers = specifiers
        self._declarators = declarators
        self._need_a_semicolon = need_a_semicolon

    def accept_print_visitor(self, visitor):
        visitor.visit_simple_declaration_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_simple_declaration_before(self)
        if self._specifiers is not None:
            self._specifiers.accept_before_after(visitor)
        if self._declarators is not None:
            self._declarators.accept_before_after(visitor)
        visitor.visit_simple_declaration_after(self)

    @property
    def specifiers(self):
        return self._specifiers

    @property
    def declarators(self):
        return self._declarators

    @property
    def need_a_semicolon(self):
        return self._need_a_semicolon


class ConditionWithDeclaration(ASTNode):
    def __init__(self, declarator_with_specifiers, initializer):
        self.declarator_with_specifiers = declarator_with_specifiers
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_condition_with_declaration_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_condition_with_declaration_before(self)
        self.declarator_with_specifiers.accept_before_after(visitor)
        self.initializer.accept_before_after(visitor)
        visitor.visit_condition_with_declaration_after(self)
