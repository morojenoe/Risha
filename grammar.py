import ply.lex
import ply.yacc
import lexer
import risha_ast
import logging

tokens = lexer.tokens

precedence = (
    ('left', 'COMMA'),
    ('right', 'ASSIGNMENT', 'MUL_EQUAL', 'DIV_EQUAL', 'MOD_EQUAL',
     'PLUS_EQUAL', 'MINUS_EQUAL', 'SHIFT_RIGHT_EQUAL', 'SHIFT_LEFT_EQUAL',
     'AND_EQUAL', 'OR_EQUAL', 'XOR_EQUAL'),
    ('left', 'LOGICAL_OR'),
    ('left', 'LOGICAL_AND'),
    ('left', 'BITWISE_OR'),
    ('left', 'BITWISE_EXCLUSIVE_OR'),
    ('left', 'BITWISE_AND'),
    ('left', 'EQUALITY', 'INEQUALITY'),
    ('left', 'LESS', 'GREATER', 'LESS_OR_EQUAL', 'GREATER_OR_EQUAL'),
    ('left', 'SHIFT_LEFT', 'SHIFT_RIGHT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVISION', 'MODULO'),
    ('right', 'LOGICAL_NOT', 'BITWISE_NOT', 'INCREMENT', 'DECREMENT'),
    # ('left', 'SCOPE_RESOLUTION_OPERATOR'),
)

start = 'translation-unit'


