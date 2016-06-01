from .risha_ast import ASTNode
from .declarators.functions import FunctionDefinition


class Sequence(ASTNode):
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_sequence_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_sequence_before(self)
        for element in self.elements:
            element.accept_before_after(visitor)
        visitor.visit_sequence_after(self)

    def extract_functions(self):
        return filter(lambda elem: isinstance(elem, FunctionDefinition),
                      self.elements)
