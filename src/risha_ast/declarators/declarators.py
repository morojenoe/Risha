from ..risha_ast import ASTNode, CommaSeparatedList


class InitDeclaratorList(CommaSeparatedList):
    pass


class InitDeclarator(ASTNode):
    def __init__(self, declarator, initializer):
        self.declarator = declarator
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_init_declarator_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_init_declarator_before(self)
        self.declarator.accept_print_visitor(visitor)
        if self.initializer is not None:
            self.initializer.accept_print_visitor(visitor)
        visitor.visit_init_declarator_after(self)


class FunctionDeclarator(ASTNode):
    def __init__(self, function_name, parameters):
        self.function_name = function_name
        self.parameters = parameters

    def accept_print_visitor(self, visitor):
        visitor.visit_function_declarator_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_function_declarator_before(self)
        if self.function_name is not None:
            self.function_name.accept_print_visitor(visitor)
        self.parameters.accept_print_visitor(visitor)
        visitor.visit_function_declarator_after(self)


class ArrayDeclarator(ASTNode):
    def __init__(self, array_name):
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
            self.array_name.accept_print_visitor(visitor)
        for parameter in self.parameters:
            parameter.accept_print_visitor(visitor)
        visitor.visit_array_declaration_after(self)


class QualifiersAndSpecifiers(ASTNode):
    def __init__(self, name):
        self.name = name

    def accept_print_visitor(self, visitor):
        visitor.visit_qualifiers_and_specifiers_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_qualifiers_and_specifiers_before(self)
        visitor.visit_qualifiers_and_specifiers_after(self)


class RefQualifier(QualifiersAndSpecifiers):
    pass
