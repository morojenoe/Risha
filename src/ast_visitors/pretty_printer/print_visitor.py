from ..abstract_visitor import AbstractVisitor


class PrintVisitor(AbstractVisitor):
    def __init__(self, output, inc_indentation=2):
        self.output = output
        self.indentation = [0]
        self.inc_indentation = inc_indentation
        self.ref_qualifier = False

    def _print_semicolon(self):
        self._print(';')

    def _print_spaces(self, num=1):
        self._print(' ' * num)

    def _new_level_indentation(self, value=None):
        if value is None:
            value = self.indentation[-1] + self.inc_indentation
        self.indentation.append(value)

    def _pop_indentation(self):
        self.indentation.pop()

    def _print_indentation(self, current=True):
        if current:
            self._print_spaces(self.indentation[-1])
        else:
            self._print_spaces(self.indentation[-1] - self.inc_indentation)

    def _print(self, text, indentation=False):
        if indentation:
            self._print_indentation()
        print(text, file=self.output, end='')

    def visit_compound_statement_before(self, compound_statement):
        if compound_statement.statements is None:
            self._print('{}')
            return
        self._print_spaces()
        self._print('{')
        self._print_new_line()
        compound_statement.statements.accept_print_visitor(self)
        self._print_indentation(False)
        self._print('}')

    def _print_new_line(self):
        print('\n', file=self.output, end='')

    def visit_before(self, elem):
        self._print(elem, True)
        self._print_spaces()

    def visit_for_before(self, for_node):
        self._print('for (', True)
        self._new_level_indentation(0)
        for_node.for_init_statement.accept_print_visitor(self)
        self._print_spaces()
        if for_node.condition is not None:
            for_node.condition.accept_print_visitor(self)
        else:
            self._print_spaces()
        self._print_semicolon()
        self._print_spaces()
        if for_node.expression is not None:
            for_node.expression.accept_print_visitor(self)
        else:
            self._print_spaces()
        self._pop_indentation()
        self._print(')')
        self._new_level_indentation()
        for_node.statement.accept_print_visitor(self)
        self._pop_indentation()

    def visit_alias_declaration_before(self, alias_declaration):
        self._print('using ', True)
        self._new_level_indentation(0)
        alias_declaration.identifier.accept_print_visitor(self)
        self._pop_indentation()
        self._print(' = ')
        alias_declaration.type_id.accept_print_visitor(self)
        self._print_semicolon()

    def visit_if_before(self, if_node):
        self._print('if (', True)
        self._new_level_indentation(0)
        if_node.condition.accept_print_visitor(self)
        self._pop_indentation()
        self._print(')')
        self._new_level_indentation()
        if_node.statement.accept_print_visitor(self)
        self._pop_indentation()
        if if_node.else_statement is not None:
            self._print_spaces()
            self._print('else')
            self._new_level_indentation()
            if_node.else_statement.accept_print_visitor(self)
            self._pop_indentation()

    def visit_class_before(self, class_node):
        class_node.class_head.accept_print_visitor(self)
        self._print(' {')
        self._print_new_line()
        self._new_level_indentation()
        class_node.member_specification.accept_print_visitor(self)
        self._pop_indentation()
        self._print('}', True)

    def visit_enum_before(self, enum_node):
        enum_node.enum_head.accept_print_visitor(self)
        self._print(' {')
        self._print_new_line()
        self._new_level_indentation()
        enum_node.enumerators.accept_print_visitor(self)
        self._pop_indentation()
        self._print_new_line()
        self._print('}', True)

    def visit_ternary_operation_before(self, ternary_operation):
        ternary_operation.logical_expression.accept_print_visitor(self)
        self._print('? ')
        ternary_operation.true_expression.accept_print_visitor(self)
        self._print(' : ')
        ternary_operation.false_expression.accept_print_visitor(self)

    def visit_binary_operation_before(self, binary_operation):
        binary_operation.left_expression.accept_print_visitor(self)
        self._print(' {0} '.format(binary_operation.operation))
        binary_operation.right_expression.accept_print_visitor(self)

    def visit_cast_expression_before(self, cast_expression):
        self._print('(')
        cast_expression.new_type.accept_print_visitor(self)
        self._print(')')
        cast_expression.cast_expression.accept_print_visitor(self)

    def visit_prefix_unary_before(self, prefix_unary):
        self._print(prefix_unary.operator)
        prefix_unary.expression.accept_print_visitor(self)

    def visit_postfix_unary_before(self, postfix_unary):
        postfix_unary.expression.accept_print_visitor(self)
        self._print(postfix_unary.operator)

    def visit_function_call_before(self, function_call):
        function_call.function.accept_print_visitor(self)
        self._print('(')
        self._new_level_indentation(0)
        function_call.parameters.accept_print_visitor(self)
        self._pop_indentation()
        self._print(')')

    def visit_array_subscription_before(self, array_subscription):
        array_subscription.array_expression.accept_print_visitor(self)
        self._print('[')
        array_subscription.subscript_expression.accept_print_visitor(self)
        self._print(']')

    def visit_member_access_before(self, class_member_access):
        class_member_access.object_expression.accept_print_visitor(self)
        self._print('.')
        self._new_level_indentation(0)
        class_member_access.member_expression.accept_print_visitor(self)
        self._pop_indentation()

    def visit_braced_init_list_before(self, braced_init_list):
        self._print('{')
        self._new_level_indentation(0)
        braced_init_list.initializer_list.accept_print_visitor(self)
        self._pop_indentation()
        self._print('}')

    def visit_equal_initializer_before(self, equal_initializer):
        self._print(' = ')
        equal_initializer.initializer_clause.accept_print_visitor(self)

    def visit_enclosed_in_paren_before(self, enclosed_in_paren):
        self._print('(')
        self._new_level_indentation(0)
        enclosed_in_paren.expression.accept_print_visitor(self)
        self._pop_indentation()
        self._print(')')

    def visit_decl_specifier_seq_before(self, decl_specifier_seq):
        for it, decl_specifier in enumerate(decl_specifier_seq.elements):
            if it > 0:
                self._print_spaces()
                self._new_level_indentation(0)
            if isinstance(decl_specifier, str):
                self._print(decl_specifier, True)
            else:
                decl_specifier.accept_print_visitor(self)
            if it > 0:
                self._pop_indentation()

    def visit_program_before(self, program):
        for declaration in program.get_declarations():
            declaration.accept_print_visitor(self)
            for _ in range(program.get_new_lines()):
                self._print_new_line()

    def visit_identifier_before(self, identifier_node):
        # if self.ref_qualifier:
        #     self._print_ampersand()
        self._print(identifier_node.identifier, True)

    def visit_enum_key_before(self, enum_key):
        self._print('enum', True)
        if enum_key.enum_key is not None:
            self._print(' {}'.format(enum_key.enum_key), True)

    def visit_enum_head_before(self, enum_head):
        enum_head.enum_key.accept_print_visitor(self)
        self._print_spaces()
        self._new_level_indentation(0)
        if enum_head.identifier is not None:
            enum_head.identifier.accept_print_visitor(self)
        self._pop_indentation()

    def visit_enumerator_list_before(self, enumerator_list):
        for it, enumerator in enumerate(enumerator_list.enumerators):
            if it > 0:
                self._print(',')
                self._print_new_line()
            enumerator.accept_print_visitor(self)

    def visit_enumerator_before(self, enumerator):
        enumerator.enumerator.accept_print_visitor(self)
        if enumerator.const_expression is not None:
            self._print(' = ')
            enumerator.const_expression.accept_print_visitor(self)

    def visit_init_declarator_before(self, init_declarator):
        if self.ref_qualifier:
            self._print('&', True)
            self._new_level_indentation(0)
            init_declarator.declarator.accept_print_visitor(self)
            self._pop_indentation()
        else:
            init_declarator.declarator.accept_print_visitor(self)
        if init_declarator.initializer is not None:
            self._new_level_indentation(0)
            init_declarator.initializer.accept_print_visitor(self)
            self._pop_indentation()

    def visit_function_declarator_before(self, function_declarator):
        if self.ref_qualifier:
            self._new_level_indentation(0)
            self._print('&')
            self._pop_indentation()
        if function_declarator.function_name is not None:
            function_declarator.function_name.accept_print_visitor(self)
        function_declarator.parameters.accept_print_visitor(self)

    def visit_statement_expression_before(self, statement_expression):
        if statement_expression.expression is not None:
            statement_expression.expression.accept_print_visitor(self)
        self._print_semicolon()

    def visit_array_declaration_before(self, array_declaration):
        if array_declaration.array_name is not None:
            array_declaration.array_name.accept_print_visitor(self)
        for parameter in array_declaration.parameters:
            self._print('[')
            self._new_level_indentation(0)
            parameter.accept_print_visitor(self)
            self._pop_indentation()
            self._print(']')

    def visit_literal_before(self, literal):
        self._print(literal.value, True)

    def visit_function_definition_before(self, function_definition):
        function_definition.simple_declaration.accept_print_visitor(self)
        self._new_level_indentation()
        function_definition.body.accept_print_visitor(self)
        self._pop_indentation()

    def visit_comma_separated_list_before(self, comma_separated_list):
        for it, element in enumerate(comma_separated_list.elements):
            if it > 0:
                self._print(', ')
            element.accept_print_visitor(self)

    def visit_member_declarator_before(self, member_declarator):
        if self.ref_qualifier:
            self._print('&')
            self._new_level_indentation(0)
            member_declarator.declarator.accept_print_visitor(self)
            self._pop_indentation()
        else:
            member_declarator.declarator.accept_print_visitor(self)
        if member_declarator.initializer is not None:
            member_declarator.initializer.accept_print_visitor(self)

    def visit_assignment_expression_before(self, assignment_expression):
        assignment_expression.expression.accept_print_visitor(self)
        self._print_spaces()
        self._print(assignment_expression.operator)
        self._print_spaces()
        self._new_level_indentation(0)
        assignment_expression.initializer.accept_print_visitor(self)
        self._pop_indentation()

    def visit_while_loop_before(self, while_loop):
        self._print('while (', True)
        self._new_level_indentation(0)
        while_loop.condition.accept_print_visitor(self)
        self._print(')')
        self._pop_indentation()
        self._new_level_indentation()
        while_loop.statement.accept_print_visitor(self)
        self._pop_indentation()

    def visit_do_while_loop_before(self, do_while_loop):
        self._print('do', True)
        self._new_level_indentation()
        do_while_loop.statement.accept_print_visitor(self)
        self._pop_indentation()
        self._print_spaces()
        self._print('while (')
        self._new_level_indentation(0)
        do_while_loop.expression.accept_print_visitor(self)
        self._print(');')
        self._pop_indentation()

    def visit_range_for_loop_before(self, range_for):
        self._print('for (', True)
        self._new_level_indentation(0)
        range_for.declaration.accept_print_visitor(self)
        self._print(' : ')
        range_for.initializer.accept_print_visitor(self)
        self._print(')')
        self._pop_indentation()
        self._new_level_indentation()
        range_for.statement.accept_print_visitor(self)
        self._pop_indentation()

    def visit_break_before(self, break_statement):
        self._print('break;', True)

    def visit_continue_before(self, continue_statement):
        self._print('continue;', True)

    def visit_return_before(self, return_statement):
        self._print('return', True)
        if return_statement.expression is not None:
            self._print_spaces()
            self._new_level_indentation(0)
            return_statement.expression.accept_print_visitor(self)
            self._pop_indentation()
        self._print_semicolon()

    def visit_simple_declaration_before(self, simple_declaration):
        if simple_declaration.specifiers is not None:
            self.ref_qualifier = simple_declaration.specifiers. \
                is_ref_qualifier_present()
            simple_declaration.specifiers.accept_print_visitor(self)
            if simple_declaration.declarators is not None:
                self._print_spaces()
                self._new_level_indentation(0)
                simple_declaration.declarators.accept_print_visitor(self)
                self._pop_indentation()
            self.ref_qualifier = False
        else:
            simple_declaration.declarators.accept_print_visitor(self)
        if simple_declaration.need_a_semicolon:
            self._print_semicolon()

    def visit_operator_function_before(self, operator_function):
        self._print('operator', True)
        self._print(operator_function.operator)

    def visit_sequence_before(self, sequence):
        for elem in sequence.elements:
            elem.accept_print_visitor(self)
            self._print_new_line()

    def visit_simple_type_before(self, simple_type):
        self._print(simple_type.type_name, True)

    def visit_condition_with_declaration_before(self, condition_with_decl):
        condition_with_decl.declarator_with_specifiers.accept_print_visitor(
            self)
        self._new_level_indentation(0)
        condition_with_decl.initializer.accept_print_visitor(self)
        self._pop_indentation()

    def visit_member_declaration_before(self, member_declaration):
        if member_declaration.specifiers is not None:
            member_declaration.specifiers.accept_print_visitor(self)
            self.ref_qualifier = member_declaration.specifiers. \
                is_ref_qualifier_present()
            if member_declaration.declarator_list is not None:
                self._print_spaces()
                self._new_level_indentation(0)
                member_declaration.declarator_list.accept_print_visitor(self)
                self._pop_indentation()
            self.ref_qualifier = False
        elif member_declaration.declarator_list is not None:
            member_declaration.declarator_list.accept_print_visitor(self)
        self._print_semicolon()

    def visit_simple_template_before(self, simple_template):
        simple_template.template_name.accept_print_visitor(self)
        self._print('<')
        self._new_level_indentation(0)
        simple_template.template_argument_list.accept_print_visitor(self)
        self._pop_indentation()
        self._print('>')

    def visit_template_argument_before(self, template_argument):
        template_argument.argument.accept_print_visitor(self)

    def visit_type_specifier_sequence_before(self, type_specifier_sequence):
        for it, elem in enumerate(type_specifier_sequence.elements):
            if it > 0:
                self._print_spaces()
            elem.accept_print_visitor(self)

    def visit_qualifiers_and_specifiers_before(self, qualifiers_and_specifiers):
        self._print(qualifiers_and_specifiers.name, True)

    def visit_class_head_before(self, class_head):
        self._print('struct ', True)
        self._new_level_indentation(0)
        class_head.class_name.accept_print_visitor(self)
        self._pop_indentation()

    def visit_return_after(self, return_statement):
        pass

    def visit_range_for_loop_after(self, range_for):
        pass

    def visit_binary_operation_after(self, binary_operation):
        pass

    def visit_enum_key_after(self, enum_key):
        pass

    def visit_literal_after(self, literal):
        pass

    def visit_for_after(self, for_node):
        pass

    def visit_qualifiers_and_specifiers_after(self, qualifiers_and_specifiers):
        pass

    def visit_enumerator_after(self, enumerator):
        pass

    def visit_statement_expression_after(self, statement_expression):
        pass

    def visit_decl_specifier_seq_after(self, decl_specifier_seq):
        pass

    def visit_enclosed_in_paren_after(self, enclosed_in_paren):
        pass

    def visit_condition_with_declaration_after(self, condition_with_decl):
        pass

    def visit_alias_declaration_after(self, alias_declaration):
        pass

    def visit_simple_type_after(self, simple_type):
        pass

    def visit_member_declaration_after(self, member_declaration):
        pass

    def visit_if_after(self, if_node):
        pass

    def visit_function_declarator_after(self, function_declarator):
        pass

    def visit_operator_function_after(self, operator_function):
        pass

    def visit_break_after(self, break_statement):
        pass

    def visit_sequence_after(self, sequence):
        pass

    def visit_braced_init_list_after(self, braced_init_list):
        pass

    def visit_identifier_after(self, identifier_node):
        pass

    def visit_function_call_after(self, function_call):
        pass

    def visit_postfix_unary_after(self, postfix_unary):
        pass

    def visit_compound_statement_after(self, compound_statement):
        pass

    def visit_member_declarator_after(self, member_declarator):
        pass

    def visit_function_definition_after(self, function_definition):
        pass

    def visit_comma_separated_list_after(self, comma_separated_list):
        pass

    def visit_array_subscription_after(self, array_subscription):
        pass

    def visit_assignment_expression_after(self, assignment_expression):
        pass

    def visit_do_while_loop_after(self, do_while_loop):
        pass

    def visit_enum_head_after(self, enum_head):
        pass

    def visit_ternary_operation_after(self, ternary_operation):
        pass

    def visit_enumerator_list_after(self, enumerator_list):
        pass

    def visit_after(self, elem):
        pass

    def visit_enum_after(self, enum_node):
        pass

    def visit_array_declaration_after(self, array_declaration):
        pass

    def visit_member_access_after(self, class_member_access):
        pass

    def visit_cast_expression_after(self, cast_expression):
        pass

    def visit_type_specifier_sequence_after(self, type_specifier_sequence):
        pass

    def visit_simple_template_after(self, simple_template):
        pass

    def visit_prefix_unary_after(self, prefix_unary):
        pass

    def visit_program_after(self, program):
        pass

    def visit_class_after(self, class_node):
        pass

    def visit_simple_declaration_after(self, simple_declaration):
        pass

    def visit_equal_initializer_after(self, equal_initializer):
        pass

    def visit_while_loop_after(self, while_loop):
        pass

    def visit_template_argument_after(self, template_argument):
        pass

    def visit_continue_after(self, continue_statement):
        pass

    def visit_init_declarator_after(self, init_declarator):
        pass

    def visit_class_head_after(self, class_head):
        pass
