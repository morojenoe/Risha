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

    @abc.abstractclassmethod
    def visit_prefix_unary(self, prefix_unary):
        pass

    @abc.abstractclassmethod
    def visit_postfix_unary(self, postfix_unary):
        pass

    @abc.abstractclassmethod
    def visit_function_call(self, function_call):
        pass

    @abc.abstractclassmethod
    def visit_array_subscription(self, array_subscription):
        pass

    @abc.abstractclassmethod
    def visit_member_access(self, class_member_access):
        pass

    @abc.abstractclassmethod
    def visit_initializer_list(self, initializer_list):
        pass

    @abc.abstractclassmethod
    def visit_braced_init_list(self, braced_init_list):
        pass

    @abc.abstractclassmethod
    def visit_equal_initializer(self, equal_initializer):
        pass

    @abc.abstractclassmethod
    def visit_enclosed_in_paren(self, enclosed_in_paren):
        pass

    @abc.abstractclassmethod
    def visit_decl_specifier_seq(self, decl_specifier_seq):
        pass

    @abc.abstractclassmethod
    def visit_program(self, program):
        pass

