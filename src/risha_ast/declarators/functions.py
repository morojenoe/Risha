from ..risha_ast import ASTNode, CommaSeparatedList


class FunctionDefinition(ASTNode):
    def __init__(self, function_head, body):
        self._function_head = function_head
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

    @property
    def name_as_string(self):
        return self._function_head.declarators.function_name.as_string()

    @name_as_string.setter
    def name_as_string(self, value):
        self._function_head.declarators.function_name = value

    @property
    def name(self):
        return self._function_head.declarators.function_name

    @name.setter
    def name(self, func_name):
        self._function_head.declarators.function_name = func_name


class ParameterDeclarationList(CommaSeparatedList):
    pass
