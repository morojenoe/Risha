from .risha_ast import ASTNode
from src.risha_ast import CommaSeparatedList


class TemplateArgumentList(CommaSeparatedList):
    pass


class TemplateArgument(ASTNode):
    def __init__(self, argument):
        self.argument = argument

    def accept_print_visitor(self, visitor):
        visitor.visit_template_argument_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_template_argument_before(self)
        self.argument.accept_before_after(visitor)
        visitor.visit_template_argument_after(self)


class SimpleTemplate(ASTNode):
    def __init__(self, template_name, template_argument_list):
        self.template_name = template_name
        self.template_argument_list = template_argument_list

    def accept_print_visitor(self, visitor):
        visitor.visit_simple_template_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_simple_template_before(self)
        self.template_name.accept_before_after(visitor)
        self.template_argument_list.accept_before_after(visitor)
        visitor.visit_simple_template_after(self)
