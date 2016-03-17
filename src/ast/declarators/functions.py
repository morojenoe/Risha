from ..risha_ast import ASTNode, CommaSeparatedList


class FunctionDefinition(ASTNode):
    def __init__(self, declarator_with_specifiers, body):
        self.declarator_with_specifiers = declarator_with_specifiers
        self.body = body

    def accept(self, visitor):
        visitor.visit_function_definition(self)


class ParameterDeclarationList(CommaSeparatedList):
    pass


class ParameterDeclaration(ASTNode):
    def __init__(self, declarator_with_specifiers, initializer):
        self.declarator_with_specifiers = declarator_with_specifiers
        self.initializer = initializer

    def accept(self, visitor):
        visitor.visit_param_decl(self)
