import ply.lex
import ply.yacc

import src.risha_ast as risha_ast
from src.grammar import lexer

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
)

start = 'translation-unit'


def p_error(p):
    print("Syntax error at {}".format(p))


def p_empty(p):
    """ empty :  """
    p[0] = None


def p_translation_unit(p):
    """ translation-unit : declaration-seq
                         | empty """
    p[0] = risha_ast.program.Program(row=p[1].row if p[1] is not None else -1,
                                     col=p[1].col if p[1] is not None else -1,
                                     declarations=p[1])


"""
 Literals
"""


def p_literal(p):
    """ literal : integer-literal
                | boolean-literal """
    p[0] = p[1]


def p_literal_character(p):
    """ literal : CHARACTER_LITERAL """
    p[0] = risha_ast.CharacterLiteral(value=p[1],
                                      row=p.lineno(1),
                                      col=p.lexpos(1))


def p_literal_floating(p):
    """ literal : FLOATING_NUMBER """
    p[0] = risha_ast.FloatingNumberLiteral(value=p[1],
                                           row=p.lineno(1),
                                           col=p.lexpos(1))


def p_literal_string(p):
    """ literal : STRING_LITERAL """
    p[0] = risha_ast.StringLiteral(value=p[1],
                                   row=p.lineno(1),
                                   col=p.lexpos(1))


def p_integer_literal(p):
    """ integer-literal : BINARY_NUMBER
                        | OCTAL_NUMBER
                        | DECIMAL_NUMBER
                        | HEXADECIMAL_NUMBER """
    p[0] = risha_ast.IntegerLiteral(value=p[1],
                                    row=p.lineno(1),
                                    col=p.lexpos(1))


def p_boolean_literal(p):
    """ boolean-literal : TRUE
                        | FALSE """
    p[0] = risha_ast.BooleanLiteral(value=p[1],
                                    row=p.lineno(1),
                                    col=p.lexpos(1))


"""
 Expressions
"""


def build_binary_expression_node(p):
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.BinaryOperation(first_expression=p[1],
                                         operation=p[2],
                                         second_expression=p[3],
                                         row=p[1].row,
                                         col=p[1].col)


def p_constant_expression(p):
    """ constant-expression : conditional-expression """
    p[0] = p[1]


def p_expression(p):
    """ expression : assignment-expression
                   | expression COMMA assignment-expression """
    if len(p) == 2:
        p[0] = risha_ast.Expression(row=p[1].row,
                                    col=p[1].col).add(p[1])
    else:
        p[0] = p[1].add(p[3])


def p_assignment_expression(p):
    """ assignment-expression : conditional-expression
                              | logical-or-expression assignment-operator initializer-clause """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.AssignmentExpression(expression=p[1],
                                              operator=p[2],
                                              initializer=p[3],
                                              row=p[1].row,
                                              col=p[1].col)


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
        p[0] = risha_ast.TernaryOperation(logical_expression=p[1],
                                          true_expression=p[3],
                                          false_expression=p[5],
                                          row=p[1].row,
                                          col=p[1].col)


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
        p[0] = risha_ast.CastExpression(cast_expression=p[4],
                                        new_type=p[2],
                                        row=p.lineno(1),
                                        col=p.lexpos(1))


def p_unary_expression(p):
    """ unary-expression : postfix-expression
                         | INCREMENT cast-expression
                         | DECREMENT cast-expression
                         | PLUS cast-expression
                         | MINUS cast-expression
                         | LOGICAL_NOT cast-expression
                         | BITWISE_NOT cast-expression """

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.PrefixUnaryExpression(operator=p[1],
                                               expression=p[2],
                                               row=p.lineno(1),
                                               col=p.lexpos(1))


def p_postfix_expression(p):
    """ postfix-expression : primary-expression
                           | postfix-expression DOT id-expression """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.ClassMemberAccess(object_expression=p[1],
                                           member_expression=p[3],
                                           row=p[1].row,
                                           col=p[1].col)


def p_postfix_expression_array_subscription(p):
    """ postfix-expression : postfix-expression L_BRACKET expression R_BRACKET
                           | postfix-expression L_BRACKET braced-init-list R_BRACKET """
    p[0] = risha_ast.ArraySubscription(array_expression=p[1],
                                       subscript_expression=p[3],
                                       row=p[1].row,
                                       col=p[1].col)


