import unittest
from src.ast_visitors.semantic_analysis.symbol_table_types import Function, \
    VariableType, Variable


class VariableTestCase(unittest.TestCase):
    def test_simple_variable(self):
        variable = Variable('current_maximum',
                            VariableType(None, None, None, 'int'),
                            False)
        self.assertEqual('int current_maximum', str(variable))

    def test_const_variable(self):
        variable = Variable('N_MAX',
                            VariableType('const', None, None,
                                         'double'),
                            False)

        self.assertEqual('const double N_MAX', str(variable))

    def test_reference_qualifier(self):
        variable = Variable('count_numbers',
                            VariableType(None, None, 'ref', 'bint'),
                            False)

        self.assertEqual('ref bint count_numbers', str(variable))

    def test_all_qualifiers(self):
        variable = Variable('unique_numbers',
                            VariableType('const', 'static', None,
                                         'set'),
                            False)

        self.assertEqual('static const set unique_numbers', str(variable))

    def test_default_value(self):
        variable = Variable('unique_numbers',
                            VariableType(None, None, None, 'set'),
                            True)

        self.assertEqual('set unique_numbers = default', str(variable))


class FunctionTestCase(unittest.TestCase):
    def test_simple_function(self):
        params = [Variable('x', VariableType('const', None,
                                             'ref', 'uint'), False)]
        variable = Function('count_bit', 'size_t', params)
        self.assertEqual('size_t count_bit(const ref uint x)', str(variable))

    def test_range_parameters(self):
        params = [
            Variable('x',
                     VariableType(None, None, None, 'int'),
                     False),
            Variable('y',
                     VariableType(None, None, None, 'int'),
                     False),
            Variable('z',
                     VariableType(None, None, None, 'int'),
                     False),
            Variable('v',
                     VariableType(None, None, None, 'int'),
                     True),
            Variable('r',
                     VariableType(None, None, None, 'int'),
                     True),
        ]
        func = Function('is_point_inside_sphere', 'bool', params)
        self.assertEqual((3, 5), func.parameters_range())

    def test_range_parameters_with_no_default_params(self):
        params = [
            Variable('x',
                     VariableType(None, None, None, 'int'),
                     False),
            Variable('y',
                     VariableType(None, None, None, 'int'),
                     False),
            Variable('z',
                     VariableType(None, None, None, 'int'),
                     False),
            Variable('v',
                     VariableType(None, None, None, 'int'),
                     False),
            Variable('r',
                     VariableType(None, None, None, 'int'),
                     False),
        ]
        func = Function('is_point_inside_sphere', 'bool', params)
        self.assertEqual((5, 5), func.parameters_range())


if __name__ == '__main__':
    unittest.main()
