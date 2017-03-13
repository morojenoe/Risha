import src.risha_ast
from .private_class_helpers import class_def2class_fwd_decl, \
    fun_def2class_fun_def, class_def2class_decl


def make_class_forward_declarations(classes):
    class_forward_declarations = src.risha_ast.Program(
        row=-1, col=-1, num_new_lines_after_decl=1)
    for cls in classes:
        class_fwd_decl = class_def2class_fwd_decl(cls)
        if class_fwd_decl is not None:
            class_forward_declarations.add(class_fwd_decl)
    return class_forward_declarations


def make_class_declarations(classes):
    class_declarations = src.risha_ast.Program(row=-1, col=-1)
    for cls in classes:
        class_decl = class_def2class_decl(cls)
        if class_decl is not None:
            class_decl = src.risha_ast.SimpleDeclaration(
                src.risha_ast.DeclSpecifierSeq(row=-1, col=-1).add(class_decl),
                None, row=-1, col=-1)
            class_declarations.add(class_decl)
    return class_declarations


def make_class_definitions(classes):
    class_definitions = src.risha_ast.Program(row=-1, col=-1)
    for cls in classes:
        fun_definitions = src.risha_ast.filter_sequence(
            cls.members, src.risha_ast.FunctionDefinition)
        for fun_def in fun_definitions:
            class_definitions.add(fun_def2class_fun_def(fun_def, cls))
    return class_definitions