def p_postfix_expression_func_call(p):
    """ postfix-expression : postfix-expression L_PAREN R_PAREN
                           | postfix-expression L_PAREN  expression-list  R_PAREN
                           | simple-type-specifier L_PAREN R_PAREN
                           | simple-type-specifier L_PAREN expression-list R_PAREN """
    if len(p) == 4:
        p[0] = risha_ast.FunctionCall(
            function=p[1],
            parameters=risha_ast.initializers.InitializerList(row=p.lineno(2),
                                                              col=p.lexpos(2)),
            row=p[1].row,
            col=p[1].col)
    else:
        p[0] = risha_ast.FunctionCall(function=p[1],
                                      parameters=p[3],
                                      row=p[1].row,
                                      col=p[1].col)


def p_postfix_expression_inc_dec(p):
    """ postfix-expression : postfix-expression INCREMENT
                           | postfix-expression DECREMENT """
    p[0] = risha_ast.PostfixUnaryExpression(expression=p[1],
                                            operator=p[2],
                                            row=p[1].row,
                                            col=p[1].col)


def p_primary_expression(p):
    """ primary-expression : literal
                           | L_PAREN expression R_PAREN
                           | id-expression """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.EnclosedInParenthesis(expression=p[2],
                                               row=p.lineno(1),
                                               col=p.lexpos(1))


def p_id_expression(p):
    """ id-expression : unqualified-id """
    p[0] = p[1]


def p_unqualified_id_identifier(p):
    """ unqualified-id : IDENTIFIER """
    p[0] = risha_ast.Identifier(identifier=p[1],
                                row=p.lineno(1),
                                col=p.lexpos(1))


def p_unqualified_id_operator_function(p):
    """ unqualified-id : operator-function-id """
    p[0] = p[1]


def p_expression_list(p):
    """ expression-list : initializer-list """
    p[0] = p[1]


"""
 Statements
"""


def p_statement(p):
    """ statement : expression-statement
                  | compound-statement
                  | selection-statement
                  | iteration-statement
                  | jump-statement
                  | declaration-statement """
    p[0] = p[1]


def p_expression_statement(p):
    """ expression-statement : expression SEMICOLON
                             | SEMICOLON """
    if len(p) == 2:
        p[0] = risha_ast.StatementExpression(expression=None,
                                             row=p.lineno(1),
                                             col=p.lexpos(1))
    else:
        p[0] = risha_ast.StatementExpression(expression=p[1],
                                             row=p[1].row,
                                             col=p[1].col)


def p_compound_statement(p):
    """ compound-statement : L_CURLY statement-seq R_CURLY
                           | L_CURLY R_CURLY """
    statements = p[2] if len(p) == 4 else None
    p[0] = risha_ast.CompoundStatement(statements=statements,
                                       row=p.lineno(1),
                                       col=p.lexpos(1))


def p_statement_seq(p):
    """ statement-seq : statement
                      | statement-seq statement """
    if len(p) == 2:
        p[0] = risha_ast.StatementSequence(row=p[1].row,
                                           col=p[1].col).add(p[1])
    else:
        p[0] = p[1].add(p[2])


def p_selection_statement_if(p):
    """ selection-statement : IF L_PAREN condition R_PAREN statement
                            | IF L_PAREN condition R_PAREN statement ELSE statement """
    else_statement = p[7] if len(p) == 8 else None
    p[0] = risha_ast.IfStatement(condition=p[3],
                                 statement=p[5],
                                 else_statement=else_statement,
                                 row=p.lineno(1),
                                 col=p.lexpos(1))


def p_condition(p):
    """ condition : expression
                  | decl-specifier-seq declarator brace-or-equal-initializer """
    if len(p) == 2:
        p[0] = p[1]
    else:
        simple_decl = risha_ast.SimpleDeclaration(specifiers=p[1],
                                                  declarators=p[2],
                                                  row=p[1].row,
                                                  col=p[1].col,
                                                  need_a_semicolon=False)
        p[0] = risha_ast.ConditionWithDeclaration(
            declarator_with_specifiers=simple_decl,
            initializer=p[3],
            row=p[1].row,
            col=p[1].col)


