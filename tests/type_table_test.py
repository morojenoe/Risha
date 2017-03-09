import unittest

import src.ast_visitors.semantic_analysis.type_table as type_table
import src.ast_visitors.semantic_analysis.symbol_table_types as st_types


class TypeTableTest(unittest.TestCase):
    def test_type_table(self):
        table = type_table.TypeTable()
        table.add_type(st_types.VariableTypeSpecifier('int'))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
