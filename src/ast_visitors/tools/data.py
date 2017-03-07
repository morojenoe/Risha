import src.risha_ast


def make_data(data):
    return src.risha_ast.Program(row=-1, col=-1, declarations=data,
                                 num_new_lines_after_decl=1)
