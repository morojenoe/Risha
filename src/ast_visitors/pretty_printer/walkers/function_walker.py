from .abstract_tree_walker import AbstractTreeWalker


class FunctionWalker(AbstractTreeWalker):
    def __init__(self):
        super().__init__()
        self._functions = []

    def visit_function_definition_before(self, function_definition):
        self._functions.append(function_definition)

    def get_functions(self):
        for function in self._functions:
            yield function
