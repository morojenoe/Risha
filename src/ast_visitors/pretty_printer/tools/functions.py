import src.risha_ast
import logging


def _fun_def2fun_decl(function_definition):
    if not isinstance(function_definition, src.risha_ast.FunctionDefinition):
        logging.error('Parameter must be a subclass of '
                      'risha_ast.FunctionDefinition')
        return None
    function_declaration = \
        src.risha_ast.SimpleDeclaration(
            function_definition.function_head.specifiers,
            function_definition.function_head.declarators,
            True)
    return function_declaration


def make_function_declarations(function_definitions):
    function_declarations = src.risha_ast.Program(num_new_lines_after_decl=1)
    for fun_def in function_definitions:
        fun_decl = _fun_def2fun_decl(fun_def)
        if fun_decl is not None:
            function_declarations.add(fun_decl)
    return function_declarations


def make_function_definitions(function_definitions):
    return src.risha_ast.Program(function_definitions)
