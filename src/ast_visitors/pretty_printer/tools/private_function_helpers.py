import copy
import logging

import src.risha_ast


def fun_def2fun_decl(function_definition):
    if not isinstance(function_definition, src.risha_ast.FunctionDefinition):
        logging.error('Parameter must be a subclass of '
                      'risha_ast.FunctionDefinition')
        return None
    return copy.deepcopy(function_definition).remove_body()