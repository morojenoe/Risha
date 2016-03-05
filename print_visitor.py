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

        self._print('{\n')
        self.indentation += self.inc_indentation
        for statement in compound_statement.statements:
            statement.accept(self)
            self._print('\n')
        self.indentation -= self.inc_indentation
        self._print('}\n')

    def _print(self, text):
        print(text, file=self.output, end='')

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
            self._print(' {\n')
        for alias in class_node.alias_declarations:
            alias.accept(self)
        for declaration in class_node.declarations:
            declaration.accept(self)
        for function in class_node.functions:
            function.accept(self)
        self._print('}\n')

    def visit_enum(self, enum_node):
        self._print('enum')
        if enum_node.enum_key is not None:
            self._print(' ' + enum_node.enum_key)
        if enum_node.enum_name is not None:
            self._print(' ' + enum_node.enum_name)
        self._print(' {\n')
        for enumerator in enum_node.enumerators:
            self._print(enumerator[0])
            if enumerator[1] is not None:
                self._print(' = ')
                enumerator[1].accept(self)
            self._print(',\n')
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
