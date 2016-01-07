import ply.lex
import ply.yacc
import cpl_ast
import cpl_ast_traverse

reserved = {
    'false': 'FALSE',
    'true': 'TRUE',
    'this': 'THIS',
    'case': 'CASE',
    'default': 'DEFAULT',
    'if': 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'using': 'USING',
    'static': 'STATIC',
    'inline': 'INLINE',
    'enum': 'ENUM',
    'class': 'CLASS',
    'struct': 'STRUCT',
    'char': 'CHAR',
    'bool': 'BOOL',
    'short': 'SHORT',
    'int': 'INT',
    'signed': 'SIGNED',
    'unsigned': 'UNSIGNED',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'void': 'VOID',
    'auto': 'AUTO',
    'const': 'CONST',
    'typedef': 'TYPEDEF',
    'operator': 'OPERATOR'
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
             'SCOPE_RESOLUTION_OPERATOR',
             'SEMICOLON',
             'ARROW'
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
t_SCOPE_RESOLUTION_OPERATOR = r'::'
t_SEMICOLON = r';'
t_ARROW = r'->'

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


start = 'translation-unit'


def p_error(p):
    print("Syntax error at {}".format(p))


def p_empty(p):
    """ empty :  """
    pass


def p_translation_unit(p):
    """ translation-unit : declaration-seq
                         | empty """
    pass


"""
 Literals
"""


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


"""
 Expressions
"""


def p_constant_expression(p):
    """ constant-expression : conditional-expression """
    pass


def p_expression(p):
    """ expression : assignment-expression
                   | expression COMMA assignment-expression """
    pass


def p_assignment_expression(p):
    """ assignment-expression : conditional-expression
                              | logical-or-expression assignment-operator initializer-clause """
    pass


def p_assignment_operator(p):
    """ assignment-operator : ASSIGNMENT
                            | MUL_EQUAL
                            | DIV_EQUAL
                            | MOD_EQUAL
                            | PLUS_EQUAL
                            | MINUS_EQUAL
                            | SHIFT_RIGHT_EQUAL
                            | SHIFT_LEFT_EQUAL
                            | AND_EQUAL
                            | OR_EQUAL
                            | XOR_EQUAL """
    pass


def p_conditional_expression(p):
    """ conditional-expression : logical-or-expression
                               | logical-or-expression QUESTION expression COLON assignment-expression """
    pass


def p_logical_or_expression(p):
    """ logical-or-expression : logical-and-expression
                              | logical-or-expression LOGICAL_OR logical-and-expression """
    pass


def p_logical_and_expression(p):
    """ logical-and-expression : inclusive-or-expression
                               | logical-and-expression LOGICAL_AND inclusive-or-expression """
    pass


def p_inclusive_or_expression(p):
    """ inclusive-or-expression : exclusive-or-expression
                                | inclusive-or-expression BITWISE_OR exclusive-or-expression """
    pass


def p_exclusive_or_expression(p):
    """ exclusive-or-expression : and-expression
                                | exclusive-or-expression BITWISE_EXCLUSIVE_OR and-expression """
    pass


def p_and_expression(p):
    """ and-expression : equality-expression
                       | and-expression BITWISE_AND equality-expression """
    pass


def p_equality_expression(p):
    """ equality-expression : relational-expression
                            | equality-expression EQUALITY relational-expression
                            | equality-expression INEQUALITY relational-expression """
    pass


def p_relational_expression(p):
    """ relational-expression : shift-expression
                              | relational-expression LESS shift-expression
                              | relational-expression LESS_OR_EQUAL shift-expression
                              | relational-expression GREATER shift-expression
                              | relational-expression GREATER_OR_EQUAL shift-expression """
    pass


def p_shift_expression(p):
    """ shift-expression : additive-expression
                         | shift-expression SHIFT_LEFT additive-expression
                         | shift-expression SHIFT_RIGHT additive-expression """
    pass


def p_additive_expression(p):
    """ additive-expression : multiplicative-expression
                            | additive-expression PLUS multiplicative-expression
                            | additive-expression MINUS multiplicative-expression """
    pass


def p_multiplicative_expression(p):
    """ multiplicative-expression : cast-expression
                                  | multiplicative-expression MULTIPLY cast-expression
                                  | multiplicative-expression DIVISION cast-expression
                                  | multiplicative-expression MODULO cast-expression """
    pass


def p_cast_expression(p):
    """ cast-expression : unary-expression
                        | L_PAREN type-id R_PAREN cast-expression """
    pass


def p_unary_expression(p):
    """ unary-expression : postfix-expression
                         | INCREMENT cast-expression
                         | DECREMENT cast-expression
                         | unary-operator cast-expression """
    pass


def p_unary_operator(p):
    """ unary-operator : PLUS
                       | MINUS
                       | LOGICAL_NOT
                       | BITWISE_NOT """
    pass


def p_postfix_expression(p):
    """ postfix-expression : primary-expression
                           | postfix-expression L_BRACKET expression R_BRACKET
                           | postfix-expression L_PAREN R_PAREN
                           | postfix-expression L_PAREN  expression-list  R_PAREN
                           | simple-type-specifier L_PAREN R_PAREN
                           | simple-type-specifier L_PAREN expression-list R_PAREN
                           | postfix-expression DOT id-expression
                           | postfix-expression INCREMENT
                           | postfix-expression DECREMENT """
    pass


def p_primary_expression(p):
    """ primary-expression : literal
                           | THIS
                           | L_PAREN expression R_PAREN
                           | id-expression """
    pass


def p_id_expression(p):
    """ id-expression : unqualified-id
                      | qualified-id """
    pass


def p_qualified_id(p):
    """ qualified-id : nested-name-specifier unqualified-id """
    pass


def p_unqualified_id(p):
    """ unqualified-id : IDENTIFIER
                       | operator-function-id """
    pass


def p_nested_name_specifier(p):
    """ nested-name-specifier : SCOPE_RESOLUTION_OPERATOR
                              | type-name SCOPE_RESOLUTION_OPERATOR
                              | nested-name-specifier IDENTIFIER SCOPE_RESOLUTION_OPERATOR """
    pass


def p_expression_list(p):
    """ expression-list : initializer-list """
    pass


"""
 Statements
"""


def p_statement(p):
    """ statement : labeled-statement
                  | expression-statement
                  | compound-statement
                  | selection-statement
                  | iteration-statement
                  | jump-statement
                  | declaration-statement """
    pass


def p_labeled_statement(p):
    """ labeled-statement : IDENTIFIER COLON statement
                          | CASE constant-expression COLON statement
                          | DEFAULT COLON statement """
    pass


def p_expression_statement(p):
    """ expression-statement : expression SEMICOLON
                             | SEMICOLON """
    pass


def p_compound_statement(p):
    """ compound-statement : L_CURLY statement-seq R_CURLY
                           | L_CURLY R_CURLY """
    pass


def p_statement_seq(p):
    """ statement-seq : statement
                      | statement-seq statement """
    pass


def p_selection_statement(p):
    """ selection-statement : IF L_PAREN condition R_PAREN statement
                            | IF L_PAREN condition R_PAREN statement ELSE statement
                            | SWITCH L_PAREN condition R_PAREN statement """
    pass


def p_condition(p):
    """ condition : expression
                  | declarator ASSIGNMENT initializer-clause
                  | declarator braced-init-list """
    pass


def p_iteration_statement(p):
    """ iteration-statement : WHILE L_PAREN condition R_PAREN statement
                            | DO statement WHILE L_PAREN expression R_PAREN SEMICOLON
                            | FOR L_PAREN for-init-statement SEMICOLON R_PAREN statement
                            | FOR L_PAREN for-init-statement condition SEMICOLON R_PAREN statement
                            | FOR L_PAREN for-init-statement SEMICOLON expression R_PAREN statement
                            | FOR L_PAREN for-init-statement condition SEMICOLON expression R_PAREN statement
                            | FOR L_PAREN for-range-declaration COLON for-range-initializer R_PAREN statement """
    pass


def p_for_init_statement(p):
    """ for-init-statement : expression-statement
                           | simple-declaration """
    pass


def p_for_range_declaration(p):
    """ for-range-declaration : decl-specifier-seq declarator """
    pass


def p_for_range_initializer(p):
    """ for-range-initializer : expression
                              | braced-init-list """
    pass


def p_jump_statement(p):
    """ jump-statement : BREAK SEMICOLON
                       | CONTINUE SEMICOLON
                       | RETURN SEMICOLON
                       | RETURN expression SEMICOLON
                       | RETURN braced-init-list SEMICOLON """
    pass


def p_declaration_statement(p):
    """ declaration-statement : block-declaration """
    pass


def p_declaration_seq(p):
    """ declaration-seq : declaration
                        | declaration-seq declaration """
    pass


def p_declaration(p):
    """ declaration : block-declaration
                    | function-definition
                    | empty-declaration """
    pass


def p_block_declaration(p):
    """ block-declaration : simple-declaration
                          | alias-declaration
                          | opaque-enum-declaration """
    pass


def p_alias_declaration(p):
    """ alias-declaration : USING IDENTIFIER ASSIGNMENT type-id """
    pass


def p_simple_declaration(p):
    """ simple-declaration : decl-specifier-seq init-declarator-list SEMICOLON
                           | decl-specifier-seq SEMICOLON
                           | init-declarator-list SEMICOLON
                           | SEMICOLON
                           | """
    pass


def p_empty_declaration(p):
    """ empty-declaration : SEMICOLON """
    pass


def p_decl_specifier(p):
    """ decl-specifier : storage-class-specifier
                       | type-specifier
                       | function-specifier
                       | TYPEDEF """
    pass


def p_decl_specifier_seq(p):
    """ decl-specifier-seq : decl-specifier
                           | decl-specifier-seq decl-specifier """
    pass


def p_storage_class_specifier(p):
    """ storage-class-specifier : STATIC """
    pass


def p_function_specifier(p):
    """ function-specifier : INLINE """
    pass


def p_typedef_name(p):
    """ typedef-name : IDENTIFIER """
    pass


def p_type_specifier(p):
    """ type-specifier : trailing-type-specifier
                       | class-specifier
                       | enum-specifier """
    pass


def p_type_specifier_seq(p):
    """ type-specifier-seq : type-specifier
                           | type-specifier type-specifier-seq """
    pass


def p_trailing_type_specifier(p):
    """ trailing-type-specifier : simple-type-specifier
                                | elaborated-type-specifier
                                | cv-qualifier """
    pass


def p_trailing_type_specifier_seq(p):
    """ trailing-type-specifier-seq : trailing-type-specifier
                                    | trailing-type-specifier trailing-type-specifier-seq """
    pass


def p_simple_type_specifier(p):
    """ simple-type-specifier : nested-name-specifier type-name
                              | type-name
                              | CHAR
                              | BOOL
                              | SHORT
                              | INT
                              | SIGNED
                              | UNSIGNED
                              | FLOAT
                              | DOUBLE
                              | VOID
                              | AUTO """
    pass


def p_type_name(p):
    """ type-name : class-name
                  | enum-name
                  | typedef-name """
    pass


def p_elaborated_type_specifier(p):
    """ elaborated-type-specifier : class-key nested-name-specifier IDENTIFIER
                                  | class-key IDENTIFIER
                                  | ENUM nested-name-specifier IDENTIFIER
                                  | ENUM IDENTIFIER """
    pass


def p_enum_name(p):
    """ enum-name : IDENTIFIER """
    pass


def p_enum_specifier(p):
    """ enum-specifier : enum-head L_CURLY R_CURLY
                       | enum-head L_CURLY enumerator-list R_CURLY
                       | enum-head L_CURLY enumerator-list COMMA R_CURLY """
    pass


def p_enum_head(p):
    """ enum-head : enum-key
                  | enum-key IDENTIFIER
                  | enum-key enum-base
                  | enum-key IDENTIFIER enum-base
                  | enum-key nested-name-specifier IDENTIFIER
                  | enum-key nested-name-specifier IDENTIFIER enum-base """
    pass


def p_opaque_enum_declaration(p):
    """ opaque-enum-declaration : enum-key IDENTIFIER
                                | enum-key IDENTIFIER enum-base """
    pass


def p_enum_key(p):
    """ enum-key : ENUM
                 | ENUM CLASS
                 | ENUM STRUCT """
    pass


def p_enum_base(p):
    """ enum-base : COLON type-specifier-seq """
    pass


def p_enumerator_list(p):
    """ enumerator-list : enumerator-definition
                        | enumerator-list COMMA enumerator-definition """
    pass


def p_enumerator_definition(p):
    """ enumerator-definition : enumerator
                              | enumerator ASSIGNMENT constant-expression """
    pass


def p_enumerator(p):
    """ enumerator : IDENTIFIER """
    pass


"""
 Declarators
"""


def p_init_declarator_list(p):
    """ init-declarator-list : init-declarator
                             | init-declarator-list COMMA init-declarator """
    pass


def p_init_declarator(p):
    """ init-declarator : declarator
                        | declarator initializer """
    pass


def p_declarator(p):
    """ declarator : noptr-declarator
                   | noptr-declarator parameters-and-qualifiers trailing-return-type """
    pass


def p_noptr_declarator(p):
    """ noptr-declarator : declarator-id
                         | noptr-declarator parameters-and-qualifiers
                         | noptr-declarator L_BRACKET constant-expression R_BRACKET
                         | noptr-declarator L_BRACKET  R_BRACKET
                         | L_PAREN noptr-declarator R_PAREN """
    pass


def p_parameters_and_qualifiers(p):
    """ parameters-and-qualifiers : L_PAREN parameter-declaration-clause R_PAREN
                                  | L_PAREN parameter-declaration-clause R_PAREN cv-qualifier-seq
                                  | L_PAREN parameter-declaration-clause R_PAREN ref-qualifier
                                  | L_PAREN parameter-declaration-clause R_PAREN cv-qualifier-seq ref-qualifier """
    pass


def p_trailing_return_type(p):
    """ trailing-return-type : ARROW trailing-type-specifier-seq
                             | ARROW trailing-type-specifier-seq abstract-declarator """
    pass


def p_cv_qualifier_seq(p):
    """ cv-qualifier-seq : cv-qualifier
                         | cv-qualifier cv-qualifier-seq """
    pass


def p_cv_qualifier(p):
    """ cv-qualifier : CONST """
    pass


def p_ref_qualifier(p):
    """ ref-qualifier : LOGICAL_AND
                      | BITWISE_AND """
    pass


def p_declarator_id(p):
    """ declarator-id : id-expression """
    pass


"""
 Declarators.type-names
"""


def p_type_id(p):
    """ type-id : type-specifier-seq
                | type-specifier-seq abstract-declarator """
    pass


def p_abstract_declarator(p):
    """ abstract-declarator : noptr-abstract-declarator
                            | parameters-and-qualifiers trailing-return-type
                            | noptr-abstract-declarator parameters-and-qualifiers trailing-return-type
                            | abstract-pack-declarator """
    pass


def p_noptr_abstract_declarator(p):
    """ noptr-abstract-declarator : noptr-abstract-declarator parameters-and-qualifiers
                                  | parameters-and-qualifiers
                                  | noptr-abstract-declarator L_BRACKET constant-expression R_BRACKET
                                  | noptr-abstract-declarator L_BRACKET  R_BRACKET
                                  | L_BRACKET constant-expression R_BRACKET
                                  | L_BRACKET R_BRACKET
                                  | L_PAREN noptr-abstract-declarator R_PAREN """
    pass


def p_abstract_pack_declarator(p):
    """ abstract-pack-declarator : noptr-abstract-pack-declarator """
    pass


def p_noptr_abstract_pack_declarator(p):
    """ noptr-abstract-pack-declarator : noptr-abstract-pack-declarator parameters-and-qualifiers
                                       | noptr-abstract-pack-declarator L_BRACKET R_BRACKET
                                       | noptr-abstract-pack-declarator L_BRACKET constant-expression R_BRACKET
                                       | empty """
    pass


"""
 Declarators.functions
"""


def p_parameter_declaration_clause(p):
    """ parameter-declaration-clause : empty
                                   | parameter-declaration-list """
    pass


def p_parameter_declaration_list(p):
    """ parameter-declaration-list : parameter-declaration
                                   | parameter-declaration-list COMMA parameter-declaration """
    pass


def p_parameter_declaration(p):
    """ parameter-declaration : decl-specifier-seq declarator
                              | decl-specifier-seq declarator ASSIGNMENT initializer-clause
                              | decl-specifier-seq abstract-declarator
                              | decl-specifier-seq
                              | decl-specifier-seq abstract-declarator ASSIGNMENT initializer-clause
                              | decl-specifier-seq ASSIGNMENT initializer-clause """
    pass


def p_function_definition(p):
    """ function-definition : decl-specifier-seq declaration function-body
                            | declaration function-body """
    pass


def p_function_body(p):
    """ function-body : compound-statement """
    pass


"""
 Declarators.initializers
"""


def p_initializer(p):
    """ initializer : brace-or-equal-initializer
                    | L_PAREN expression-list R_PAREN """
    pass


def p_brace_or_equal_initializer(p):
    """ brace-or-equal-initializer : ASSIGNMENT initializer-clause
                                   | braced-init-list """
    pass


def p_initializer_clause(p):
    """ initializer-clause : assignment-expression
                           | braced-init-list """
    pass


def p_initializer_list(p):
    """ initializer-list : initializer-clause
                         | initializer-list COMMA initializer-clause """
    pass


def p_braced_init_list(p):
    """ braced-init-list : L_CURLY initializer-list R_CURLY
                         | L_CURLY initializer-list COMMA R_CURLY
                         | L_CURLY R_CURLY """
    pass


"""
 Classes
"""


def p_class_name(p):
    """ class-name : IDENTIFIER """
    pass


def p_class_specifier(p):
    """ class-specifier : class-head L_CURLY R_CURLY
                        | class-head L_CURLY member-specification R_CURLY """
    pass


def p_class_head(p):
    """ class-head : class-key class-head-name """
    pass


def p_class_head_name(p):
    """ class-head-name : class-name
                        | nested-name-specifier class-name"""
    pass


def p_class_key(p):
    """ class-key : CLASS
                  | STRUCT """


def p_member_specification(p):
    """ member-specification : member-declaration
                             | member-declaration member-specification """
    pass


def p_member_declaration(p):
    """ member-declaration : empty-declaration
                           | decl-specifier-seq SEMICOLON
                           | member-declarator-list SEMICOLON
                           | decl-specifier-seq member-declarator-list SEMICOLON
                           | alias-declaration
                           | function-definition """
    pass


def p_member_declarator_list(p):
    """ member-declarator-list : member-declarator
                               | member-declarator-list COMMA member-declarator """
    pass


def p_member_declarator(p):
    """ member-declarator : declarator
                          | declarator brace-or-equal-initializer """
    pass


"""
 Overloading
"""


def p_operator_function_id(p):
    """ operator-function-id : OPERATOR operator """
    pass


def p_operator(p):
    """ operator : ASSIGNMENT
                 | MUL_EQUAL
                 | DIV_EQUAL
                 | MOD_EQUAL
                 | PLUS_EQUAL
                 | MINUS_EQUAL
                 | SHIFT_RIGHT_EQUAL
                 | SHIFT_LEFT_EQUAL
                 | AND_EQUAL
                 | OR_EQUAL
                 | XOR_EQUAL
                 | LOGICAL_OR
                 | LOGICAL_AND
                 | BITWISE_OR
                 | BITWISE_AND
                 | BITWISE_EXCLUSIVE_OR
                 | EQUALITY
                 | INEQUALITY
                 | LESS
                 | LESS_OR_EQUAL
                 | GREATER
                 | GREATER_OR_EQUAL
                 | SHIFT_LEFT
                 | SHIFT_RIGHT
                 | PLUS
                 | MINUS
                 | MULTIPLY
                 | DIVISION
                 | MODULO
                 | LOGICAL_NOT
                 | BITWISE_NOT """
    pass


lexer = ply.lex.lex()
parser = ply.yacc.yacc()
print(parser.parse(input=r'int a(){}', lexer=lexer, debug=False))
# cpl_ast_traverse.generate_cpp(parser.parse(input="10"))
