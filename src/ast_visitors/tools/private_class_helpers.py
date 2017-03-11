import copy
import logging

import src.risha_ast
from .private_function_helpers import fun_def2fun_decl


def class_def2class_fwd_decl(cls):
    if not isinstance(cls, src.risha_ast.ClassDefinition):
        logging.error('Parameter must be a subclass of a'
                      'risha_ast.ClassDefinition')
        return None
    class_declaration = src.risha_ast.SimpleDeclaration(
        specifiers=src.risha_ast.DeclSpecifierSeq(row=cls.row, col=cls.col).add(
            cls.class_head),
        declarators=None,
        row=cls.row,
        col=cls.col)
    return class_declaration


def fun_def2class_fun_def(fun_def, cls):
    if not isinstance(fun_def, src.risha_ast.FunctionDefinition):
        logging.error('The first parameter must be a subclass of a '
                      'risha_ast.FunctionDefinition')
        return None
    if not isinstance(cls, src.risha_ast.ClassDefinition):
        logging.error('The second parameter must be a subclass of a'
                      'risha_ast.ClassDefinition')
        return None
    fun = copy.deepcopy(fun_def)
    fun.name = src.risha_ast.NestedNameSpecifier(row=-1, col=-1) \
        .add(cls.name) \
        .add(fun_def.name)
    return fun


def class_def2class_decl(cls):
    if not isinstance(cls, src.risha_ast.ClassDefinition):
        logging.error('Parameter must be a subclass of a'
                      'risha_ast.ClassDefinition')
        return None
    new_class = copy.deepcopy(cls)
    cls_fun = new_class.get_all_functions()
    new_class.remove_all_functions()
    return new_class.add_members([fun_def2fun_decl(fun) for fun in cls_fun])
