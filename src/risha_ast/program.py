from .sequence import Sequence


class Program(Sequence):
    def __init__(self, declarations=None, num_new_lines_after_decl=2):
        super().__init__()
        if declarations is not None:
            self.add(declarations)
        self._num_new_lines = num_new_lines_after_decl

    def accept_print_visitor(self, visitor):
        visitor.visit_program_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_program_before(self)
        for declaration in self.elements:
            declaration.accept_before_after(visitor)
        visitor.visit_program_after(self)

    @property
    def number_of_new_lines(self):
        return self._num_new_lines
