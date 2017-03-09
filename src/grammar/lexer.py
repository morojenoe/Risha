reserved = {
    'false': 'FALSE',
    'true': 'TRUE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'using': 'USING',
    'static': 'STATIC',
    'enum': 'ENUM',
    'class': 'CLASS',
    'struct': 'STRUCT',
    'char': 'CHAR',
    'bool': 'BOOL',
    'short': 'SHORT',
    'int': 'INT',
    'long': 'LONG',
    'ushort': 'USHORT',
    'uint': 'UINT',
    'ulong': 'ULONG',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'void': 'VOID',
    'auto': 'AUTO',
    'const': 'CONST',
    'operator': 'OPERATOR',
    'ref': 'REF',
}

tokens = [
             'IDENTIFIER',
             'BINARY_NUMBER',
             'OCTAL_NUMBER',
             'DECIMAL_NUMBER',
             'HEXADECIMAL_NUMBER',
             'CHARACTER_LITERAL',
             'FLOATING_NUMBER',
             'STRING_LITERAL',
             'ASSIGNMENT',
             'MUL_EQUAL',
             'DIV_EQUAL',
             'MOD_EQUAL',
             'PLUS_EQUAL',
             'MINUS_EQUAL',
             'SHIFT_RIGHT_EQUAL',
             'SHIFT_LEFT_EQUAL',
             'AND_EQUAL',
             'OR_EQUAL',
             'XOR_EQUAL',
             'COMMA',
             'QUESTION',
             'COLON',
             'LOGICAL_OR',
             'LOGICAL_AND',
             'BITWISE_OR',
             'BITWISE_AND',
             'BITWISE_EXCLUSIVE_OR',
             'EQUALITY',
             'INEQUALITY',
             'LESS',
             'LESS_OR_EQUAL',
             'GREATER',
             'GREATER_OR_EQUAL',
             'SHIFT_LEFT',
             'SHIFT_RIGHT',
             'PLUS',
             'MINUS',
             'MULTIPLY',
             'DIVISION',
             'MODULO',
             'L_PAREN',
             'R_PAREN',
             'L_BRACKET',
             'R_BRACKET',
             'L_CURLY',
             'R_CURLY',
             'INCREMENT',
             'DECREMENT',
             'LOGICAL_NOT',
             'BITWISE_NOT',
             'DOT',
             'SEMICOLON',
         ] + list(reserved.values())

t_BINARY_NUMBER = r'0[b|B][0|1](_?[0|1])*(LLU|ULL|LL|U)?'
t_OCTAL_NUMBER = r'0(_?[0-7])*(LLU|ULL|LL|U)?'
t_DECIMAL_NUMBER = r'[1-9](_?\d)*(LLU|ULL|LL|U)?'
t_HEXADECIMAL_NUMBER = r"0[x|X][0-9a-fA-F](_?[0-9a-fA-F])*(LLU|ULL|LL|U)?"
t_CHARACTER_LITERAL = \
    r'\'([^\\\'\"\n\t\v\b\r]|\\\'|\\n|\\t|\\v|\\b|\\r|\\\\|\\\'|\\\")\''
t_FLOATING_NUMBER = \
    r'((\d+[eE][+-]?\d+)|((\d*\.\d+)|(\d+\.))([eE][+-]?\d+)?)(F|L)?'
t_STRING_LITERAL = \
    r'"([^\\\"\\\n\\\\]|\\\\|\\\'|\\\"|\\a|\\b|\\f|\\n|\\r|\\t|\\v)*"'
t_ASSIGNMENT = r'='
t_MUL_EQUAL = r'\*='
t_DIV_EQUAL = r'/='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_SHIFT_RIGHT_EQUAL = r'>>='
t_SHIFT_LEFT_EQUAL = r'<<='
t_AND_EQUAL = r'&='
t_OR_EQUAL = r'\|='
t_XOR_EQUAL = r'^='
t_COMMA = r','
t_QUESTION = r'\?'
t_COLON = r':'
t_LOGICAL_OR = r'\|\|'
t_LOGICAL_AND = r'&&'
t_BITWISE_OR = r'\|'
t_BITWISE_AND = r'&'
t_BITWISE_EXCLUSIVE_OR = r'\^'
t_EQUALITY = r'=='
t_INEQUALITY = r'!='
t_LESS = r'<'
t_LESS_OR_EQUAL = r'<='
t_GREATER = r'>'
t_GREATER_OR_EQUAL = r'>='
t_SHIFT_LEFT = r'<<'
t_SHIFT_RIGHT = r'>>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_L_BRACKET = r'\['
t_R_BRACKET = r'\]'
t_L_CURLY = r'\{'
t_R_CURLY = r'\}'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_LOGICAL_NOT = r'!'
t_BITWISE_NOT = r'~'
t_DOT = r'\.'
t_SEMICOLON = r';'
t_ignore = ' \t'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][0-9a-zA-Z_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n'
    t.lexer.lineno += t.value.count("\n")
