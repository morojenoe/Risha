from ..risha_ast import ASTNode
from ..comma_separated_list import CommaSeparatedList


class InitializerList(CommaSeparatedList):
    pass


class BracedInitializerList(ASTNode):
    def __init__(self, initializer_list):
        self.initializer_list = initializer_list

    def accept_print_visitor(self, visitor):
        visitor.visit_braced_init_list_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_braced_init_list_before(self)
        self.initializer_list.accept_before_after(visitor)
        visitor.visit_braced_init_list_after(self)


class EqualInitializer(ASTNode):
    def __init__(self, initializer_clause):
        self.initializer_clause = initializer_clause

    def accept_print_visitor(self, visitor):
        visitor.visit_equal_initializer_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_equal_initializer_before(self)
        self.initializer_clause.accept_before_after(visitor)
        visitor.visit_equal_initializer_after(self)
