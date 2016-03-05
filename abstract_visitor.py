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
