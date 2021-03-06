import warnings

from .symbol_table import SymbolTable


class ScopeTable:
    def __init__(self):
        self._symbol_tables = []

    def enter_scope(self):
        self._symbol_tables.append(SymbolTable())
        return self

    def exit_scope(self):
        if len(self._symbol_tables) == 0:
            raise IndexError("There is no scope you've entered")
        self._symbol_tables.pop()
        return self

    def insert_variable(self, variable):
        if len(self._symbol_tables) == 0:
            raise IndexError("There is no scope you're entered")
        self._symbol_tables[-1].insert_variable(variable)
        return self

    def insert_function(self, function):
        if len(self._symbol_tables) == 0:
            raise IndexError("There is no scope you're entered")
        self._symbol_tables[-1].insert_function(function)
        return self

    def insert_new_type(self, variable_type):
        if len(self._symbol_tables) == 0:
            raise IndexError("There is no scope you're entered")
        self._symbol_tables[-1].insert_new_type(variable_type)
        return self

    def lookup_variable(self, identifier):
        for scope in reversed(self._symbol_tables):
            if scope.lookup_variable(identifier) is not None:
                return scope.lookup_variable(identifier)
        return None

    def lookup_function(self, function):
        for scope in reversed(self._symbol_tables):
            if scope.lookup_function(function) is not None:
                return scope.lookup_function(function)
        return None
