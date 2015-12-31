import ply.lex
import ply.yacc
import cpl_ast
import cpl_ast_traverse

reserved = {
    'false': 'FALSE',
    'true': 'TRUE'
}

literals = ""

tokens = [
             'IDENTIFIER',
             'BINARY_NUMBER',
             'OCTAL_NUMBER',
             'DECIMAL_NUMBER',
             'HEXADECIMAL_NUMBER',
             'CHARACTER_LITERAL',
             'FLOATING_NUMBER',
             'STRING_LITERAL'
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

t_ignore = ' \t'


def t_IDENTIFIER(t):
    r""" [a-zA-Z_][0-9a-zA-Z_]* """
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r""" \n """
    t.lexer.lineno += t.value.count("\n")


def p_error(p):
    print("Syntax error at {}".format(p.value))


def p_literal(p):
    """ literal : integer-literal
                | CHARACTER_LITERAL
                | FLOATING_NUMBER
                | STRING_LITERAL
                | boolean-literal """
    p[0] = p[1]


def p_integer_literal(p):
    """ integer-literal : BINARY_NUMBER
                        | OCTAL_NUMBER
                        | DECIMAL_NUMBER
                        | HEXADECIMAL_NUMBER """
    p[0] = p[1]


def p_boolean_literal(p):
    """ boolean-literal : TRUE
                        | FALSE """
    p[0] = p[1]


lexer = ply.lex.lex()
parser = ply.yacc.yacc()
print(parser.parse(input=r'"as\\d\'\"sasd"', lexer=lexer, debug=False))
# cpl_ast_traverse.generate_cpp(parser.parse(input="10"))
