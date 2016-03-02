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
