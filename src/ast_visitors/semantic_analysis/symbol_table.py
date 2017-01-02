import warnings

from .symbol_table_types import Function, Variable, VariableType


class SymbolTable:
    def __init__(self):
        self._variables = {}
        self._functions = {}
        self._types = {}

    def insert_variable(self, variable):
        if variable.identifier in self._variables:
            warnings.warn('Identifier {old_id} is already in symbol table. '
                          'You\'re trying to add new identifier {new_id}. '
                          'Old value will be overwritten.'.format(
                old_id=self._variables[variable.identifier], new_id=variable))

        if not issubclass(variable, Variable):
            raise TypeError('SymbolTable expects variable of type Variable, '
                            'got {type}'.format(type=type(variable)))
        self._variables[variable.identifier] = variable

    def insert_function(self, function):
        if self._functions.get(function.identifier) is None:
            self._functions[function.identifier] = []
        self._functions[function.identifier].append(function)

    def insert_new_type(self, identifier, symbol_table):
        self._types[identifier] = symbol_table

    def lookup_variable(self, identifier):
        return self._variables.get(identifier)

    def lookup_function(self, function):
        functions = list(filter(self._is_functions_similar, self._functions[
            function.identifier]))
        if len(functions) == 0:
            return None
        if len(functions) == 1:
            return functions[0]
        raise LookupError('SymbolTable has many functions that are '
                          'appropriate for given function.')

    def _is_functions_similar(self, called_func, func_in_table):
        """
        Return True if func_in_table is suited for calling like called_func.
        """
        if called_func.identifier != func_in_table.identifier:
            return False
        params_range = func_in_table.parameters_range()
        if params_range[0] <= len(called_func.parameters) <= params_range[1]:
            return all(map(lambda p1, p2: p1 == p2, called_func.parameters,
                       func_in_table.parameters))
        return False
