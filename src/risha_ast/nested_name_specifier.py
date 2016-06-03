from .sequence import Sequence


class NestedNameSpecifier(Sequence):
    def accept_print_visitor(self, visitor):
        visitor.visit_nested_name_specifier_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_nested_name_specifier_before(self)
        for element in self.elements:
            element.accept_before_after(visitor)
        visitor.visit_nested_name_specifier_after(self)
