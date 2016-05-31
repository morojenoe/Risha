from ..risha_ast import ASTNode, CommaSeparatedList


class FunctionDefinition(ASTNode):
    def __init__(self, simple_declaration, body):
        self._function_head = simple_declaration
        self._body = body

    def accept_print_visitor(self, visitor):
        visitor.visit_function_definition_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_function_definition_before(self)
        self._function_head.accept_before_after(visitor)
        self._body.accept_before_after(visitor)
        visitor.visit_function_definition_after(self)

    @property
    def function_head(self):
        return self._function_head

    @property
    def body(self):
        return self._body


class ParameterDeclarationList(CommaSeparatedList):
    pass