def p_iteration_statement_while(p):
    """ iteration-statement : WHILE L_PAREN condition R_PAREN statement """
    p[0] = risha_ast.WhileLoop(condition=p[3],
                               statement=p[5],
                               row=p.lineno(1),
                               col=p.lexpos(1))


def p_iteration_statement_do_while(p):
    """ iteration-statement : DO statement WHILE L_PAREN expression R_PAREN SEMICOLON """
    p[0] = risha_ast.DoWhileLoop(statement=p[2],
                                 expression=p[5],
                                 row=p.lineno(1),
                                 col=p.lexpos(1))


def p_iteration_statement_for(p):
    """ iteration-statement : FOR L_PAREN for-range-declaration COLON for-range-initializer R_PAREN statement """
    p[0] = risha_ast.RangeForLoop(declaration=p[3],
                                  initializer=p[5],
                                  statement=p[7],
                                  row=p.lineno(1),
                                  col=p.lexpos(1))


def p_iteration_for_statement(p):
    """ iteration-statement : FOR L_PAREN for-init-statement SEMICOLON R_PAREN statement
                            | FOR L_PAREN for-init-statement SEMICOLON expression R_PAREN statement
                            | FOR L_PAREN for-init-statement condition SEMICOLON expression R_PAREN statement
                            | FOR L_PAREN for-init-statement condition SEMICOLON R_PAREN statement"""
    init_statement = p[3]
    condition = p[4] if len(p) in [8, 9] else None
    expression = p[5] if len(p) == 8 else p[6] if len(p) == 9 else None
    statement = p[len(p) - 1]
    p[0] = risha_ast.ForLoop(for_init_statement=init_statement,
                             condition=condition,
                             expression=expression,
                             statement=statement,
                             row=p.lineno(1),
                             col=p.lexpos(1))


def p_for_init_statement(p):
    """ for-init-statement : expression-statement
                           | simple-declaration """
    p[0] = p[1]


def p_for_range_declaration(p):
    """ for-range-declaration : decl-specifier-seq declarator """
    p[0] = risha_ast.SimpleDeclaration(specifiers=p[1],
                                       declarators=p[2],
                                       row=p[1].row,
                                       col=p[1].col,
                                       need_a_semicolon=False)


def p_for_range_initializer(p):
    """ for-range-initializer : expression
                              | braced-init-list """
    p[0] = p[1]


def p_jump_statement_break(p):
    """ jump-statement : BREAK SEMICOLON """
    p[0] = risha_ast.BreakStatement(row=p.lineno(1),
                                    col=p.lexpos(1))


def p_jump_statement_continue(p):
    """ jump-statement : CONTINUE SEMICOLON """
    p[0] = risha_ast.ContinueStatement(row=p.lineno(1),
                                       col=p.lexpos(1))


def p_jump_statement_return(p):
    """ jump-statement : RETURN SEMICOLON
                       | RETURN expression SEMICOLON
                       | RETURN braced-init-list SEMICOLON """
    expression = p[2] if len(p) > 3 else None
    p[0] = risha_ast.ReturnStatement(expression=expression,
                                     row=p.lineno(1),
                                     col=p.lexpos(1))


def p_declaration_statement(p):
    """ declaration-statement : block-declaration """
    p[0] = p[1]


"""
  Declarations
"""


def p_declaration_seq(p):
    """ declaration-seq : declaration
                        | declaration-seq declaration """
    if len(p) == 2:
        p[0] = risha_ast.DeclarationSequence(row=p[1].row,
                                             col=p[1].col).add(p[1])
    else:
        p[0] = p[1].add(p[2])


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
    p[0] = risha_ast.AliasDeclaration(
        identifier=risha_ast.Identifier(identifier=p[2],
                                        row=p.lineno(2),
                                        col=p.lexpos(2)),
        type_id=p[4],
        row=p.lineno(1),
        col=p.lexpos(1))


def p_simple_declaration(p):
    """ simple-declaration : init-declarator-list SEMICOLON
                           | SEMICOLON """
    specifiers = None
    declarators = p[1] if len(p) == 3 else None
    row = p.lineno(1) if len(p) == 2 else p[1].row
    col = p.lexpos(1) if len(p) == 2 else p[1].col
    p[0] = risha_ast.SimpleDeclaration(specifiers=specifiers,
                                       declarators=declarators,
                                       row=row,
                                       col=col)


