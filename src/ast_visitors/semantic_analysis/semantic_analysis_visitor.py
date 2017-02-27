from .scope_table import ScopeTable
from .tools import make_function, make_variables, make_variable_from_enumerator
from ..abstract_visitor import AbstractVisitor
from .analysis_state import IdentifierCheckState


class SemanticAnalysisVisitor(AbstractVisitor):
    def __init__(self):
        self._scope_table = ScopeTable()
        self._scope_table.enter_scope()
        self._errors = []
        self._state = {
            'identifier_check': []
        }

    def _enter_new_scope(self):
        self._scope_table.enter_scope()

    def _exit_scope(self):
        self._scope_table.exit_scope()

    def _add_error(self, message):
        self._errors.append(message)

    def get_errors(self):
        return self._errors

    def visit_nested_name_specifier_after(self, nested_name_specifier):
        pass

    def visit_postfix_unary_before(self, postfix_unary):
        pass

    def visit_enum_before(self, enum_node):
        self._state['enum_name'] = enum_node.identifier

    def visit_prefix_unary_after(self, prefix_unary):
        pass

    def visit_ternary_operation_before(self, ternary_operation):
        pass

    def visit_qualifiers_and_specifiers_after(self, qualifiers_and_specifiers):
        pass

    def visit_postfix_unary_after(self, postfix_unary):
        pass

    def visit_template_argument_before(self, template_argument):
        pass

    def visit_member_access_after(self, class_member_access):
        pass

    def visit_continue_before(self, continue_statement):
        pass

    def visit_range_for_loop_before(self, range_for):
        pass

    def visit_do_while_loop_after(self, do_while_loop):
        pass

    def visit_class_head_after(self, class_head):
        pass

    def visit_cast_expression_after(self, cast_expression):
        pass

    def visit_decl_specifier_seq_after(self, decl_specifier_seq):
        pass

    def visit_equal_initializer_before(self, equal_initializer):
        pass

    def visit_function_definition_before(self, function_definition):
        function = make_function(function_definition)
        self._scope_table.insert_function(function)
        self._enter_new_scope()

    def visit_braced_init_list_after(self, braced_init_list):
        pass

    def visit_nested_name_specifier_before(self, nested_name_specifier):
        pass

    def visit_enum_after(self, enum_node):
        del self._state['enum_name']

    def visit_simple_type_after(self, simple_type):
        pass

    def visit_identifier_after(self, identifier_node):
        pass

    def visit_enumerator_list_before(self, enumerator_list):
        pass

    def visit_compound_statement_before(self, compound_statement):
        self._enter_new_scope()

    def visit_comma_separated_list_after(self, comma_separated_list):
        pass

    def visit_enclosed_in_paren_before(self, enclosed_in_paren):
        pass

    def visit_alias_declaration_after(self, alias_declaration):
        pass

    def visit_before(self, elem):
        pass

    def visit_function_declarator_after(self, function_declarator):
        self._state['identifier_check'].pop()

    def visit_template_argument_after(self, template_argument):
        pass

    def visit_simple_declaration_before(self, simple_declaration):
        self._state['identifier_check'].append(
            IdentifierCheckState.NO_NEED_TO_CHECK_IDENTIFIER)

    def visit_member_access_before(self, class_member_access):
        pass

    def visit_range_for_loop_after(self, range_for):
        pass

    def visit_enumerator_list_after(self, enumerator_list):
        pass

    def visit_compound_statement_after(self, compound_statement):
        self._exit_scope()

    def visit_continue_after(self, continue_statement):
        pass

    def visit_operator_function_before(self, operator_function):
        pass

    def visit_statement_expression_after(self, statement_expression):
        pass

    def visit_condition_with_declaration_after(self, condition_with_decl):
        pass

    def visit_while_loop_after(self, while_loop):
        pass

    def visit_braced_init_list_before(self, braced_init_list):
        pass

    def visit_after(self, elem):
        pass

    def visit_simple_template_after(self, simple_template):
        pass

    def visit_function_definition_after(self, function_definition):
        self._exit_scope()

    def visit_enum_key_after(self, enum_key):
        pass

    def visit_ternary_operation_after(self, ternary_operation):
        pass

    def visit_array_subscription_after(self, array_subscription):
        pass

    def visit_sequence_before(self, sequence):
        pass

    def visit_assignment_expression_after(self, assignment_expression):
        pass

    def visit_simple_template_before(self, simple_template):
        pass

    def visit_decl_specifier_seq_before(self, decl_specifier_seq):
        pass

    def visit_enumerator_before(self, enumerator):
        pass

    def visit_for_before(self, for_node):
        pass

    def visit_for_after(self, for_node):
        pass

    def visit_type_specifier_sequence_after(self, type_specifier_sequence):
        pass

    def visit_array_subscription_before(self, array_subscription):
        pass

    def visit_enclosed_in_paren_after(self, enclosed_in_paren):
        pass

    def visit_simple_declaration_after(self, simple_declaration):
        self._state['identifier_check'].pop()
        variables = make_variables(simple_declaration)
        for variable in variables:
            self._scope_table.insert_variable(variable)

    def visit_enum_head_after(self, enum_head):
        self._state['identifier_check'].pop()

    def visit_class_before(self, class_node):
        pass

    def visit_identifier_before(self, identifier_node):
        if (len(self._state['identifier_check']) == 0 or
                    self._state['identifier_check'][-1] ==
                    IdentifierCheckState.NEED_TO_CHECK_IDENTIFIER):
            variable = self._scope_table.lookup_variable(
                identifier_node.identifier)
            if variable is None:
                self._add_error('\'{}\' was not declared in this scope'.format(
                    identifier_node.identifier))

    def visit_equal_initializer_after(self, equal_initializer):
        pass

    def visit_init_declarator_after(self, init_declarator):
        pass

    def visit_type_specifier_sequence_before(self, type_specifier_sequence):
        pass

    def visit_enum_head_before(self, enum_head):
        self._state['identifier_check'].append(
            IdentifierCheckState.NO_NEED_TO_CHECK_IDENTIFIER)

    def visit_function_call_before(self, function_call):
        pass

    def visit_class_head_before(self, class_head):
        pass

    def visit_statement_expression_before(self, statement_expression):
        pass

    def visit_if_before(self, if_node):
        pass

    def visit_qualifiers_and_specifiers_before(self, qualifiers_and_specifiers):
        pass

    def visit_function_declarator_before(self, function_declarator):
        self._state['identifier_check'].append(
            IdentifierCheckState.NO_NEED_TO_CHECK_IDENTIFIER)

    def visit_cast_expression_before(self, cast_expression):
        pass

    def visit_array_declaration_before(self, array_declaration):
        pass

    def visit_assignment_expression_before(self, assignment_expression):
        pass

    def visit_if_after(self, if_node):
        pass

    def visit_literal_after(self, literal):
        pass

    def visit_simple_type_before(self, simple_type):
        pass

    def visit_program_after(self, program):
        pass

    def visit_literal_before(self, literal):
        pass

    def visit_while_loop_before(self, while_loop):
        pass

    def visit_init_declarator_before(self, init_declarator):
        pass

    def visit_operator_function_after(self, operator_function):
        pass

    def visit_return_after(self, return_statement):
        pass

    def visit_break_after(self, break_statement):
        pass

    def visit_enumerator_after(self, enumerator):
        variable = make_variable_from_enumerator(enumerator,
                                                 self._state['enum_name'])
        self._scope_table.insert_variable(variable)

    def visit_break_before(self, break_statement):
        pass

    def visit_array_declaration_after(self, array_declaration):
        pass

    def visit_function_call_after(self, function_call):
        pass

    def visit_return_before(self, return_statement):
        pass

    def visit_binary_operation_before(self, binary_operation):
        pass

    def visit_class_after(self, class_node):
        pass

    def visit_prefix_unary_before(self, prefix_unary):
        pass

    def visit_condition_with_declaration_before(self, condition_with_decl):
        pass

    def visit_do_while_loop_before(self, do_while_loop):
        pass

    def visit_program_before(self, program):
        pass

    def visit_comma_separated_list_before(self, comma_separated_list):
        pass

    def visit_alias_declaration_before(self, alias_declaration):
        pass

    def visit_enum_key_before(self, enum_key):
        pass

    def visit_sequence_after(self, sequence):
        pass

    def visit_binary_operation_after(self, binary_operation):
        pass

    def visit_identifier_check_after(self, identifier_check):
        self._state['identifier_check'].pop()

    def visit_identifier_check_before(self, identifier_check):
        self._state['identifier_check'].append(
            IdentifierCheckState.NEED_TO_CHECK_IDENTIFIER)
