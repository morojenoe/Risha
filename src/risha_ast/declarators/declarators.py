from ..risha_ast import ASTNode, CommaSeparatedList


class InitDeclaratorList(CommaSeparatedList):
    pass


class InitDeclarator(ASTNode):
    def __init__(self, declarator, initializer):
        self.declarator = declarator
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_init_declarator_before(self)


class FunctionDeclarator(ASTNode):
    def __init__(self, function_name, parameters):
        self.function_name = function_name
        self.parameters = parameters

    def accept_print_visitor(self, visitor):
        visitor.visit_function_declarator_before(self)


class ArrayDeclarator(ASTNode):
    def __init__(self, array_name):
        self.array_name = array_name
        self.parameters = []

    def add_parameter(self, parameter):
        self.parameters.append(parameter)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_array_declaration_before(self)


class ParametersAndQualifiers(ASTNode):
    def __init__(self, ):
        pass

    def accept_print_visitor(self, visitor):
        visitor.visit_parameters_and_qualifiers(self)


class QualifiersAndSpecifiers(ASTNode):
    def __init__(self, name):
        self.name = name

    def accept_print_visitor(self, visitor):
        visitor.visit_qualifiers_and_specifiers_before(self)


class RefQualifier(QualifiersAndSpecifiers):
    pass
