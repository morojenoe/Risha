from ..risha_ast import ASTNode


class InitializerList(ASTNode):
    def __init__(self):
        self.initializer_clauses = []

    def add_clause(self, clause):
        self.initializer_clauses.append(clause)
        return self

    def accept(self, visitor):
        visitor.visit_initializer_list(self)


class BracedInitializerList(ASTNode):
    def __init__(self, initializer_list):
        self.initializer_list = initializer_list

    def accept(self, visitor):
        visitor.visit_braced_init_list(self)


class EqualInitializer(ASTNode):
    def __init__(self, initializer_clause):
        self.initializer_clause = initializer_clause

    def accept(self, visitor):
        visitor.visit_equal_initializer(self)