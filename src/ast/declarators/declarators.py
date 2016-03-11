from ..risha_ast import ASTNode


class InitDeclaratorList(ASTNode):
    def __init__(self):
        self.declarators = []

    def add_declarator(self, declarator):
        self.declarators.append(declarator)
        return self

    def accept(self, visitor):
        visitor.visit_init_declarator_list(self)


class InitDeclarator(ASTNode):
    def __init__(self, declarator, initializer):
        self.declarator = declarator
        self.initializer = initializer

    def accept(self, visitor):
        visitor.visit_init_declarator(self)


class FunctionDeclarator(ASTNode):
    def __init__(self, function_name, parameters):
        self.function_name = function_name
        self.parameters = parameters

    def accept(self, visitor):
        visitor.visit_function_declarator(self)
