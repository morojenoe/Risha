import src.risha_ast


def make_data(data):
    return src.risha_ast.Program(data, num_new_lines_after_decl=1)
