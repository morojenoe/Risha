import logging

from .symbol_table_types import *
import src.risha_ast


def make_function(function_definition):
    identifier = function_definition.name.to_string()
    return_type = _get_variable_type(
        src.risha_ast.SimpleDeclaration(function_definition.return_type,
                                        None, -1, -1))
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


def make_variable_from_enumerator(enumerator: src.risha_ast.Enumerator,
                                  enum_name):
    var_type_specifier = VariableTypeSpecifier(enum_name)
    var_type = VariableType(cv_qualifier=True,
                            storage_qualifier=False,
                            reference_qualifier=False,
                            var_type=var_type_specifier)
    return Variable(enumerator.enumerator.identifier, var_type, True)


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
        elif isinstance(specifier, src.risha_ast.EnumDefinition):
            var_type_specifier = specifier.identifier
        elif isinstance(specifier, src.risha_ast.ClassDefinition):
            var_type_specifier = specifier.name_as_string()
        else:
            logging.getLogger('risha').warning('Unknown specifier:' +
                                               repr(specifier))

    return VariableType(const_qualifier,
                        storage_qualifier,
                        ref_qualifier,
                        var_type_specifier)


def _get_identifiers_and_initializers(simple_declaration):
    if (isinstance(simple_declaration.declarators,
                   src.risha_ast.InitDeclaratorList) or
            isinstance(simple_declaration.declarators,
                       src.risha_ast.MemberDeclaratorList)):
        result = []
        for declarator in simple_declaration.declarators.elements:
            identifier = _get_identifier(declarator.declarator)
            initializer = _get_initializer(declarator.initializer)
            result.append((identifier, initializer))
        return result
    elif isinstance(simple_declaration.declarators, src.risha_ast.Identifier):
        identifier = _get_identifier(simple_declaration.declarators)
        return [(identifier, None)]
    else:
        identifier = _get_identifier(simple_declaration.declarators.declarator)
        initializer = _get_initializer(
            simple_declaration.declarators.initializer)
        return [(identifier, initializer)]


def _get_identifier(declarator):
    assert isinstance(declarator, src.risha_ast.Identifier)
    return declarator.identifier


def _get_initializer(initializer):
    if initializer is None:
        return None
    assert isinstance(initializer, src.risha_ast.EqualInitializer)
    return initializer.initializer_clause
