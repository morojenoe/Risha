from .sequence import Sequence


class CommaSeparatedList(Sequence):
    def accept_print_visitor(self, visitor):
        visitor.visit_comma_separated_list_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_comma_separated_list_before(self)
        for element in self.elements:
            element.accept_before_after(visitor)
        visitor.visit_comma_separated_list_after(self)
