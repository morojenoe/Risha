import unittest

from src.ast_visitors import VariableTypeSpecifier


class VariableClassTest(unittest.TestCase):
    def test_equality(self):
        var_int_1 = VariableTypeSpecifier('int')
        var_int_2 = VariableTypeSpecifier('int')
        self.assertEqual(var_int_1, var_int_2)

    def test_template_equality(self):
        var_int_1 = VariableTypeSpecifier('vector', 'int', 'allocator', 'int')
        var_int_2 = VariableTypeSpecifier('vector', 'int', 'allocator', 'int')
        self.assertEqual(var_int_1, var_int_2)

    def test_inequality(self):
        var_int_1 = VariableTypeSpecifier('string')
        var_int_2 = VariableTypeSpecifier('char')
        self.assertNotEqual(var_int_1, var_int_2)

    def test_template_inequality(self):
        var_int_1 = VariableTypeSpecifier('map', 'int', 'long long')
        var_int_2 = VariableTypeSpecifier('map', 'int', 'unsigned long long')
        self.assertNotEqual(var_int_1, var_int_2)

    def test_nested_equal(self):
        var_int_1 = VariableTypeSpecifier('map',
                                          VariableTypeSpecifier('int'),
                                          VariableTypeSpecifier('long long'))
        var_int_2 = VariableTypeSpecifier('map',
                                          VariableTypeSpecifier('int'),
                                          VariableTypeSpecifier('long long'))
        self.assertEqual(var_int_1, var_int_2)

    def test_nested_not_equal(self):
        var_int_1 = VariableTypeSpecifier('map',
                                          VariableTypeSpecifier('int'),
                                          VariableTypeSpecifier('long long'))
        var_int_2 = VariableTypeSpecifier('map',
                                          VariableTypeSpecifier('int'),
                                          VariableTypeSpecifier('unsigned long long'))
        self.assertNotEqual(var_int_1, var_int_2)


if __name__ == '__main__':
    unittest.main()
