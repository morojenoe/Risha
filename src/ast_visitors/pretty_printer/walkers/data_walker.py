from src.ast_visitors.pretty_printer.walkers.empty_tree_walker \
    import EmptyTreeWalker


class DataWalker(EmptyTreeWalker):
    def __init__(self):
        super().__init__()
        self._data = []
        self._count_scope_enterings = 0

    def visit_class_before(self, class_node):
        self._count_scope_enterings += 1

    def visit_class_after(self, class_node):
        self._count_scope_enterings -= 1

    def visit_function_definition_before(self, function_definition):
        self._count_scope_enterings += 1

    def visit_function_definition_after(self, function_definition):
        self._count_scope_enterings -= 1

    def visit_simple_declaration_before(self, simple_declaration):
        if self._count_scope_enterings == 0:
            self._data.append(simple_declaration)

    def get_data(self):
        for data in self._data:
            yield data
