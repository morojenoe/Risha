import unittest
import src.ast_visitors.semantic_analysis.types as types


class VariableTestCase(unittest.TestCase):
    def test_simple_variable(self):
        variable = types.Variable('current_maximum', types.VariableType(None,
                                                                        None,
                                                                        None,
                                                                        'int'))
        self.assertEqual('int current_maximum', str(variable))

    def test_const_variable(self):
        variable = types.Variable('N_MAX', types.VariableType('const',
                                                              None,
                                                              None,
                                                              'double'))

        self.assertEqual('const double N_MAX', str(variable))

    def test_reference_qualifier(self):
        variable = types.Variable('count_numbers', types.VariableType(None,
                                                                      None,
                                                                      'ref',
                                                                      'bint'))

        self.assertEqual('ref bint count_numbers', str(variable))

    def test_all_qualifiers(self):
        variable = types.Variable('unique_numbers', types.VariableType('const',
                                                                       'static',
                                                                       None,
                                                                       'set'))

        self.assertEqual('static const set unique_numbers', str(variable))


class FunctionTestCase(unittest.TestCase):
    def test_simple_function(self):
        params = [types.Variable('x', types.VariableType('const', None,
                                                         'ref', 'uint'))]
        variable = types.Function('count_bit', 'size_t', params)
        self.assertEqual('size_t count_bit(const ref uint x)', str(variable))


if __name__ == '__main__':
    unittest.main()
