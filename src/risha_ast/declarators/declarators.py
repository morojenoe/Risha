from ..risha_ast import ASTNode, Identifier
from ..comma_separated_list import CommaSeparatedList


class InitDeclaratorList(CommaSeparatedList):
    pass


class InitDeclarator(ASTNode):
    def __init__(self, declarator, initializer, row, col):
        super().__init__(row, col)
        self.declarator = declarator
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_init_declarator_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_init_declarator_before(self)
        self.declarator.accept_before_after(visitor)
        if self.initializer is not None:
            self.initializer.accept_before_after(visitor)
        visitor.visit_init_declarator_after(self)


class FunctionDeclarator(ASTNode):
    def __init__(self, function_name, parameters, row, col):
        super().__init__(row, col)
        self._function_name = function_name
        self._parameters = parameters

    def accept_print_visitor(self, visitor):
        visitor.visit_function_declarator_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_function_declarator_before(self)
        if self._function_name is not None:
            self._function_name.accept_before_after(visitor)
        self._parameters.accept_before_after(visitor)
        visitor.visit_function_declarator_after(self)

    @property
    def function_name(self):
        return self._function_name

    @property
    def parameters_for_printing(self):
        return self._parameters

    @property
    def parameters(self):
        return self._parameters.expression

    @function_name.setter
    def function_name(self, value):
        if isinstance(value, str):
            self._function_name = Identifier(value)
        else:
            self._function_name = value


class ArrayDeclarator(ASTNode):
    def __init__(self, array_name, row, col):
        super().__init__(row, col)
        self.array_name = array_name
        self.parameters = []

    def add_parameter(self, parameter):
        self.parameters.append(parameter)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_array_declaration_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_array_declaration_before(self)
        if self.array_name is not None:
            self.array_name.accept_before_after(visitor)
        for parameter in self.parameters:
            parameter.accept_before_after(visitor)
        visitor.visit_array_declaration_after(self)


class QualifiersAndSpecifiers(ASTNode):
    def __init__(self, name, row, col):
        super().__init__(row, col)
        self.name = name

    def accept_print_visitor(self, visitor):
        visitor.visit_qualifiers_and_specifiers_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_qualifiers_and_specifiers_before(self)
        visitor.visit_qualifiers_and_specifiers_after(self)


class RefQualifier(QualifiersAndSpecifiers):
    pass


class ConstQualifier(QualifiersAndSpecifiers):
    pass


class StorageSpecifier(QualifiersAndSpecifiers):
    pass
