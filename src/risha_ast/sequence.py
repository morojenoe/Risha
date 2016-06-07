from .declarators.functions import FunctionDefinition
from .risha_ast import ASTNode


class Sequence(ASTNode):
    def __init__(self):
        self._elements = []
        super().__init__()

    def add(self, element):
        if isinstance(element, list):
            self._elements.extend(element)
        else:
            self._elements.append(element)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_sequence_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_sequence_before(self)
        for element in self._elements:
            element.accept_before_after(visitor)
        visitor.visit_sequence_after(self)

    @property
    def elements(self):
        return self._elements

    def extract_functions(self):
        return filter(lambda elem: isinstance(elem, FunctionDefinition),
                      self._elements)

    def __iter__(self):
        self._index_for_iter = 0
        return self

    def __next__(self):
        if self._index_for_iter < len(self._elements):
            self._index_for_iter += 1
            return self._elements[self._index_for_iter - 1]
        raise StopIteration