def p_simple_declaration_with_specifiers(p):
    """ simple-declaration : decl-specifier-seq init-declarator-list SEMICOLON
                           | decl-specifier-seq SEMICOLON """
    specifiers = p[1]
    declarators = p[2] if len(p) == 4 else None
    p[0] = risha_ast.SimpleDeclaration(specifiers=specifiers,
                                       declarators=declarators,
                                       row=p[1].row,
                                       col=p[1].col)


def p_empty_declaration(p):
    """ empty-declaration : SEMICOLON """
    p[0] = p[1]


def p_decl_specifier(p):
    """ decl-specifier : storage-class-specifier
                       | type-specifier """
    p[0] = p[1]


def p_decl_specifier_seq(p):
    """ decl-specifier-seq : decl-specifier
                           | decl-specifier-seq decl-specifier """
    if len(p) == 2:
        p[0] = risha_ast.DeclSpecifierSeq(row=p[1].row,
                                          col=p[1].col)
        if isinstance(p[1], risha_ast.RefQualifier):
            p[0].set_ref_qualifier()
        else:
            p[0] = p[0].add(p[1])
    else:
        if isinstance(p[2], risha_ast.RefQualifier):
            p[0] = p[1].set_ref_qualifier()
        else:
            p[0] = p[1].add(p[2])


def p_storage_class_specifier(p):
    """ storage-class-specifier : STATIC """
    p[0] = risha_ast.StorageSpecifier(name=p[1],
                                      row=p.lineno(1),
                                      col=p.lexpos(1))


def p_type_specifier(p):
    """ type-specifier : trailing-type-specifier
                       | ref-qualifier
                       | class-specifier
                       | enum-specifier """
    p[0] = p[1]


def p_type_specifier_seq(p):
    """ type-specifier-seq : type-specifier
                           | type-specifier type-specifier-seq """
    if len(p) == 2:
        p[0] = risha_ast.TypeSpecifierSequence(row=p[1].row,
                                               col=p[1].col).add(p[1])
    else:
        p[0] = p[2].add(p[1])


def p_trailing_type_specifier(p):
    """ trailing-type-specifier : simple-type-specifier
                                | elaborated-type-specifier
                                | cv-qualifier """
    p[0] = p[1]


def p_trailing_type_specifier_seq(p):
    """ trailing-type-specifier-seq : trailing-type-specifier
                                    | trailing-type-specifier trailing-type-specifier-seq """
    if len(p) == 2:
        p[0] = risha_ast.TrailingTypeSpecifierSequence(row=p[1].row,
                                                       col=p[1].col).add(p[1])
    else:
        p[0] = p[2].add(p[1])


def p_simple_type_specifier(p):
    """ simple-type-specifier : CHAR
                              | BOOL
                              | SHORT
                              | INT
                              | SIGNED
                              | UNSIGNED
                              | FLOAT
                              | DOUBLE
                              | VOID
                              | AUTO """
    p[0] = risha_ast.SimpleType(type_name=p[1],
                                row=p.lineno(1),
                                col=p.lexpos(1))


def p_simple_type_specifier_type_name(p):
    """ simple-type-specifier : type-name """
    p[0] = p[1]


def p_type_name(p):
    """ type-name : class-name
                  | enum-name """
    p[0] = p[1]


def p_elaborated_type_specifier_enum(p):
    """ elaborated-type-specifier : enum-key IDENTIFIER """
    p[0] = risha_ast.enums.EnumHead(enum_key=p[1],
                                    identifier=risha_ast.Identifier(
                                        identifier=p[2],
                                         row=p.lineno(2),
                                         col=p.lexpos(2)),
                                    row=p[1].row,
                                    col=p[1].col)


def p_elaborated_type_specifier_class(p):
    """ elaborated-type-specifier : class-key IDENTIFIER """
    p[0] = risha_ast.ClassHead(class_key=p[1],
                               class_name=risha_ast.Identifier(
                                   identifier=p[2],
                                   row=p.lineno(2),
                                   col=p.lexpos(2)),
                               row=p[1].row,
                               col=p[1].col)


"""
  Declarations.Enums
"""


def p_enum_name(p):
    """ enum-name : IDENTIFIER """
    p[0] = risha_ast.Identifier(identifier=p[1],
                                row=p.lineno(1),
                                col=p.lineno(1))


