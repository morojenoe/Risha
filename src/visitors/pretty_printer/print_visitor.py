from src.visitors import abstract_visitor


class PrintVisitor(abstract_visitor.AbstractVisitor):
    def __init__(self, output, inc_indentation=2):
        self.output = output
        self.indentation = [0]
        self.inc_indentation = inc_indentation
        self.ref_qualifier = False

    def _print_semicolon(self):
        self._print(';')

    def _print_space(self):
        self._print(' ')

    def _new_level_indentation(self, value=None):
        if value is None:
            value = self.indentation[-1] + self.inc_indentation
        self.indentation.append(value)

    def _pop_indentation(self):
        self.indentation.pop()

    def _print_indentation(self, current=True):
        if current:
            print(' ' * self.indentation[-1], file=self.output, end='')
        else:
            print(' ' * (self.indentation[-1] - self.inc_indentation),
                  file=self.output, end='')

    def _print(self, text, indentation=False):
        if indentation:
            self._print_indentation()
        print(text, file=self.output, end='')

    def visit_compound_statement(self, compound_statement):
        if compound_statement.statements is None:
            self._print('{}')
            return

        self._print_space()
        self._print('{')
        self._print_new_line()
        compound_statement.statements.accept(self)
        self._print_indentation(False)
        self._print('}')

    def _print_new_line(self):
        print('\n', file=self.output, end='')

    def visit(self, elem):
        self._print(elem, True)
        self._print_space()

    def visit_for(self, for_node):
        self._print('for (', True)
        self._new_level_indentation(0)
        for_node.for_init_statement.accept(self)
        self._print_space()
        if for_node.condition is not None:
            for_node.condition.accept(self)
        else:
            self._print_space()
        self._print_semicolon()
        self._print_space()
        if for_node.expression is not None:
            for_node.expression.accept(self)
        else:
            self._print_space()
        self._pop_indentation()
        self._print(')')
        self._new_level_indentation()
        for_node.statement.accept(self)
        self._pop_indentation()

    def visit_alias_declaration(self, alias_declaration):
        self._print('using ', True)
        self._new_level_indentation(0)
        alias_declaration.identifier.accept(self)
        self._pop_indentation()
        self._print(' = ')
        alias_declaration.type_id.accept(self)
        self._print_semicolon()

    def visit_if(self, if_node):
        self._print('if (', True)
        self._new_level_indentation(0)
        if_node.condition.accept(self)
        self._pop_indentation()
        self._print(')')
        self._new_level_indentation()
        if_node.statement.accept(self)
        self._pop_indentation()
        if if_node.else_statement is not None:
            self._print_space()
            self._print('else')
            self._new_level_indentation()
            if_node.else_statement.accept(self)
            self._pop_indentation()

    def visit_class(self, class_node):
        self._print('struct ', True)
        self._new_level_indentation(0)
        class_node.class_head.class_name.accept(self)
        self._pop_indentation()
        self._print(' {')
        self._print_new_line()
        self._new_level_indentation()
        class_node.member_specification.accept(self)
        self._pop_indentation()
        self._print('}', True)

    def visit_enum(self, enum_node):
        enum_node.enum_head.accept(self)
        self._print(' {')
        self._print_new_line()
        self._new_level_indentation()
        enum_node.enumerators.accept(self)
        self._pop_indentation()
        self._print_new_line()
        self._print('}', True)

    def visit_ternary_operation(self, ternary_operation):
        ternary_operation.logical_expression.accept(self)
        self._print('? ')
        ternary_operation.true_expression.accpet(self)
        self._print(' : ')
        ternary_operation.false_expression.accept(self)

    def visit_binary_operation(self, binary_operation):
        binary_operation.left_expression.accept(self)
        self._print(' {0} '.format(binary_operation.operation))
        binary_operation.right_expression.accept(self)

    def visit_cast_expression(self, cast_expression):
        self._print('(')
        cast_expression.new_type.accept(self)
        self._print(')')
        cast_expression.cast_expression.accept(self)

    def visit_prefix_unary(self, prefix_unary):
        self._print(prefix_unary.operator)
        prefix_unary.expression.accept(self)

    def visit_postfix_unary(self, postfix_unary):
        postfix_unary.expression.accept(self)
        self._print(postfix_unary.operator)

    def visit_function_call(self, function_call):
        function_call.function.accept(self)
        self._print('(')
        self._new_level_indentation(0)
        function_call.parameters.accept(self)
        self._pop_indentation()
        self._print(')')

    def visit_array_subscription(self, array_subscription):
        array_subscription.array_expression.accept(self)
        self._print('[')
        array_subscription.subscript_expression.accept(self)
        self._print(']')

    def visit_member_access(self, class_member_access):
        class_member_access.object_expression.accept(self)
        self._print('.')
        self._new_level_indentation(0)
        class_member_access.member_expression.accept(self)
        self._pop_indentation()

    def visit_braced_init_list(self, braced_init_list):
        self._print('{')
        self._new_level_indentation(0)
        braced_init_list.initializer_list.accept(self)
        self._pop_indentation()
        self._print('}')

    def visit_equal_initializer(self, equal_initializer):
        self._print(' = ')
        equal_initializer.initializer_clause.accept(self)

    def visit_enclosed_in_paren(self, enclosed_in_paren):
        self._print('(')
        self._new_level_indentation(0)
        enclosed_in_paren.expression.accept(self)
        self._pop_indentation()
        self._print(')')

    def visit_decl_specifier_seq(self, decl_specifier_seq):
        for it, decl_specifier in enumerate(decl_specifier_seq.elements):
            if it > 0:
                self._print_space()
                self._new_level_indentation(0)
            if isinstance(decl_specifier, str):
                self._print(decl_specifier, True)
            else:
                decl_specifier.accept(self)
            if it > 0:
                self._pop_indentation()

    def visit_program(self, program):
        for declaration in program.declarations:
            declaration.accept(self)
            self._print_new_line()

    def visit_identifier(self, identifier_node):
        self._print(identifier_node.identifier, True)

    def visit_enum_key(self, enum_key):
        self._print('enum', True)
        if enum_key.enum_key is not None:
            self._print(' {}'.format(enum_key.enum_key), True)

    def visit_enum_head(self, enum_head):
        enum_head.enum_key.accept(self)
        self._print_space()
        self._new_level_indentation(0)
        if enum_head.identifier is not None:
            enum_head.identifier.accept(self)
        self._pop_indentation()

    def visit_enumerator_list(self, enumerator_list):
        for it, enumerator in enumerate(enumerator_list.enumerators):
            if it > 0:
                self._print(',')
                self._print_new_line()
            enumerator.accept(self)

    def visit_enumerator(self, enumerator):
        enumerator.enumerator.accept(self)
        if enumerator.const_expression is not None:
            self._print(' = ')
            enumerator.const_expression.accept(self)

    def visit_init_declarator(self, init_declarator):
        if self.ref_qualifier:
            self._print('&', True)
            self._new_level_indentation(0)
            init_declarator.declarator.accept(self)
            self._pop_indentation()
        else:
            init_declarator.declarator.accept(self)
        if init_declarator.initializer is not None:
            self._new_level_indentation(0)
            init_declarator.initializer.accept(self)
            self._pop_indentation()

    def visit_function_declarator(self, function_declarator):
        if self.ref_qualifier:
            self._new_level_indentation(0)
            self._print('&')
            self._pop_indentation()
        if function_declarator.function_name is not None:
            function_declarator.function_name.accept(self)
        function_declarator.parameters.accept(self)

    def visit_statement_expression(self, statement_expression):
        if statement_expression.expression is not None:
            statement_expression.expression.accept(self)
        self._print_semicolon()

    def visit_array_declaration(self, array_declaration):
        if array_declaration.array_name is not None:
            array_declaration.array_name.accept(self)
        for parameter in array_declaration.parameters:
            self._print('[')
            self._new_level_indentation(0)
            parameter.accept(self)
            self._pop_indentation()
            self._print(']')

    def visit_literal(self, literal):
        self._print(literal.value, True)

    def visit_param_decl(self, param_declaration):
        param_declaration.declarator_with_specifiers.accept(self)
        if param_declaration.initializer is not None:
            self._new_level_indentation(0)
            self._print_space()
            param_declaration.initializer.accept(self)
            self._pop_indentation()

    def visit_function_definition(self, function_definition):
        function_definition.declarator_with_specifiers.accept(self)
        self._new_level_indentation()
        function_definition.body.accept(self)
        self._pop_indentation()

    def visit_comma_separated_list(self, comma_separated_list):
        for it, element in enumerate(comma_separated_list.elements):
            if it > 0:
                self._print(', ')
            element.accept(self)

    def visit_member_declarator(self, member_declarator):
        if self.ref_qualifier:
            self._print('&')
            self._new_level_indentation(0)
            member_declarator.declarator.accept(self)
            self._pop_indentation()
        else:
            member_declarator.declarator.accept(self)
        if member_declarator.initializer is not None:
            member_declarator.initializer.accept(self)

    def visit_assignment_expression(self, assignment_expression):
        assignment_expression.expression.accept(self)
        self._print_space()
        self._print(assignment_expression.operator)
        self._print_space()
        self._new_level_indentation(0)
        assignment_expression.initializer.accept(self)
        self._pop_indentation()

    def visit_while_loop(self, while_loop):
        self._print('while (', True)
        self._new_level_indentation(0)
        while_loop.condition.accept(self)
        self._print(')')
        self._pop_indentation()
        self._new_level_indentation()
        while_loop.statement.accept(self)
        self._pop_indentation()

    def visit_do_while_loop(self, do_while_loop):
        self._print('do', True)
        self._new_level_indentation()
        do_while_loop.statement.accept(self)
        self._pop_indentation()
        self._print_space()
        self._print('while (')
        self._new_level_indentation(0)
        do_while_loop.expression.accept(self)
        self._print(');')
        self._pop_indentation()

    def visit_range_for_loop(self, range_for):
        self._print('for (', True)
        self._new_level_indentation(0)
        range_for.declaration.accept(self)
        self._print(' : ')
        range_for.initializer.accept(self)
        self._print(')')
        self._pop_indentation()
        self._new_level_indentation()
        range_for.statement.accept(self)
        self._pop_indentation()

    def visit_break(self, break_statement):
        self._print('break;', True)

    def visit_continue(self, continue_statement):
        self._print('continue;', True)

    def visit_return(self, return_statement):
        self._print('return', True)
        if return_statement.expression is not None:
            self._print_space()
            self._new_level_indentation(0)
            return_statement.expression.accept(self)
            self._pop_indentation()
        self._print_semicolon()

    def visit_declarator_with_specifiers(self, declarator_with_specifiers):
        if declarator_with_specifiers.specifiers is not None:
            self.ref_qualifier = declarator_with_specifiers.specifiers \
                .is_ref_qualifier_present()
            declarator_with_specifiers.specifiers.accept(self)
            if declarator_with_specifiers.declarator is not None:
                self._print_space()
                self._new_level_indentation(0)
                declarator_with_specifiers.declarator.accept(self)
                self._pop_indentation()
            self.ref_qualifier = False
        elif declarator_with_specifiers.declarator is not None:
            declarator_with_specifiers.declarator.accept(self)

    def visit_operator_function(self, operator_function):
        self._print('operator', True)
        self._print(operator_function.operator)

    def visit_sequence(self, sequence):
        for elem in sequence.elements:
            elem.accept(self)
            self._print_new_line()

    def visit_simple_type(self, simple_type):
        self._print(simple_type.type_name, True)

    def visit_simple_declaration(self, simple_declaration):
        if simple_declaration.specifiers is not None:
            simple_declaration.specifiers.accept(self)
            self.ref_qualifier = simple_declaration.specifiers. \
                is_ref_qualifier_present()
        if simple_declaration.list_of_declarators is not None:
            if simple_declaration.specifiers is not None:
                self._print_space()
            self._new_level_indentation(0)
            simple_declaration.list_of_declarators.accept(self)
            self._pop_indentation()
        self.ref_qualifier = False
        self._print_semicolon()

    def visit_condition_with_declaration(self, condition_with_decl):
        condition_with_decl.declarator_with_specifiers.accept(self)
        self._new_level_indentation(0)
        condition_with_decl.initializer.accept(self)
        self._pop_indentation()

    def visit_member_declaration(self, member_declaration):
        if member_declaration.specifiers is not None:
            member_declaration.specifiers.accept(self)
            self.ref_qualifier = member_declaration.specifiers. \
                is_ref_qualifier_present()
            if member_declaration.declarator_list is not None:
                self._print_space()
                self._new_level_indentation(0)
                member_declaration.declarator_list.accept(self)
                self._pop_indentation()
            self.ref_qualifier = False
        elif member_declaration.declarator_list is not None:
            member_declaration.declarator_list.accept(self)
        self._print_semicolon()

    def visit_simple_template(self, simple_template):
        simple_template.template_name.accept(self)
        self._print('<')
        self._new_level_indentation(0)
        simple_template.template_argument_list.accept(self)
        self._pop_indentation()
        self._print('>')

    def visit_template_argument(self, template_argument):
        template_argument.argument.accept(self)

    def visit_type_specifier_sequence(self, type_specifier_sequence):
        for it, elem in enumerate(type_specifier_sequence.elements):
            if it > 0:
                self._print_space()
            elem.accept(self)

    def visit_qualifiers_and_specifiers(self, qualifiers_and_specifiers):
        self._print(qualifiers_and_specifiers.name, True)
