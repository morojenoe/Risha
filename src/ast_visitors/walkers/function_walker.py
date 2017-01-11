from .empty_tree_walker import EmptyTreeWalker


class FunctionWalker(EmptyTreeWalker):
    def __init__(self):
        super().__init__()
        self._functions = []
        self._count_scope_enterings = 0

    def visit_function_definition_before(self, function_definition):
        if self._count_scope_enterings == 0:
            self._functions.append(function_definition)
        self._count_scope_enterings += 1

    def visit_class_before(self, class_node):
        self._count_scope_enterings += 1

    def visit_class_after(self, class_node):
        self._count_scope_enterings -= 1

    def visit_function_definition_after(self, function_definition):
        self._count_scope_enterings -= 1

    def get_functions(self):
        for function in self._functions:
            yield function
