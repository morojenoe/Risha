from .abstract_tree_walker import AbstractTreeWalker


class ClassVisitor(AbstractTreeWalker):
    def __init__(self):
        super().__init__()
        self._classes = []

    def visit_class_before(self, class_node):
        self._classes.append(class_node)

    def get_classes(self):
        for _class in self._classes:
            yield _class