def p_enum_specifier(p):
    """ enum-specifier : enum-head L_CURLY R_CURLY
                       | enum-head L_CURLY enumerator-list R_CURLY
                       | enum-head L_CURLY enumerator-list COMMA R_CURLY """
    if len(p) == 4:
        p[0] = risha_ast.EnumDefinition(enum_head=p[1],
                                        enumerators=risha_ast.EnumeratorList(
                                            row=p.lineno(2),
                                            col=p.lexpos(2)),
                                        row=p[1].row,
                                        col=p[1].col)
    else:
        p[0] = risha_ast.enums.EnumDefinition(enum_head=p[1],
                                              enumerators=p[3],
                                              row=p[1].row,
                                              col=p[1].col)


def p_enum_head(p):
    """ enum-head : enum-key
                  | enum-key IDENTIFIER """
    if len(p) == 2:
        p[0] = risha_ast.enums.EnumHead(enum_key=p[1],
                                        identifier=None,
                                        row=p[1].row,
                                        col=p[1].col)
    else:
        p[0] = risha_ast.enums.EnumHead(enum_key=p[1],
                                        identifier=risha_ast.Identifier(
                                            identifier=p[2],
                                            row=p.lineno(2),
                                            col=p.lexpos(2)),
                                        row=p[1].row,
                                        col=p[1].col)


def p_opaque_enum_declaration(p):
    """ opaque-enum-declaration : enum-key IDENTIFIER """
    p[0] = risha_ast.enums.EnumHead(enum_key=p[1],
                                    identifier=risha_ast.Identifier(
                                        identifier=p[2],
                                        row=p.lineno(2),
                                        col=p.lexpos(2)),
                                    row=p[1].row,
                                    col=p[1].col)


def p_enum_key(p):
    """ enum-key : ENUM """
    p[0] = risha_ast.enums.EnumKey(enum_key=None,
                                   row=p.lineno(1),
                                   col=p.lexpos(1))


def p_enumerator_list(p):
    """ enumerator-list : enumerator-definition
                        | enumerator-list COMMA enumerator-definition """
    if len(p) == 2:
        p[0] = risha_ast.enums.EnumeratorList(row=p[1].row, col=p[1].col) \
            .add_enumerator(p[1])
    else:
        p[0] = p[1].add_enumerator(p[3])


def p_enumerator_definition(p):
    """ enumerator-definition : enumerator
                              | enumerator ASSIGNMENT constant-expression """
    if len(p) == 2:
        p[0] = risha_ast.enums.Enumerator(enumerator=p[1],
                                          const_expression=None,
                                          row=p[1].row,
                                          col=p[1].col)
    else:
        p[0] = risha_ast.enums.Enumerator(
            enumerator=p[1],
            const_expression=risha_ast.IdentifierCheck(node=p[3],
                                                       row=p[3].row,
                                                       col=p[3].col),
            row=p[1].row,
            col=p[1].col)


def p_enumerator(p):
    """ enumerator : IDENTIFIER """
    p[0] = risha_ast.Identifier(identifier=p[1],
                                row=p.lineno(1),
                                col=p.lexpos(1))


"""
 Declarators
"""


def p_init_declarator_list(p):
    """ init-declarator-list : init-declarator
                             | init-declarator-list COMMA init-declarator """
    if len(p) == 2:
        p[0] = risha_ast.InitDeclaratorList(row=p[1].row,
                                            col=p[1].col).add(p[1])
    else:
        p[0] = p[1].add(p[3])


def p_init_declarator(p):
    """ init-declarator : declarator
                        | declarator initializer """
    if len(p) == 2:
        p[0] = risha_ast.InitDeclarator(declarator=p[1],
                                        initializer=None,
                                        row=p[1].row,
                                        col=p[1].col)
    else:
        p[0] = risha_ast.InitDeclarator(declarator=p[1],
                                        initializer=p[2],
                                        row=p[1].row,
                                        col=p[1].col)


def p_declarator(p):
    """ declarator : noptr-declarator """
    p[0] = p[1]


def p_noptr_declarator(p):
    """ noptr-declarator : declarator-id
                         | noptr-declarator parameters-and-qualifiers """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = risha_ast.FunctionDeclarator(function_name=p[1],
                                            parameters=p[2],
                                            row=p[1].row,
                                            col=p[1].col)


