from ..risha_ast import ASTNode


class FunctionDefinition(ASTNode):
    def __init__(self, decl_specifiers, declarator, body):
        self.decl_specifiers = decl_specifiers
        self.declarator = declarator
        self.body = body

    def accept(self, visitor):
        visitor.visit_function_definition(self)


class ParameterDeclarationList(ASTNode):
    def __init__(self):
        self.parameters = []

    def add_parameter(self, parameter):
        self.parameters.append(parameter)
        return self

    def accept(self, visitor):
        visitor.visit_param_decl_list(self)


class ParameterDeclaration(ASTNode):
    def __init__(self, decl_specifiers, declarator, initializer):
        self.decl_specifiers = decl_specifiers
        self.declarator = declarator
        self.initializer = initializer

    def accept(self, visitor):
        visitor.visit_param_decl(self)
