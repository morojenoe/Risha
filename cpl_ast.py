class ASTNode:
    pass


class Node(ASTNode):
    def __init__(self, *args):
        self.childs = list(args)
