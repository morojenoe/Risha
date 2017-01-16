import unittest

from src.ast_visitors.semantic_analysis.type_table import VariableClass


class VariableClassTest(unittest.TestCase):
    def test_equality(self):
        var_int_1 = VariableClass('int')
        var_int_2 = VariableClass('int')
        self.assertEqual(var_int_1, var_int_2)

    def test_template_equality(self):
        var_int_1 = VariableClass('vector', 'int', 'allocator', 'int')
        var_int_2 = VariableClass('vector', 'int', 'allocator', 'int')
        self.assertEqual(var_int_1, var_int_2)

    def test_inequality(self):
        var_int_1 = VariableClass('string')
        var_int_2 = VariableClass('char')
        self.assertNotEqual(var_int_1, var_int_2)

    def test_template_inequality(self):
        var_int_1 = VariableClass('map', 'int', 'long long')
        var_int_2 = VariableClass('map', 'int', 'unsigned long long')
        self.assertNotEqual(var_int_1, var_int_2)


if __name__ == '__main__':
    unittest.main()
