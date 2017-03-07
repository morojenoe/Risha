import src.risha_ast

from .private_function_helpers import fun_def2fun_decl


def make_function_declarations(function_definitions):
    function_declarations = src.risha_ast.Program(
        row=-1, col=-1, num_new_lines_after_decl=1)
    for fun_def in function_definitions:
        fun_decl = fun_def2fun_decl(fun_def)
        if fun_decl is not None:
            function_declarations.add(fun_decl)
    return function_declarations


def make_function_definitions(function_definitions):
    return src.risha_ast.Program(row=-1,
                                 col=-1,
                                 declarations=list(function_definitions))