def p_noptr_declarator_array_decl_with_param(p):
    """ noptr-declarator : noptr-declarator L_BRACKET constant-expression R_BRACKET """
    if isinstance(p[1], risha_ast.Identifier):
        p[0] = risha_ast.ArrayDeclarator(array_name=p[1],
                                         row=p[1].row,
                                         col=p[1].col).add_parameter(p[3])
    else:
        assert isinstance(p[1], risha_ast.ArrayDeclarator)
        p[0] = p[1].add_parameter(p[3])


def p_noptr_declarator_array_decl_with_empty_param(p):
    """ noptr-declarator : noptr-declarator L_BRACKET  R_BRACKET """
    if isinstance(p[1], risha_ast.Identifier):
        p[0] = risha_ast.ArrayDeclarator(array_name=p[1],
                                         row=p[1].row,
                                         col=p[1].col).add_parameter(None)
    else:
        assert isinstance(p[1], risha_ast.ArrayDeclarator)
        p[0] = p[1].add_parameter(None)


def p_noptr_declarator_paren(p):
    """ noptr-declarator : L_PAREN noptr-declarator R_PAREN """
    p[0] = risha_ast.EnclosedInParenthesis(expression=p[2],
                                           row=p.lineno(1),
                                           col=p.lexpos(1))


def p_parameters_and_qualifiers(p):
    """ parameters-and-qualifiers : L_PAREN parameter-declaration-clause R_PAREN """
    p[0] = risha_ast.EnclosedInParenthesis(expression=p[2],
                                           row=p.lineno(1),
                                           col=p.lexpos(1))


def p_cv_qualifier(p):
    """ cv-qualifier : CONST """
    p[0] = risha_ast.ConstQualifier(name=p[1],
                                    row=p.lineno(1),
                                    col=p.lexpos(1))


def p_ref_qualifier(p):
    """ ref-qualifier : REF """
    p[0] = risha_ast.RefQualifier(name=p[1],
                                  row=p.lineno(1),
                                  col=p.lexpos(1))


def p_declarator_id(p):
    """ declarator-id : id-expression """
    p[0] = p[1]


"""
 Declarators.type-names
"""


def p_type_id(p):
    """ type-id : type-specifier-seq
                | type-specifier-seq abstract-declarator """
    specifiers = p[1]
    declarators = p[2] if len(p) == 3 else None
    p[0] = risha_ast.SimpleDeclaration(specifiers=specifiers,
                                       declarators=declarators,
                                       row=p[1].row,
                                       col=p[1].col,
                                       need_a_semicolon=False)


def p_abstract_declarator(p):
    """ abstract-declarator : noptr-abstract-declarator """
    p[0] = p[1]


def p_noptr_abstract_declarator_array_with_prefix(p):
    """ noptr-abstract-declarator : noptr-abstract-declarator L_BRACKET constant-expression R_BRACKET
                                  | noptr-abstract-declarator L_BRACKET R_BRACKET """
    if isinstance(p[1], risha_ast.ArrayDeclarator):
        if len(p) == 4:
            p[0] = p[1].add_parameter(None)
        else:
            p[0] = p[1].add_parameter(p[3])
    else:
        parameter = p[3] if len(p) == 5 else None
        p[0] = risha_ast.ArrayDeclarator(array_name=p[1],
                                         row=p[1].row,
                                         col=p[1].col).add_parameter(parameter)


def p_noptr_abstract_declarator_array_without_prefix(p):
    """ noptr-abstract-declarator : L_BRACKET constant-expression R_BRACKET
                                  | L_BRACKET R_BRACKET """
    parameter = p[2] if len(p) == 4 else None
    p[0] = risha_ast.ArrayDeclarator(array_name=None,
                                     row=p.lineno(1),
                                     col=p.lexpos(1)).add_parameter(parameter)


def p_noptr_abstract_declarator_functions(p):
    """ noptr-abstract-declarator : noptr-abstract-declarator parameters-and-qualifiers
                                  | parameters-and-qualifiers """
    function_name = p[1] if len(p) == 3 else None
    parameters = p[2] if len(p) == 3 else p[1]
    p[0] = risha_ast.FunctionDeclarator(function_name=function_name,
                                        parameters=parameters,
                                        row=p[1].row,
                                        col=p[1].col)


