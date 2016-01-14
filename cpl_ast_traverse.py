import cpl_ast


def generate_cpp(node):
    file = open('test.cpp', 'w', encoding='utf-8')
    traverse(node, file)


def traverse(node, file):
    if isinstance(node, cpl_ast.Node):
        for child in node.childs:
            traverse(child, file)
    else:
        print(node, file=file)
