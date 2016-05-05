class SymbolTable:
    def __init__(self):
        self._variables = {}
        self._functions = {}
        self._types = {}

    def insert_variable(self, variable):
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