def p_noptr_abstract_declarator_enclosed_in_paren(p):
    """ noptr-abstract-declarator : L_PAREN noptr-abstract-declarator R_PAREN """
    p[0] = risha_ast.EnclosedInParenthesis(expression=p[2],
                                           row=p.lineno(1),
                                           col=p.lineno(1))


"""
 Declarators.functions
"""


def p_parameter_declaration_clause(p):
    """ parameter-declaration-clause : parameter-declaration-list """
    p[0] = p[1]


def p_parameter_declaration_clause_empty(p):
    """ parameter-declaration-clause : empty """
    p[0] = risha_ast.ParameterDeclarationList(row=-1,
                                              col=-1)


def p_parameter_declaration_list(p):
    """ parameter-declaration-list : parameter-declaration
                                   | parameter-declaration-list COMMA parameter-declaration """
    if len(p) == 2:
        p[0] = risha_ast.ParameterDeclarationList(row=p[1].row,
                                                  col=p[1].col).add(p[1])
    else:
        p[0] = p[1].add(p[3])


def p_parameter_declaration(p):
    """ parameter-declaration : decl-specifier-seq declarator
                              | decl-specifier-seq abstract-declarator
                              | decl-specifier-seq
                              | decl-specifier-seq ASSIGNMENT initializer-clause """
    row = p[1].row
    col = p[1].col
    if len(p) == 2:
        p[0] = risha_ast.SimpleDeclaration(specifiers=p[1],
                                           declarators=None,
                                           row=row,
                                           col=col,
                                           need_a_semicolon=False)
    elif len(p) == 3:
        p[0] = risha_ast.SimpleDeclaration(specifiers=p[1],
                                           declarators=p[2],
                                           row=row,
                                           col=col,
                                           need_a_semicolon=False)
    elif len(p) == 4:
        p[0] = risha_ast.SimpleDeclaration(
            specifiers=p[1],
            declarators=risha_ast.EqualInitializer(initializer_clause=p[3],
                                                   row=p.lineno(2),
                                                   col=p.lexpos(2)),
            row=row,
            col=col,
            need_a_semicolon=False)


def p_parameter_declaration_with_initializer(p):
    """ parameter-declaration : decl-specifier-seq declarator ASSIGNMENT initializer-clause
                              | decl-specifier-seq abstract-declarator ASSIGNMENT initializer-clause """
    declarator = risha_ast.InitDeclarator(
        declarator=p[2],
        initializer=risha_ast.EqualInitializer(initializer_clause=p[4],
                                               row=p.lineno(3),
                                               col=p.lexpos(3)),
        row=p[1].row,
        col=p[1].col)
    p[0] = risha_ast.SimpleDeclaration(specifiers=p[1],
                                       declarators=declarator,
                                       row=p[1].row,
                                       col=p[1].col,
                                       need_a_semicolon=False)


def p_function_definition(p):
    """ function-definition : decl-specifier-seq declarator function-body
                            | declarator function-body """
    if len(p) == 4:
        p[0] = risha_ast.FunctionDefinition(return_type=p[1],
                                            function_head=p[2],
                                            body=p[3],
                                            row=p[1].row,
                                            col=p[1].col)
    else:
        p[0] = risha_ast.FunctionDefinition(return_type=None,
                                            function_head=p[1],
                                            body=p[2],
                                            row=p[1].row,
                                            col=p[1].col)


def p_function_body(p):
    """ function-body : compound-statement """
    p[0] = p[1]


"""
 Declarators.initializers
"""


def p_initializer(p):
    """ initializer : brace-or-equal-initializer
                    | L_PAREN expression-list R_PAREN """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.EnclosedInParenthesis(p[2],
                                               row=p.lineno(1),
                                               col=p.lexpos(1))


def p_brace_or_equal_initializer(p):
    """ brace-or-equal-initializer : ASSIGNMENT initializer-clause
                                   | braced-init-list """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = risha_ast.initializers.EqualInitializer(p[2],
                                                       row=p.lineno(1),
                                                       col=p.lexpos(1))


def p_initializer_clause(p):
    """ initializer-clause : assignment-expression
                           | braced-init-list """
    p[0] = p[1]


