import src.ast_visitors.semantic_analysis


class TypeTable:
    def __init__(self):
        self._type_table = {}

    def add_type(self, var_type):
        if var_type in self._type_table:
            return self
        self._type_table[var_type] = \
            src.ast_visitors.semantic_analysis.symbol_table.SymbolTable()
        return self

    def add_function_to_type(self, var_type, function):
        if var_type not in self._type_table:
            self.add_type(var_type)
        self._type_table[var_type].insert_function(function)
        return self

    def add_variable_or_const(self, var_type, variable):
        if var_type not in self._type_table:
            self.add_type(var_type)
        self._type_table[var_type].insert_variable(variable)
        return self
