import abc


class AbstractVisitor(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def visit_before(self, elem):
        pass

    @abc.abstractclassmethod
    def visit_for_before(self, for_node):
        pass

    @abc.abstractclassmethod
    def visit_compound_statement_before(self, compound_statement):
        pass

    @abc.abstractclassmethod
    def visit_alias_declaration_before(self, alias_declaration):
        pass

    @abc.abstractclassmethod
    def visit_if_before(self, if_node):
        pass

    @abc.abstractclassmethod
    def visit_class_before(self, class_node):
        pass

    @abc.abstractclassmethod
    def visit_enum_before(self, enum_node):
        pass

    @abc.abstractclassmethod
    def visit_ternary_operation_before(self, ternary_operation):
        pass

    @abc.abstractclassmethod
    def visit_binary_operation_before(self, binary_operation):
        pass

    @abc.abstractclassmethod
    def visit_cast_expression_before(self, cast_expression):
        pass

    @abc.abstractclassmethod
    def visit_prefix_unary_before(self, prefix_unary):
        pass

    @abc.abstractclassmethod
    def visit_postfix_unary_before(self, postfix_unary):
        pass

    @abc.abstractclassmethod
    def visit_function_call_before(self, function_call):
        pass

    @abc.abstractclassmethod
    def visit_array_subscription_before(self, array_subscription):
        pass

    @abc.abstractclassmethod
    def visit_member_access_before(self, class_member_access):
        pass

    @abc.abstractclassmethod
    def visit_braced_init_list_before(self, braced_init_list):
        pass

    @abc.abstractclassmethod
    def visit_equal_initializer_before(self, equal_initializer):
        pass

    @abc.abstractclassmethod
    def visit_enclosed_in_paren_before(self, enclosed_in_paren):
        pass

    @abc.abstractclassmethod
    def visit_decl_specifier_seq_before(self, decl_specifier_seq):
        pass

    @abc.abstractclassmethod
    def visit_program_before(self, program):
        pass

    @abc.abstractclassmethod
    def visit_identifier_before(self, identifier_node):
        pass

    @abc.abstractclassmethod
    def visit_enum_key_before(self, enum_key):
        pass

    @abc.abstractclassmethod
    def visit_enum_head_before(self, enum_head):
        pass

    @abc.abstractclassmethod
    def visit_enumerator_before(self, enumerator):
        pass

    @abc.abstractclassmethod
    def visit_enumerator_list_before(self, enumerator_list):
        pass

    @abc.abstractclassmethod
    def visit_init_declarator_before(self, init_declarator):
        pass

    @abc.abstractclassmethod
    def visit_function_declarator_before(self, function_declarator):
        pass

    @abc.abstractclassmethod
    def visit_statement_expression_before(self, statement_expression):
        pass

    @abc.abstractclassmethod
    def visit_array_declaration_before(self, array_declaration):
        pass

    @abc.abstractclassmethod
    def visit_literal_before(self, literal):
        pass

    @abc.abstractclassmethod
    def visit_function_definition_before(self, function_definition):
        pass

    @abc.abstractclassmethod
    def visit_comma_separated_list_before(self, comma_separated_list):
        pass

    @abc.abstractclassmethod
    def visit_assignment_expression_before(self, assignment_expression):
        pass

    @abc.abstractclassmethod
    def visit_while_loop_before(self, while_loop):
        pass

    @abc.abstractclassmethod
    def visit_do_while_loop_before(self, do_while_loop):
        pass

    @abc.abstractclassmethod
    def visit_range_for_loop_before(self, range_for):
        pass

    @abc.abstractclassmethod
    def visit_break_before(self, break_statement):
        pass

    @abc.abstractclassmethod
    def visit_continue_before(self, continue_statement):
        pass

    @abc.abstractclassmethod
    def visit_return_before(self, return_statement):
        pass

    @abc.abstractclassmethod
    def visit_operator_function_before(self, operator_function):
        pass

    @abc.abstractclassmethod
    def visit_sequence_before(self, sequence):
        pass

    @abc.abstractclassmethod
    def visit_simple_type_before(self, simple_type):
        pass

    @abc.abstractclassmethod
    def visit_simple_declaration_before(self, simple_declaration):
        pass

    @abc.abstractclassmethod
    def visit_condition_with_declaration_before(self, condition_with_decl):
        pass

    @abc.abstractclassmethod
    def visit_simple_template_before(self, simple_template):
        pass

    @abc.abstractclassmethod
    def visit_template_argument_before(self, template_argument):
        pass

    @abc.abstractclassmethod
    def visit_type_specifier_sequence_before(self, type_specifier_sequence):
        pass

    @abc.abstractclassmethod
    def visit_qualifiers_and_specifiers_before(self, qualifiers_and_specifiers):
        pass

    @abc.abstractclassmethod
    def visit_after(self, elem):
        pass

    @abc.abstractclassmethod
    def visit_for_after(self, for_node):
        pass

    @abc.abstractclassmethod
    def visit_compound_statement_after(self, compound_statement):
        pass

    @abc.abstractclassmethod
    def visit_alias_declaration_after(self, alias_declaration):
        pass

    @abc.abstractclassmethod
    def visit_if_after(self, if_node):
        pass

    @abc.abstractclassmethod
    def visit_class_after(self, class_node):
        pass

    @abc.abstractclassmethod
    def visit_enum_after(self, enum_node):
        pass

    @abc.abstractclassmethod
    def visit_ternary_operation_after(self, ternary_operation):
        pass

    @abc.abstractclassmethod
    def visit_binary_operation_after(self, binary_operation):
        pass

    @abc.abstractclassmethod
    def visit_cast_expression_after(self, cast_expression):
        pass

    @abc.abstractclassmethod
    def visit_prefix_unary_after(self, prefix_unary):
        pass

    @abc.abstractclassmethod
    def visit_postfix_unary_after(self, postfix_unary):
        pass

    @abc.abstractclassmethod
    def visit_function_call_after(self, function_call):
        pass

    @abc.abstractclassmethod
    def visit_array_subscription_after(self, array_subscription):
        pass

    @abc.abstractclassmethod
    def visit_member_access_after(self, class_member_access):
        pass

    @abc.abstractclassmethod
    def visit_braced_init_list_after(self, braced_init_list):
        pass

    @abc.abstractclassmethod
    def visit_equal_initializer_after(self, equal_initializer):
        pass

    @abc.abstractclassmethod
    def visit_enclosed_in_paren_after(self, enclosed_in_paren):
        pass

    @abc.abstractclassmethod
    def visit_decl_specifier_seq_after(self, decl_specifier_seq):
        pass

    @abc.abstractclassmethod
    def visit_program_after(self, program):
        pass

    @abc.abstractclassmethod
    def visit_identifier_after(self, identifier_node):
        pass

    @abc.abstractclassmethod
    def visit_enum_key_after(self, enum_key):
        pass

    @abc.abstractclassmethod
    def visit_enum_head_after(self, enum_head):
        pass

    @abc.abstractclassmethod
    def visit_enumerator_after(self, enumerator):
        pass

    @abc.abstractclassmethod
    def visit_enumerator_list_after(self, enumerator_list):
        pass

    @abc.abstractclassmethod
    def visit_init_declarator_after(self, init_declarator):
        pass

    @abc.abstractclassmethod
    def visit_function_declarator_after(self, function_declarator):
        pass

    @abc.abstractclassmethod
    def visit_statement_expression_after(self, statement_expression):
        pass

    @abc.abstractclassmethod
    def visit_array_declaration_after(self, array_declaration):
        pass

    @abc.abstractclassmethod
    def visit_literal_after(self, literal):
        pass

    @abc.abstractclassmethod
    def visit_function_definition_after(self, function_definition):
        pass

    @abc.abstractclassmethod
    def visit_comma_separated_list_after(self, comma_separated_list):
        pass

    @abc.abstractclassmethod
    def visit_assignment_expression_after(self, assignment_expression):
        pass

    @abc.abstractclassmethod
    def visit_while_loop_after(self, while_loop):
        pass

    @abc.abstractclassmethod
    def visit_do_while_loop_after(self, do_while_loop):
        pass

    @abc.abstractclassmethod
    def visit_range_for_loop_after(self, range_for):
        pass

    @abc.abstractclassmethod
    def visit_break_after(self, break_statement):
        pass

    @abc.abstractclassmethod
    def visit_continue_after(self, continue_statement):
        pass

    @abc.abstractclassmethod
    def visit_return_after(self, return_statement):
        pass

    @abc.abstractclassmethod
    def visit_operator_function_after(self, operator_function):
        pass

    @abc.abstractclassmethod
    def visit_sequence_after(self, sequence):
        pass

    @abc.abstractclassmethod
    def visit_simple_type_after(self, simple_type):
        pass

    @abc.abstractclassmethod
    def visit_simple_declaration_after(self, simple_declaration):
        pass

    @abc.abstractclassmethod
    def visit_condition_with_declaration_after(self, condition_with_decl):
        pass

    @abc.abstractclassmethod
    def visit_simple_template_after(self, simple_template):
        pass

    @abc.abstractclassmethod
    def visit_template_argument_after(self, template_argument):
        pass

    @abc.abstractclassmethod
    def visit_type_specifier_sequence_after(self, type_specifier_sequence):
        pass

    @abc.abstractclassmethod
    def visit_qualifiers_and_specifiers_after(self, qualifiers_and_specifiers):
        pass

    @abc.abstractclassmethod
    def visit_class_head_before(self, class_head):
        pass

    @abc.abstractclassmethod
    def visit_class_head_after(self, class_head):
        pass

    @abc.abstractclassmethod
    def visit_nested_name_specifier_before(self, nested_name_specifier):
        pass

    @abc.abstractclassmethod
    def visit_nested_name_specifier_after(self, nested_name_specifier):
        pass

    @abc.abstractclassmethod
    def visit_identifier_check_before(self, identifier_check):
        pass

    @abc.abstractclassmethod
    def visit_identifier_check_after(self, identifier_check):
        pass
