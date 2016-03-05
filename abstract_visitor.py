import abc


class AbstractVisitor(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def visit(self, elem):
        pass

    @abc.abstractclassmethod
    def visit_for(self, for_node):
        pass

    @abc.abstractclassmethod
    def visit_compound_statement(self, compound_statement):
        pass

    @abc.abstractclassmethod
    def visit_alias_declaration(self, alias_declaration):
        pass

    @abc.abstractclassmethod
    def visit_if(self, if_node):
        pass

    @abc.abstractclassmethod
    def visit_class(self, class_node):
        pass

    @abc.abstractclassmethod
    def visit_enum(self, enum_node):
        pass

    @abc.abstractclassmethod
    def visit_ternary_operation(self, ternary_operation):
        pass

    @abc.abstractclassmethod
    def visit_binary_operation(self, binary_operation):
        pass

    @abc.abstractclassmethod
    def visit_cast_expression(self, cast_expression):
        pass

    @abc.abstractclassmethod
    def visit_expression(self, expression_node):
        pass
