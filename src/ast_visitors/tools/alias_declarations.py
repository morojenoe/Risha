import src.risha_ast


def make_alias_declarations(alias_declarations):
    return src.risha_ast.Program(row=-1,
                                 col=-1,
                                 declarations=alias_declarations)
