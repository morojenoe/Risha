import risha_ast


def generate_cpp(node, file_name):
    with open(file_name, 'w', encoding='utf-8') as cpp_file:
        traverse(node, cpp_file)


def traverse(node, file):
    if isinstance(node, risha_ast.Node):
        for child in node.childs:
            traverse(child, file)
    else:
        print(node, file=file, end='')
