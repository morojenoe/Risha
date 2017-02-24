import logging

from .symbol_table_types import *
import src.risha_ast


def make_function(function_definition):
    identifier = function_definition.name.to_string()
    return_type = _get_variable_type(
        src.risha_ast.SimpleDeclaration(function_definition.return_type, None))
    parameters = []
    for parameter in function_definition.parameters:
        variable = make_variables(parameter)
        parameters.append(variable[0])
    return Function(identifier, return_type, parameters)


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
    ref_qualifier = simple_declaration.specifiers.reference_qualifier
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
        elif isinstance(specifier, src.risha_ast.Identifier):
            var_type_specifier = VariableTypeSpecifier(specifier.identifier)
        else:
            logging.getLogger('risha').warning('Unknown specifier:' +
                                               repr(specifier))

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
                           declarator.initializer.initializer_clause if
                           declarator.initializer is not None else None))
        return result
    elif isinstance(simple_declaration.declarators, src.risha_ast.Identifier):
        return [(simple_declaration.declarators, None)]
    else:
        return [(simple_declaration.declarators.declarator,
                 simple_declaration.declarators.initializer.initializer_clause)]