def create_args(p):
    if len(p) == 1:
        p[0] = risha_ast.Node()
    elif len(p) == 2:
        p[0] = risha_ast.Node(p[1])
    elif len(p) == 2:
        p[0] = risha_ast.Node(p[1])
    elif len(p) == 3:
        p[0] = risha_ast.Node(p[1], p[2])
    elif len(p) == 4:
        p[0] = risha_ast.Node(p[1], p[2], p[3])
    elif len(p) == 5:
        p[0] = risha_ast.Node(p[1], p[2], p[3], p[4])
    elif len(p) == 6:
        p[0] = risha_ast.Node(p[1], p[2], p[3], p[4], p[5])
    elif len(p) == 7:
        p[0] = risha_ast.Node(p[1], p[2], p[3], p[4], p[5], p[6])
    elif len(p) == 8:
        p[0] = risha_ast.Node(p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    elif len(p) == 9:
        p[0] = risha_ast.Node(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    else:
        assert False


def p_error(p):
    print("Syntax error at {}".format(p))


def p_empty(p):
    """ empty :  """
    p[0] = None


def p_translation_unit(p):
    """ translation-unit : declaration-seq
                         | empty """
    create_args(p)


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


def build_binary_expression_node(p):
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.BinaryOperation(p[1], p[2], p[3])


def p_constant_expression(p):
    """ constant-expression : conditional-expression """
    p[0] = p[1]


def p_expression(p):
    """ expression : assignment-expression
                   | expression COMMA assignment-expression """
    if len(p) == 2:
        p[0] = risha_ast.ExpressionNode().add_expression(p[1])
    else:
        p[0] = p[1].add_expression(p[3])


def p_assignment_expression(p):
    """ assignment-expression : conditional-expression
                              | logical-or-expression assignment-operator initializer-clause """
    create_args(p)


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
    p[0] = p[1]


def p_conditional_expression(p):
    """ conditional-expression : logical-or-expression
                               | logical-or-expression QUESTION expression COLON assignment-expression """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.TernaryOperationNode(p[1], p[3], p[5])


def p_logical_or_expression(p):
    """ logical-or-expression : logical-and-expression
                              | logical-or-expression LOGICAL_OR logical-and-expression """
    build_binary_expression_node(p)


def p_logical_and_expression(p):
    """ logical-and-expression : inclusive-or-expression
                               | logical-and-expression LOGICAL_AND inclusive-or-expression """
    build_binary_expression_node(p)


def p_inclusive_or_expression(p):
    """ inclusive-or-expression : exclusive-or-expression
                                | inclusive-or-expression BITWISE_OR exclusive-or-expression """
    build_binary_expression_node(p)


def p_exclusive_or_expression(p):
    """ exclusive-or-expression : and-expression
                                | exclusive-or-expression BITWISE_EXCLUSIVE_OR and-expression """
    build_binary_expression_node(p)


def p_and_expression(p):
    """ and-expression : equality-expression
                       | and-expression BITWISE_AND equality-expression """
    build_binary_expression_node(p)


def p_equality_expression(p):
    """ equality-expression : relational-expression
                            | equality-expression EQUALITY relational-expression
                            | equality-expression INEQUALITY relational-expression """
    build_binary_expression_node(p)


def p_relational_expression(p):
    """ relational-expression : shift-expression
                              | relational-expression LESS shift-expression
                              | relational-expression LESS_OR_EQUAL shift-expression
                              | relational-expression GREATER shift-expression
                              | relational-expression GREATER_OR_EQUAL shift-expression """
    build_binary_expression_node(p)


def p_shift_expression(p):
    """ shift-expression : additive-expression
                         | shift-expression SHIFT_LEFT additive-expression
                         | shift-expression SHIFT_RIGHT additive-expression """
    build_binary_expression_node(p)


def p_additive_expression(p):
    """ additive-expression : multiplicative-expression
                            | additive-expression PLUS multiplicative-expression
                            | additive-expression MINUS multiplicative-expression """
    build_binary_expression_node(p)


def p_multiplicative_expression(p):
    """ multiplicative-expression : cast-expression
                                  | multiplicative-expression MULTIPLY cast-expression
                                  | multiplicative-expression DIVISION cast-expression
                                  | multiplicative-expression MODULO cast-expression """
    build_binary_expression_node(p)


def p_cast_expression(p):
    """ cast-expression : unary-expression
                        | L_PAREN type-id R_PAREN cast-expression """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.CastExpression(p[4], p[2])


def p_unary_expression(p):
    """ unary-expression : postfix-expression
                         | INCREMENT cast-expression
                         | DECREMENT cast-expression
                         | unary-operator cast-expression """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.PrefixUnaryExpressionNode(p[1], p[2])


def p_unary_operator(p):
    """ unary-operator : PLUS
                       | MINUS
                       | LOGICAL_NOT
                       | BITWISE_NOT """
    p[0] = p[1]


def p_postfix_expression(p):
    """ postfix-expression : primary-expression
                           | postfix-expression L_BRACKET expression R_BRACKET
                           | postfix-expression L_BRACKET braced-init-list R_BRACKET
                           | postfix-expression DOT id-expression """
    create_args(p)


def p_postfix_expression_func_call(p):
    """ postfix-expression : postfix-expression L_PAREN R_PAREN
                           | postfix-expression L_PAREN  expression-list  R_PAREN
                           | simple-type-specifier L_PAREN R_PAREN
                           | simple-type-specifier L_PAREN expression-list R_PAREN """
    if len(p) == 4:
        # TODO: change none to empty ExpressionListNode
        p[0] = risha_ast.FunctionCallNode(p[1], None)
    else:
        p[0] = risha_ast.FunctionCallNode(p[1], p[3])


def p_postfix_expression_inc_dec(p):
    """ postfix-expression : postfix-expression INCREMENT
                           | postfix-expression DECREMENT """
    p[0] = risha_ast.PostfixUnaryExpressionNode(p[1], p[2])


def p_primary_expression(p):
    """ primary-expression : literal
                           | L_PAREN expression R_PAREN
                           | id-expression """
    #                      | THIS
    create_args(p)


def p_id_expression(p):
    """ id-expression : unqualified-id """
    #                 | qualified-id
    p[0] = p[1]


# def p_qualified_id(p):
#     """ qualified-id : nested-name-specifier unqualified-id """
#     create_args(p)


def p_unqualified_id(p):
    """ unqualified-id : IDENTIFIER
                       | operator-function-id """
    p[0] = p[1]


# def p_nested_name_specifier(p):
#     """ nested-name-specifier : SCOPE_RESOLUTION_OPERATOR
#                               | type-name SCOPE_RESOLUTION_OPERATOR
#                               | nested-name-specifier IDENTIFIER SCOPE_RESOLUTION_OPERATOR """
#     create_args(p)


def p_expression_list(p):
    """ expression-list : initializer-list """
    p[0] = p[1]


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
    p[0] = p[1]


def p_labeled_statement(p):
    """ labeled-statement : IDENTIFIER COLON statement
                          | CASE constant-expression COLON statement
                          | DEFAULT COLON statement """
    create_args(p)


def p_expression_statement(p):
    """ expression-statement : expression SEMICOLON
                             | SEMICOLON """
    create_args(p)


def p_compound_statement(p):
    """ compound-statement : L_CURLY statement-seq R_CURLY
                           | L_CURLY R_CURLY """
    if len(p) == 4:
        p[0] = risha_ast.CompoundStatementNode(p[2])
    else:
        p[0] = risha_ast.CompoundStatementNode(None)


def p_statement_seq(p):
    """ statement-seq : statement
                      | statement-seq statement """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = list(p[1]) + [p[2]]


def p_selection_statement(p):
    """ selection-statement : SWITCH L_PAREN condition R_PAREN statement """
    create_args(p)


def p_selection_statement_if(p):
    """ selection-statement : IF L_PAREN condition R_PAREN statement
                            | IF L_PAREN condition R_PAREN statement ELSE statement """
    if len(p) == 6:
        p[0] = risha_ast.IfNode(p[3], p[5], None)
    else:
        p[0] = risha_ast.IfNode(p[3], p[5], p[7])


def p_condition(p):
    """ condition : expression
                  | declarator ASSIGNMENT initializer-clause
                  | declarator braced-init-list """
    create_args(p)


def p_iteration_statement(p):
    """ iteration-statement : WHILE L_PAREN condition R_PAREN statement
                            | DO statement WHILE L_PAREN expression R_PAREN SEMICOLON
                            | FOR L_PAREN for-range-declaration COLON for-range-initializer R_PAREN statement """
    create_args(p)


def p_iteration_for_statement(p):
    """ iteration-statement : FOR L_PAREN for-init-statement SEMICOLON R_PAREN statement
                            | FOR L_PAREN for-init-statement SEMICOLON expression R_PAREN statement
                            | FOR L_PAREN for-init-statement condition SEMICOLON expression R_PAREN statement """
    if len(p) == 7:
        p[0] = risha_ast.ForNode(p[3], None, None, p[6])
    elif len(p) == 8:
        p[0] = risha_ast.ForNode(p[3], None, p[5], p[7])
    elif len(p) == 9:
        p[0] = risha_ast.ForNode(p[3], p[4], p[6], p[8])


def p_iteration_for_statement_with_condition(p):
    """ iteration-statement : FOR L_PAREN for-init-statement condition SEMICOLON R_PAREN statement """
    p[0] = risha_ast.ForNode(p[3], p[4], None, p[7])


def p_for_init_statement(p):
    """ for-init-statement : expression-statement
                           | simple-declaration """
    create_args(p)


def p_for_range_declaration(p):
    """ for-range-declaration : decl-specifier-seq declarator """
    create_args(p)


def p_for_range_initializer(p):
    """ for-range-initializer : expression
                              | braced-init-list """
    create_args(p)


def p_jump_statement(p):
    """ jump-statement : BREAK SEMICOLON
                       | CONTINUE SEMICOLON
                       | RETURN SEMICOLON
                       | RETURN expression SEMICOLON
                       | RETURN braced-init-list SEMICOLON """
    create_args(p)


def p_declaration_statement(p):
    """ declaration-statement : block-declaration """
    p[0] = p[1]


"""
  Declarations
"""


def p_declaration_seq(p):
    """ declaration-seq : declaration
                        | declaration-seq declaration """
    create_args(p)
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = list(p[1]) + [p[2]]


def p_declaration(p):
    """ declaration : block-declaration
                    | function-definition
                    | empty-declaration """
    p[0] = p[1]


def p_block_declaration(p):
    """ block-declaration : simple-declaration
                          | alias-declaration
                          | opaque-enum-declaration """
    p[0] = p[1]


def p_alias_declaration(p):
    """ alias-declaration : USING IDENTIFIER ASSIGNMENT type-id SEMICOLON """
    p[0] = risha_ast.AliasDeclarationNode(p[2], p[4])


def p_simple_declaration(p):
    """ simple-declaration : decl-specifier-seq init-declarator-list SEMICOLON
                           | decl-specifier-seq SEMICOLON
                           | init-declarator-list SEMICOLON
                           | SEMICOLON
                           | """
    create_args(p)


def p_empty_declaration(p):
    """ empty-declaration : SEMICOLON """
    p[0] = p[1]


def p_decl_specifier(p):
    """ decl-specifier : storage-class-specifier
                       | type-specifier
                       | function-specifier
                       | TYPEDEF """
    create_args(p)


def p_decl_specifier_seq(p):
    """ decl-specifier-seq : decl-specifier
                           | decl-specifier-seq decl-specifier """
    create_args(p)
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = list(p[1]) + [p[2]]


def p_storage_class_specifier(p):
    """ storage-class-specifier : STATIC """
    p[0] = p[1]


def p_function_specifier(p):
    """ function-specifier : INLINE """
    p[0] = p[1]


def p_typedef_name(p):
    """ typedef-name : IDENTIFIER """
    p[0] = p[1]


def p_type_specifier(p):
    """ type-specifier : trailing-type-specifier
                       | class-specifier
                       | enum-specifier """
    p[0] = p[1]


def p_type_specifier_seq(p):
    """ type-specifier-seq : type-specifier
                           | type-specifier type-specifier-seq """
    create_args(p)
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = [p[1]] + list(p[2])


def p_trailing_type_specifier(p):
    """ trailing-type-specifier : simple-type-specifier
                                | elaborated-type-specifier
                                | cv-qualifier """
    p[0] = p[1]


def p_trailing_type_specifier_seq(p):
    """ trailing-type-specifier-seq : trailing-type-specifier
                                    | trailing-type-specifier trailing-type-specifier-seq """
    create_args(p)
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = [p[1]] + list(p[2])


def p_simple_type_specifier(p):
    """ simple-type-specifier : type-name
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
    #                         | nested-name-specifier type-name
    create_args(p)


def p_type_name(p):
    """ type-name : class-name
                  | enum-name
                  | typedef-name """
    p[0] = p[1]


def p_elaborated_type_specifier(p):
    """ elaborated-type-specifier : class-key IDENTIFIER
                                  | enum-key IDENTIFIER """
    #                             | class-key nested-name-specifier IDENTIFIER
    #                             | ENUM nested-name-specifier IDENTIFIER
    create_args(p)


"""
  Declarations.Enums
"""


def p_enum_name(p):
    """ enum-name : IDENTIFIER """
    p[0] = p[1]


def p_enum_specifier(p):
    """ enum-specifier : enum-head L_CURLY R_CURLY
                       | enum-head L_CURLY enumerator-list R_CURLY
                       | enum-head L_CURLY enumerator-list COMMA R_CURLY """
    enum_key = p[1][0]
    enum_name = p[1][1]
    if len(p) == 4:
        p[0] = risha_ast.EnumNode(enum_key, enum_name, None)
    else:
        p[0] = risha_ast.EnumNode(enum_key, enum_name, p[3])


def p_enum_head(p):
    """ enum-head : enum-key
                  | enum-key IDENTIFIER """
    #             | enum-key enum-base
    #             | enum-key IDENTIFIER enum-base
    #             | enum-key nested-name-specifier IDENTIFIER
    #             | enum-key nested-name-specifier IDENTIFIER enum-base
    p[0] = (p[1], None) if len(p) == 2 else (p[1], p[2])


def p_opaque_enum_declaration(p):
    """ opaque-enum-declaration : enum-key IDENTIFIER """
    #                           | enum-key IDENTIFIER enum-base
    create_args(p)


def p_enum_key(p):
    """ enum-key : ENUM
                 | ENUM CLASS
                 | ENUM STRUCT """
    p[0] = None if len(p) == 2 else p[2]


# def p_enum_base(p):
#     """ enum-base : COLON type-specifier-seq """
#     create_args(p)


def p_enumerator_list(p):
    """ enumerator-list : enumerator-definition
                        | enumerator-list COMMA enumerator-definition """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = list(p[1]) + [p[3]]


def p_enumerator_definition(p):
    """ enumerator-definition : enumerator
                              | enumerator ASSIGNMENT constant-expression """
    if len(p) == 2:
        p[0] = (p[1], None)
    else:
        p[0] = (p[1], p[3])


def p_enumerator(p):
    """ enumerator : IDENTIFIER """
    p[0] = p[1]


"""
 Declarators
"""


def p_init_declarator_list(p):
    """ init-declarator-list : init-declarator
                             | init-declarator-list COMMA init-declarator """
    p[0] = [p[1]] if len(p) == 2 else list(p[1]) + [p[3]]


def p_init_declarator(p):
    """ init-declarator : declarator
                        | declarator initializer """
    create_args(p)


def p_declarator(p):
    """ declarator : noptr-declarator
                   | noptr-declarator parameters-and-qualifiers trailing-return-type """
    create_args(p)


def p_noptr_declarator(p):
    """ noptr-declarator : declarator-id
                         | noptr-declarator parameters-and-qualifiers
                         | noptr-declarator L_BRACKET constant-expression R_BRACKET
                         | noptr-declarator L_BRACKET  R_BRACKET
                         | L_PAREN noptr-declarator R_PAREN """
    create_args(p)


def p_parameters_and_qualifiers(p):
    """ parameters-and-qualifiers : L_PAREN parameter-declaration-clause R_PAREN
                                  | L_PAREN parameter-declaration-clause R_PAREN cv-qualifier-seq
                                  | L_PAREN parameter-declaration-clause R_PAREN ref-qualifier
                                  | L_PAREN parameter-declaration-clause R_PAREN cv-qualifier-seq ref-qualifier """
    create_args(p)


def p_trailing_return_type(p):
    """ trailing-return-type : ARROW trailing-type-specifier-seq
                             | ARROW trailing-type-specifier-seq abstract-declarator """
    create_args(p)


def p_cv_qualifier_seq(p):
    """ cv-qualifier-seq : cv-qualifier
                         | cv-qualifier cv-qualifier-seq """
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + list(p[2])


def p_cv_qualifier(p):
    """ cv-qualifier : CONST """
    p[0] = p[1]


def p_ref_qualifier(p):
    """ ref-qualifier : LOGICAL_AND
                      | BITWISE_AND """
    p[0] = p[1]


def p_declarator_id(p):
    """ declarator-id : id-expression """
    p[0] = p[1]


"""
 Declarators.type-names
"""


def p_type_id(p):
    """ type-id : type-specifier-seq
                | type-specifier-seq abstract-declarator """
    create_args(p)


def p_abstract_declarator(p):
    """ abstract-declarator : noptr-abstract-declarator
                            | parameters-and-qualifiers trailing-return-type
                            | noptr-abstract-declarator parameters-and-qualifiers trailing-return-type
                            | abstract-pack-declarator """
    create_args(p)


def p_noptr_abstract_declarator(p):
    """ noptr-abstract-declarator : noptr-abstract-declarator parameters-and-qualifiers
                                  | parameters-and-qualifiers
                                  | noptr-abstract-declarator L_BRACKET constant-expression R_BRACKET
                                  | noptr-abstract-declarator L_BRACKET  R_BRACKET
                                  | L_BRACKET constant-expression R_BRACKET
                                  | L_BRACKET R_BRACKET
                                  | L_PAREN noptr-abstract-declarator R_PAREN """
    create_args(p)


def p_abstract_pack_declarator(p):
    """ abstract-pack-declarator : noptr-abstract-pack-declarator """
    create_args(p)


def p_noptr_abstract_pack_declarator(p):
    """ noptr-abstract-pack-declarator : noptr-abstract-pack-declarator parameters-and-qualifiers
                                       | noptr-abstract-pack-declarator L_BRACKET R_BRACKET
                                       | noptr-abstract-pack-declarator L_BRACKET constant-expression R_BRACKET
                                       | empty """
    create_args(p)


"""
 Declarators.functions
"""


def p_parameter_declaration_clause(p):
    """ parameter-declaration-clause : parameter-declaration-list """
    p[0] = p[1]


def p_parameter_declaration_clause_empty(p):
    """ parameter-declaration-clause : empty """
    p[0] = []


def p_parameter_declaration_list(p):
    """ parameter-declaration-list : parameter-declaration
                                   | parameter-declaration-list COMMA parameter-declaration """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = list(p[1]) + [p[3]]


def p_parameter_declaration(p):
    """ parameter-declaration : decl-specifier-seq declarator
                              | decl-specifier-seq declarator ASSIGNMENT initializer-clause
                              | decl-specifier-seq abstract-declarator
                              | decl-specifier-seq
                              | decl-specifier-seq abstract-declarator ASSIGNMENT initializer-clause
                              | decl-specifier-seq ASSIGNMENT initializer-clause """
    create_args(p)


def p_function_definition(p):
    """ function-definition : decl-specifier-seq declarator function-body
                            | declarator function-body """
    create_args(p)


def p_function_body(p):
    """ function-body : compound-statement """
    p[0] = p[1]


"""
 Declarators.initializers
"""


def p_initializer(p):
    """ initializer : brace-or-equal-initializer
                    | L_PAREN expression-list R_PAREN """
    create_args(p)


def p_brace_or_equal_initializer(p):
    """ brace-or-equal-initializer : ASSIGNMENT initializer-clause
                                   | braced-init-list """
    create_args(p)


def p_initializer_clause(p):
    """ initializer-clause : assignment-expression
                           | braced-init-list """
    create_args(p)


def p_initializer_list(p):
    """ initializer-list : initializer-clause
                         | initializer-list COMMA initializer-clause """
    create_args(p)


def p_braced_init_list(p):
    """ braced-init-list : L_CURLY initializer-list R_CURLY
                         | L_CURLY initializer-list COMMA R_CURLY
                         | L_CURLY R_CURLY """
    create_args(p)


"""
 Classes
"""


def p_class_name(p):
    """ class-name : IDENTIFIER """
    p[0] = p[1]


def p_class_specifier(p):
    """ class-specifier : class-head L_CURLY R_CURLY
                        | class-head L_CURLY member-specification R_CURLY """
    create_args(p)


def p_class_head(p):
    """ class-head : class-key class-head-name """
    p[0] = p[2]


def p_class_head_name(p):
    """ class-head-name : class-name """
    p[0] = p[1]


def p_class_key(p):
    """ class-key : CLASS
                  | STRUCT """
    p[0] = p[1]


def p_member_specification(p):
    """ member-specification : member-declaration
                             | member-declaration member-specification """
    create_args(p)


def p_member_declaration(p):
    """ member-declaration : empty-declaration
                           | decl-specifier-seq SEMICOLON
                           | member-declarator-list SEMICOLON
                           | decl-specifier-seq member-declarator-list SEMICOLON
                           | alias-declaration
                           | function-definition """
    create_args(p)


def p_member_declarator_list(p):
    """ member-declarator-list : member-declarator
                               | member-declarator-list COMMA member-declarator """
    create_args(p)


def p_member_declarator(p):
    """ member-declarator : declarator
                          | declarator brace-or-equal-initializer """
    create_args(p)


"""
 Overloading
"""


def p_operator_function_id(p):
    """ operator-function-id : OPERATOR operator """
    create_args(p)


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
    p[0] = p[1]


lexer = ply.lex.lex(module=lexer)
parser = ply.yacc.yacc()
