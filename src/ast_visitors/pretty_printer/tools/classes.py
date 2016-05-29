import src.risha_ast
import logging


def _class_def2class_decl(class_definition):
    if not isinstance(class_definition, src.risha_ast.ClassDefinition):
        logging.error('Parameter must be a subclass of '
                      'risha_ast.ClassDefinition')
        return None
    class_declaration = src.risha_ast.SimpleDeclaration(
        src.risha_ast.DeclSpecifierSeq().add(class_definition.class_head),
        None)
    return class_declaration


def make_class_declarations(class_definitions):
    class_declarations = src.risha_ast.Program(num_new_lines_after_decl=1)
    for cls_definition in class_definitions:
        class_decl = _class_def2class_decl(cls_definition)
        if class_decl is not None:
            class_declarations.add(class_decl)
    return class_declarations
