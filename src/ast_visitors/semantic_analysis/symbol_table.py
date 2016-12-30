import warnings


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
        pass
