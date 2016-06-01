from .risha_ast import ASTNode


class Program(ASTNode):
    def __init__(self, declarations=None, num_new_lines_after_decl=2):
        self._declarations = declarations if declarations is not None else []
        self._num_new_lines = num_new_lines_after_decl

    def add(self, declaration):
        self._declarations.append(declaration)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_program_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_program_before(self)
        for declaration in self._declarations:
            declaration.accept_before_after(visitor)
        visitor.visit_program_after(self)

    def get_new_lines(self):
        return self._num_new_lines

    def get_declarations(self):
        for decl in self._declarations:
            yield decl
