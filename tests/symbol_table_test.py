import unittest
from src.ast_visitors.semantic_analysis.symbol_table_types import Variable, \
    VariableType, Function
from src.ast_visitors.semantic_analysis.symbol_table import SymbolTable


class SymbolTableVariablesTestCase(unittest.TestCase):
    def test_simple_variable(self):
        symbol_table = SymbolTable()
        variable = Variable('current_maximum',
                            VariableType(None, None, None, 'int'),
                            False)
        symbol_table.insert_variable(variable)
        self.assertEqual(variable,
                         symbol_table.lookup_variable(variable.identifier))


class SymbolTableFunctionsTestCase(unittest.TestCase):
    def test_simple_function(self):
        symbol_table = SymbolTable()
        params = [Variable('x', VariableType('const', None, 'ref', 'uint'),
                           False)]
        func = Function('count_bit', 'size_t', params)
        symbol_table.insert_function(func)
        self.assertEqual(func, symbol_table.lookup_function(func))

    def test_not_existed_function(self):
        symbol_table = SymbolTable()
        params = [Variable('x', VariableType('const', None, 'ref', 'uint'),
                           False)]
        func = Function('count_bit', 'size_t', params)
        self.assertEqual(None, symbol_table.lookup_function(func))

if __name__ == '__main__':
    unittest.main()
