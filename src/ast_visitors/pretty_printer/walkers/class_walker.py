from src.ast_visitors.pretty_printer.walkers.empty_tree_walker \
    import EmptyTreeWalker


class ClassWalker(EmptyTreeWalker):
    def __init__(self):
        super().__init__()
        self._classes = []
        self._count_scope_enterings = 0

    def visit_class_before(self, class_node):
        if self._count_scope_enterings == 0:
            self._classes.append(class_node)
        self._count_scope_enterings += 1

    def visit_class_after(self, class_node):
        self._count_scope_enterings -= 1

    def visit_function_definition_before(self, function_definition):
        self._count_scope_enterings += 1

    def visit_function_definition_after(self, function_definition):
        self._count_scope_enterings -= 1

    def get_classes(self):
        for _class in self._classes:
            yield _class
