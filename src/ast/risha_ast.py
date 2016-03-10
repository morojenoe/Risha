import abc


class ASTNode(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def accept(self, visitor):
        pass


class Node(ASTNode):
    def __init__(self, *args):
        self.childs = list(args)

    def accept(self, visitor):
        for child in self.childs:
            if child is None:
                continue
            if isinstance(child, ASTNode):
                child.accept(visitor)
            elif isinstance(child, list):
                for children_of_child in child:
                    children_of_child.accept(visitor)
            else:
                visitor.visit(child)


class ForLoop(ASTNode):
    def __init__(self, for_init_statement, condition, expression, statement):
        self.for_init_statement = for_init_statement
        self.condition = condition
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        visitor.visit_for(self)


class CompoundStatement(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        visitor.visit_compound_statement(self)


class AliasDeclaration(ASTNode):
    def __init__(self, identifier, type_id):
        self.identifier = identifier
        self.type_id = type_id

    def accept(self, visitor):
        visitor.visit_alias_declaration(self)


class IfStatement(ASTNode):
    def __init__(self, condition, statement, else_statement):
        self.condition = condition
        self.statement = statement
        self.else_statement = else_statement

    def accept(self, visitor):
        visitor.visit_if(self)


class ParameterDeclaration(ASTNode):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visit_parameter_declaration(self)


class ClassHead(ASTNode):
    def __init__(self, class_key, class_name):
        self.class_key = class_key
        self.class_name = class_name

    def accept(self, visitor):
        pass


class ClassDefinition(ASTNode):
    def __init__(self, class_head, member_specification):
        self.class_head = class_head
        self.member_specification = member_specification

    def accept(self, visitor):
        visitor.visit_class(self)


class MemberSpecification(ASTNode):
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        return self

    def accept(self, visitor):
        visitor.visit_member_specification(self)


class EnumDefinition(ASTNode):
    def __init__(self, enum_head, enumerators):
        self.enum_head = enum_head
        self.enumerators = enumerators if enumerators is not None else []

    def accept(self, visitor):
        visitor.visit_enum(self)


class TernaryOperation(ASTNode):
    def __init__(self, logical_expression, true_expression, false_expression):
        self.logical_expression = logical_expression
        self.true_expression = true_expression
        self.false_expression = false_expression

    def accept(self, visitor):
        visitor.visit_ternary_operation(self)


class BinaryOperation(ASTNode):
    def __init__(self, first_expression, operation, second_expression):
        self.left_expression = first_expression
        self.operation = operation
        self.right_expression = second_expression

    def accept(self, visitor):
        visitor.visit_binary_operation(self)


class CastExpression(ASTNode):
    def __init__(self, cast_expression, new_type):
        self.cast_expression = cast_expression
        self.new_type = new_type

    def accept(self, visitor):
        visitor.visit_cast_expression(self)


class Expression(ASTNode):
    def __init__(self):
        self.expressions = []

    def add_expression(self, expression):
        self.expressions.append(expression)
        return self

    def accept(self, visitor):
        visitor.visit_expression(self)


class PrefixUnaryExpression(ASTNode):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_prefix_unary(self)


class PostfixUnaryExpression(ASTNode):
    def __init__(self, expression, operator):
        self.expression = expression
        self.operator = operator

    def accept(self, visitor):
        visitor.visit_postfix_unary(self)


class FunctionCall(ASTNode):
    def __init__(self, function, parameters):
        self.function = function
        self.parameters = parameters

    def accept(self, visitor):
        visitor.visit_function_call(self)


class ArraySubscription(ASTNode):
    def __init__(self, array_expression, subscript_expression):
        self.array_expression = array_expression
        self.subscript_expression = subscript_expression

    def accept(self, visitor):
        visitor.visit_array_subscription(self)


class ClassMemberAccess(ASTNode):
    def __init__(self, object_expression, member_expression):
        self.object_expression = object_expression
        self.member_expression = member_expression

    def accept(self, visitor):
        visitor.visit_member_access(self)


class InitializerList(ASTNode):
    def __init__(self):
        self.initializer_clauses = []

    def add_clause(self, clause):
        self.initializer_clauses.append(clause)
        return self

    def accept(self, visitor):
        visitor.visit_initializer_list(self)


class BracedInitializerList(ASTNode):
    def __init__(self, initializer_list):
        self.initializer_list = initializer_list

    def accept(self, visitor):
        visitor.visit_braced_init_list(self)


class EqualInitializer(ASTNode):
    def __init__(self, initializer_clause):
        self.initializer_clause = initializer_clause

    def accept(self, visitor):
        visitor.visit_equal_initializer(self)


class EnclosedInParenthesis(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_enclosed_in_paren(self)


class DeclSpecifierSeq(ASTNode):
    def __init__(self):
        self.decl_specifiers = []

    def add_decl_specifier(self, decl_specifier):
        self.decl_specifiers.append(decl_specifier)
        return self

    def accept(self, visitor):
        visitor.visit_decl_specifier_seq(self)


class Program(ASTNode):
    def __init__(self, declarations):
        self.declarations = declarations if declarations is not None else []

    def accept(self, visitor):
        visitor.visit_program(self)


class Identifier(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        visitor.visit_identifier(self)


class EnumKey(ASTNode):
    def __init__(self, enum_key):
        self.enum_key = enum_key

    def accept(self, visitor):
        visitor.visit_enum_key(self)


class EnumHead(ASTNode):
    def __init__(self, enum_key, identifier):
        self.enum_key = enum_key
        self.identifier = identifier

    def accept(self, visitor):
        visitor.visit_enum_head(self)


class Enumerator(ASTNode):
    def __init__(self, enumerator, const_expression):
        self.enumerator = enumerator
        self.const_expression = const_expression

    def accept(self, visitor):
        visitor.visit_enumerator(self)


class EnumeratorList(ASTNode):
    def __init__(self):
        self.enumerators = []

    def add_enumerator(self, enumerator):
        self.enumerators.append(enumerator)
        return self

    def accept(self, visitor):
        visitor.visit_enumerator_list(self)
