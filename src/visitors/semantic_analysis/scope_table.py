from .symbol_table import SymbolTable


class ScopeTable:
    def __init__(self):
        self.symbol_tables = []

    def enter_scope(self):
        self.symbol_tables.append(SymbolTable())

    def exit_scope(self):
        self.symbol_tables.pop()

    def insert_variable(self, variable):
        pass

    def insert_function(self, function):
        pass

    def insert_new_type(self, variable_type):
        pass

    def lookup_variable(self, identifier):
        pass

    def lookup_function(self, function):
        pass
