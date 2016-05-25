from ..risha_ast import ASTNode, CommaSeparatedList


class FunctionDefinition(ASTNode):
    def __init__(self, declarator_with_specifiers, body):
        self.declarator_with_specifiers = declarator_with_specifiers
        self.body = body

    def accept_print_visitor(self, visitor):
        visitor.visit_function_definition_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_function_definition_before(self)
        self.declarator_with_specifiers.accept_before_after(visitor)
        self.body.accept_before_after(visitor)
        visitor.visit_function_definition_after(self)


class ParameterDeclarationList(CommaSeparatedList):
    pass


class ParameterDeclaration(ASTNode):
    def __init__(self, declarator_with_specifiers, initializer):
        self.declarator_with_specifiers = declarator_with_specifiers
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_param_decl_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_param_decl_before(self)
        self.declarator_with_specifiers.accept_before_after(visitor)
        if self.initializer is not None:
            self.initializer.accept_before_after(visitor)
        visitor.visit_param_decl_after(self)
