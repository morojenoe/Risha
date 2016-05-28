from ..risha_ast import ASTNode, CommaSeparatedList


class FunctionDefinition(ASTNode):
    def __init__(self, simple_declaration, body):
        self._simple_declaration = simple_declaration
        self._body = body

    def accept_print_visitor(self, visitor):
        visitor.visit_function_definition_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_function_definition_before(self)
        self._simple_declaration.accept_before_after(visitor)
        self._body.accept_before_after(visitor)
        visitor.visit_function_definition_after(self)

    @property
    def simple_declaration(self):
        return self._simple_declaration

    @property
    def body(self):
        return self._body


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
