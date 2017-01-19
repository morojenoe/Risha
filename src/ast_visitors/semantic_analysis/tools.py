import logging

from .symbol_table_types import *
import src.risha_ast


def make_variables(simple_declaration):
    var_type = _get_variable_type(simple_declaration)
    var_identifiers_and_initializers = _get_identifiers_and_initializers(
        simple_declaration)
    variables = [Variable(identifier, var_type, initializer)
                 for identifier, initializer in
                 var_identifiers_and_initializers]
    return variables


def _get_variable_type(simple_declaration):
    const_qualifier = None
    storage_qualifier = None
    ref_qualifier = None
    var_type_specifier = None
    for specifier in simple_declaration.specifiers:
        if isinstance(specifier, src.risha_ast.ConstQualifier):
            const_qualifier = True
        elif isinstance(specifier, src.risha_ast.SimpleType):
            var_type_specifier = VariableTypeSpecifier(specifier.name)
        elif isinstance(specifier, src.risha_ast.ReferenceQualifier):
            ref_qualifier = True
        elif isinstance(specifier, src.risha_ast.StorageSpecifier):
            storage_qualifier = True
        else:
            logging.getLogger('risha').warning('Unknown specifier:' + specifier)

    return VariableType(const_qualifier,
                        storage_qualifier,
                        ref_qualifier,
                        var_type_specifier)


def _get_identifiers_and_initializers(simple_declaration):
    if isinstance(simple_declaration.declarators,
                  src.risha_ast.InitDeclaratorList):
        result = []
        for declarator in simple_declaration.declarators.elements:
            result.append((declarator.declarator,
                           declarator.initializer.initializer_clause))
        return result
    else:
        return [(simple_declaration.declarator.declarator,
                 simple_declaration.declarator.initializer.initializer_clause)]
