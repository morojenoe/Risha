import copy

import src.risha_ast
import logging


def _class_def2class_decl(cls):
    if not isinstance(cls, src.risha_ast.ClassDefinition):
        logging.error('Parameter must be a subclass of a'
                      'risha_ast.ClassDefinition')
        return None
    class_declaration = src.risha_ast.SimpleDeclaration(
        src.risha_ast.DeclSpecifierSeq().add(cls.class_head),
        None)
    return class_declaration


def _fun_def2class_fun_def(fun_def, cls):
    if not isinstance(fun_def, src.risha_ast.FunctionDefinition):
        logging.error('The first parameter must be a subclass of a '
                      'risha_ast.FunctionDefinition')
        return None
    if not isinstance(cls, src.risha_ast.ClassDefinition):
        logging.error('The second parameter must be a subclass of a'
                      'risha_ast.ClassDefinition')
        return None
    fun = copy.deepcopy(fun_def)
    fun.name = src.risha_ast.NestedNameSpecifier()\
        .add(cls.name)\
        .add(fun_def.name)
    return fun


def make_class_declarations(classes):
    class_declarations = src.risha_ast.Program(num_new_lines_after_decl=1)
    for cls in classes:
        class_decl = _class_def2class_decl(cls)
        if class_decl is not None:
            class_declarations.add(class_decl)
    return class_declarations


def make_class_definitions(classes):
    class_definitions = src.risha_ast.Program()
    for cls in classes:
        fun_definitions = cls.members.extract_functions()
        for fun_def in fun_definitions:
            class_definitions.add(_fun_def2class_fun_def(fun_def, cls))
    return class_definitions