def p_initializer_list(p):
    """ initializer-list : initializer-clause
                         | initializer-list COMMA initializer-clause """
    if len(p) == 2:
        p[0] = risha_ast.InitializerList(row=p[1].row,
                                         col=p[1].col).add(p[1])
    else:
        p[0] = p[1].add(p[3])


def p_braced_init_list(p):
    """ braced-init-list : L_CURLY initializer-list R_CURLY
                         | L_CURLY initializer-list COMMA R_CURLY
                         | L_CURLY R_CURLY """
    row = p.lineno(1)
    col = p.lexpos(1)
    if len(p) == 3:
        p[0] = risha_ast.BracedInitializerList(
            initializer_list=risha_ast.InitializerList(row=row, col=col),
            row=row,
            col=col)
    else:
        p[0] = risha_ast.BracedInitializerList(initializer_list=p[2],
                                               row=row,
                                               col=col)


"""
 Classes
"""


def p_class_name(p):
    """ class-name : IDENTIFIER """
    p[0] = risha_ast.Identifier(identifier=p[1],
                                row=p.lineno(1),
                                col=p.lexpos(1))


def p_class_specifier(p):
    """ class-specifier : class-head L_CURLY R_CURLY
                        | class-head L_CURLY member-specification R_CURLY """
    if len(p) == 4:
        empty_mem_specification = risha_ast.MemberSpecifications(
            row=p.lineno(2),
            col=p.lexpos(2))
        p[0] = risha_ast.ClassDefinition(
            class_head=p[1],
            member_specification=empty_mem_specification,
            row=p[1].row,
            col=p[1].col)
    else:
        p[0] = risha_ast.ClassDefinition(class_head=p[1],
                                         member_specification=p[3],
                                         row=p[1].row,
                                         col=p[1].col)


def p_class_head(p):
    """ class-head : class-key class-name """
    p[0] = risha_ast.ClassHead(class_key=p[1],
                               class_name=p[2],
                               row=p[1].row,
                               col=p[1].col)


def p_class_key(p):
    """ class-key : CLASS
                  | STRUCT """
    p[0] = p[1]


"""
 Class.members
"""


def p_member_specification(p):
    """ member-specification : member-declaration
                             | member-declaration member-specification """
    if len(p) == 2:
        p[0] = risha_ast.MemberSpecifications(row=p[1].row,
                                              col=p[1].col).add(p[1])
    else:
        p[0] = p[2].add(p[1])


def p_member_declaration(p):
    """ member-declaration : empty-declaration
                           | alias-declaration
                           | function-definition """
    p[0] = p[1]


def p_member_declaration_declarators(p):
    """ member-declaration : member-declarator-list SEMICOLON
                           | decl-specifier-seq member-declarator-list SEMICOLON """
    if len(p) == 3:
        p[0] = risha_ast.SimpleDeclaration(None, p[1], row=p[1].row,
                                           col=p[1].col)
    else:
        p[0] = risha_ast.SimpleDeclaration(p[1], p[2], row=p[1].row,
                                           col=p[1].col)


def p_member_declaration_declarators_specifiers(p):
    """ member-declaration : decl-specifier-seq SEMICOLON """
    p[0] = risha_ast.SimpleDeclaration(p[1], None, row=p[1].row, col=p[1].col)


def p_member_declarator_list(p):
    """ member-declarator-list : member-declarator
                               | member-declarator-list COMMA member-declarator """
    if len(p) == 2:
        p[0] = risha_ast.MemberDeclaratorList(row=p[1].row,
                                              col=p[1].col).add(p[1])
    else:
        p[0] = p[1].add(p[3])


def p_member_declarator(p):
    """ member-declarator : declarator
                          | declarator brace-or-equal-initializer """
    if len(p) == 2:
        p[0] = risha_ast.InitDeclarator(p[1], None, row=p[1].row, col=p[1].col)
    else:
        p[0] = risha_ast.InitDeclarator(p[1], p[2], row=p[1].row, col=p[1].col)


"""
 Overloading
"""


def p_operator_function_id(p):
    """ operator-function-id : OPERATOR operator """
    row = p.lineno(1)
    col = p.lexpos(1)
    p[0] = risha_ast.OperatorFunction(operator=p[2], row=row, col=col)


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
