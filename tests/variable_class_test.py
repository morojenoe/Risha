import unittest

from src.ast_visitors import VariableIdentifier


class VariableClassTest(unittest.TestCase):
    def test_equality(self):
        var_int_1 = VariableIdentifier('int')
        var_int_2 = VariableIdentifier('int')
        self.assertEqual(var_int_1, var_int_2)

    def test_template_equality(self):
        var_int_1 = VariableIdentifier('vector', 'int', 'allocator', 'int')
        var_int_2 = VariableIdentifier('vector', 'int', 'allocator', 'int')
        self.assertEqual(var_int_1, var_int_2)

    def test_inequality(self):
        var_int_1 = VariableIdentifier('string')
        var_int_2 = VariableIdentifier('char')
        self.assertNotEqual(var_int_1, var_int_2)

    def test_template_inequality(self):
        var_int_1 = VariableIdentifier('map', 'int', 'long long')
        var_int_2 = VariableIdentifier('map', 'int', 'unsigned long long')
        self.assertNotEqual(var_int_1, var_int_2)

    def test_nested_equal(self):
        var_int_1 = VariableIdentifier('map',
                                       VariableIdentifier('int'),
                                       VariableIdentifier('long long'))
        var_int_2 = VariableIdentifier('map',
                                       VariableIdentifier('int'),
                                       VariableIdentifier('long long'))
        self.assertEqual(var_int_1, var_int_2)

    def test_nested_not_equal(self):
        var_int_1 = VariableIdentifier('map',
                                       VariableIdentifier('int'),
                                       VariableIdentifier('long long'))
        var_int_2 = VariableIdentifier('map',
                                       VariableIdentifier('int'),
                                       VariableIdentifier('unsigned long long'))
        self.assertNotEqual(var_int_1, var_int_2)


if __name__ == '__main__':
    unittest.main()
