import abstract_visitor


class PrintVisitor(abstract_visitor.AbstractVisitor):
    def __init__(self, output, inc_indentation=2):
        self.output = output
        self.indentation = 0
        self.inc_indentation = inc_indentation

    def visit_compound_statement(self, compound_statement):
        if compound_statement.statements is None:
            self._print('{ }')
            return

        self._print('{')
        self._print_new_line()
        self.indentation += self.inc_indentation
        for statement in compound_statement.statements:
            statement.accept(self)
            self._print_new_line()
        self.indentation -= self.inc_indentation
        self._print('}')
        self._print_new_line()

    def _print(self, text):
        print(text, file=self.output, end='')

    def _print_new_line(self):
        print('\n', file=self.output, end='')

    def visit(self, elem):
        self._print(elem + ' ')

    def visit_for(self, for_node):
        self._print('for (')
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
        self.indentation += self.inc_indentation
        for_node.statement.accept(self)
        self.indentation -= self.inc_indentation

    def visit_alias_declaration(self, alias_declaration):
        self._print('using {id} = '.format(id=alias_declaration.identifier))
        alias_declaration.type_id.accept(self)
        self._print(';')

    def visit_if(self, if_node):
        self._print('if (')
        if_node.condition.accept(self)
        self._print(') ')
        if_node.statement.accept(self)
        if if_node.else_statement is not None:
            self._print(' else')
            if_node.else_statement.accept(self)

    def visit_class(self, class_node):
        self._print('struct ')
        if class_node.class_name is not None:
            self._print(class_node.class_name)
            self._print(' {')
            self._print_new_line()
        for alias in class_node.alias_declarations:
            alias.accept(self)
        for declaration in class_node.declarations:
            declaration.accept(self)
        for function in class_node.functions:
            function.accept(self)
        self._print('}')
        self._print_new_line()

    def visit_enum(self, enum_node):
        self._print('enum')
        if enum_node.enum_key is not None:
            self._print(' ' + enum_node.enum_key)
        if enum_node.enum_name is not None:
            self._print(' ' + enum_node.enum_name)
        self._print(' {')
        self._print_new_line()
        for enumerator in enum_node.enumerators:
            self._print(enumerator[0])
            if enumerator[1] is not None:
                self._print(' = ')
                enumerator[1].accept(self)
            self._print(',')
            self._print_new_line()
        self._print('}')

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
        braced_init_list.initializer_list.accept(self)
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
                self._print(decl_specifier + ' ')
            else:
                decl_specifier.accept(self)

    def visit_program(self, program):
        for declaration in program.declarations:
            declaration.accept(self)
