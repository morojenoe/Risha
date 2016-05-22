from .risha_ast import ASTNode, CommaSeparatedList


class TemplateArgumentList(CommaSeparatedList):
    pass


class TemplateArgument(ASTNode):
    def __init__(self, argument):
        self.argument = argument

    def accept_print_visitor(self, visitor):
        visitor.visit_template_argument_before(self)


class SimpleTemplate(ASTNode):
    def __init__(self, template_name, template_argument_list):
        self.template_name = template_name
        self.template_argument_list = template_argument_list

    def accept_print_visitor(self, visitor):
        visitor.visit_simple_template_before(self)
