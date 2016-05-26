from . import ASTNode


class Program(ASTNode):
    def __init__(self, declarations=None):
        self.declarations = declarations if declarations is not None else []

    def add(self, declaration):
        self.declarations.append(declaration)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_program_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_program_before(self)
        for declaration in self.declarations:
            declaration.accept_before_after(visitor)
        visitor.visit_program_after(self)
