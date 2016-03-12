from src.visitors import abstract_visitor


class PrintVisitor(abstract_visitor.AbstractVisitor):
    def __init__(self, output, inc_indentation=2):
        self.output = output
        self.indentation = [0]
        self.inc_indentation = inc_indentation

    def _new_level_indentation(self, value=None):
        if value is None:
            value = self.indentation[-1] + self.inc_indentation
        self.indentation.append(value)

    def _pop_indentation(self):
        self.indentation.pop()

    def visit_compound_statement(self, compound_statement):
        if compound_statement.statements is None:
            self._print('{ }')
            return

        self._print('{')
        self._print_new_line()
        self._new_level_indentation()
        for statement in compound_statement.statements:
            statement.accept(self)
            self._print_new_line()
        self._pop_indentation()
        self._print('}', True)
        self._print_new_line()

    def _print(self, text, indentation=False):
        if indentation:
            print(' ' * self.indentation[-1], file=self.output, end='')
        print(text, file=self.output, end='')

    def _print_new_line(self):
        print('\n', file=self.output, end='')

    def visit(self, elem):
        self._print(elem + ' ', True)

    def visit_for(self, for_node):
        self._print('for (', True)
        for_node.for_init_statement.accept(self)
        if for_node.condition is not None:
            for_node.condition.accept(self)
        else:
            self._print(' ')
        self._print('; ')
        if for_node.expression is not None:
            for_node.expression.accept(self)
        else:
            self._print(' ')
        self._print(') ')
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
        self._print(';')

    def visit_if(self, if_node):
        self._print('if (', True)
        if_node.condition.accept(self)
        self._print(') ')
        if_node.statement.accept(self)
        if if_node.else_statement is not None:
            self._print(' else ')
            if_node.else_statement.accept(self)

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
        self._print_new_line()

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

    def visit_expression(self, expression_node):
        for it, expression in enumerate(expression_node.expressions):
            if it > 0:
                self._print(', ')
            expression.accept(self)

    def visit_prefix_unary(self, prefix_unary):
        self._print(prefix_unary.operator)
        prefix_unary.expression.accept(self)

    def visit_postfix_unary(self, postfix_unary):
        postfix_unary.expression.accept(self)
        self._print(postfix_unary.operator)

    def visit_function_call(self, function_call):
        function_call.function.accept(self)
        self._print('(')
        function_call.parameters.accept(self)
        self._print(')')

    def visit_array_subscription(self, array_subscription):
        array_subscription.array_expression.accept(self)
        self._print('[')
        array_subscription.subscription_expression.accept(self)
        self._print(']')

    def visit_member_access(self, class_member_access):
        class_member_access.object_expression.accept(self)
        self._print('.')
        class_member_access.member_expression.accept(self)

    def visit_initializer_list(self, initializer_list):
        for it, elem in enumerate(initializer_list.initializer_clauses):
            if it > 0:
                self._print(', ')
            elem.accept(self)

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
        enclosed_in_paren.expression.accept(self)
        self._print(')')

    def visit_decl_specifier_seq(self, decl_specifier_seq):
        for decl_specifier in decl_specifier_seq.decl_specifiers:
            if isinstance(decl_specifier, str):
                self._print(decl_specifier + ' ', True)
            else:
                decl_specifier.accept(self)

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
        self._print(' ')
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

    def visit_member_specification(self, member_specification):
        for member in member_specification.members:
            member.accept(self)
            self._print_new_line()

    def visit_init_declarator(self, init_declarator):
        init_declarator.declarator.accept(self)
        if init_declarator.initializer is not None:
            self._print(' ')
            init_declarator.initializer.accept(self)

    def visit_init_declarator_list(self, init_declarator_list):
        for it, declarator in enumerate(init_declarator_list.declarators):
            if it > 0:
                self._print(', ')
            declarator.accept(self)

    def visit_function_declarator(self, function_declarator):
        self._new_level_indentation(0)
        function_declarator.function_name.accept(self)
        function_declarator.parameters.accept(self)
        self._pop_indentation()

    def visit_expression_statement(self, expression_statement):
        if expression_statement.statement is not None:
            expression_statement.statement.accept(self)
        self._print(';')

    def visit_array_declaration(self, array_declaration):
        array_declaration.array_name.accept(self)
        for parameter in array_declaration.parameters:
            self._print('[')
            parameter.accept(self)
            self._print(']')

    def visit_string_literal(self, string_literal):
        self._print(string_literal.value)

    def visit_floating_literal(self, floating_literal):
        self._print(floating_literal.value)

    def visit_boolean_literal(self, boolean_literal):
        self._print(boolean_literal.value)

    def visit_integer_literal(self, integer_literal):
        self._print(integer_literal.value)

    def visit_character_literal(self, character_literal):
        self._print(character_literal.value)

    def visit_param_decl_list(self, param_decl_list):
        for it, parameter in enumerate(param_decl_list.parameters):
            if it > 0:
                self._print(', ')
            parameter.accept(self)

    def visit_param_decl(self, param_declaration):
        param_declaration.decl_specifiers.accept(self)
        self._print(' ')
        self._new_level_indentation(0)
        param_declaration.declarator.accept(self)
        self._print(' ')
        param_declaration.initializer.accept(self)
        self._pop_indentation()

    def visit_function_definition(self, function_definition):
        function_definition.decl_specifiers.accept(self)
        self._print(' ')
        self._new_level_indentation(0)
        function_definition.declarator.accept(self)
        self._pop_indentation()
        function_definition.body.accept(self)
