from ..risha_ast import ASTNode, CommaSeparatedList


class FunctionDefinition(ASTNode):
    def __init__(self, return_type, function_head, body):
        self._return_type = return_type
        self._function_head = function_head
        self._body = body

    def accept_print_visitor(self, visitor):
        visitor.visit_function_definition_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_function_definition_before(self)
        if self._return_type is not None:
            self._return_type.accept_before_after(visitor)
        self._function_head.accept_before_after(visitor)
        if self._body is not None:
            self._body.accept_before_after(visitor)
        visitor.visit_function_definition_after(self)

    def remove_body(self):
        self._body = None
        return self

    @property
    def return_type(self):
        return self._return_type

    @property
    def function_head(self):
        return self._function_head

    @property
    def body(self):
        return self._body

    @property
    def name_as_string(self):
        return self._function_head.function_name.as_string()

    @name_as_string.setter
    def name_as_string(self, value):
        self._function_head.function_name = value

    @property
    def name(self):
        return self._function_head.function_name

    @name.setter
    def name(self, func_name):
        self._function_head.function_name = func_name


class ParameterDeclarationList(CommaSeparatedList):
    pass
