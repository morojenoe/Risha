from . import ASTNode, ClassDefinition


class Program(ASTNode):
    def __init__(self, declarations):
        self.declarations = declarations if declarations is not None else []

    def accept_print_visitor(self, visitor):
        visitor.visit_program(self)

    def get_all_classes(self):
        classes = []
        for decl in self.declarations:
            if issubclass(decl, ClassDefinition):
                classes.append(decl)
        return classes
