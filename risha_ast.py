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


class ForNode(ASTNode):
    def __init__(self, for_init_statement, condition, expression, statement):
        self.for_init_statement = for_init_statement
        self.condition = condition
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        visitor.visit_for(self)


class CompoundStatementNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        visitor.visit_compound_statement(self)


class AliasDeclarationNode(ASTNode):
    def __init__(self, identifier, type_id):
        self.identifier = identifier
        self.type_id = type_id

    def accept(self, visitor):
        visitor.visit_alias_declaration(self)


class IfNode(ASTNode):
    def __init__(self, condition, statement, else_statement):
        self.condition = condition
        self.statement = statement
        self.else_statement = else_statement

    def accept(self, visitor):
        visitor.visit_if(self)


class ParameterDeclarationNode(ASTNode):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visit_parameter_declaration(self)


class ClassNode(ASTNode):
    def __init__(self, class_name, alias_declarations, functions, declarations):
        self.class_name = class_name
        if alias_declarations is not None:
            self.alias_declarations = alias_declarations
        else:
            self.alias_declarations = []
        self.functions = functions if functions is not None else []
        self.declarations = declarations if declarations is not None else []

    def accept(self, visitor):
        visitor.visit_class(self)


class EnumNode(ASTNode):
    def __init__(self, enum_key, enum_name, enumerators):
        self.enum_key = enum_key
        self.enum_name = enum_name
        self.enumerators = enumerators if enumerators is not None else []

    def accept(self, visitor):
        visitor.visit_enum(self)


class TernaryOperationNode(ASTNode):
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


class ExpressionNode(ASTNode):
    def __init__(self):
        self.expressions = []

    def add_expression(self, expression):
        self.expressions.append(expression)
        return self

    def accept(self, visitor):
        visitor.visit_expression(self)


class PrefixUnaryExpressionNode(ASTNode):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_prefix_unary(self)


class PostfixUnaryExpressionNode(ASTNode):
    def __init__(self, expression, operator):
        self.expression = expression
        self.operator = operator

    def accept(self, visitor):
        visitor.visit_postfix_unary(self)


class FunctionCallNode(ASTNode):
    def __init__(self, function, parameters):
        self.function = function
        self.parameters = parameters

    def accept(self, visitor):
        visitor.visit_function_call(self)


class ArraySubscriptionNode(ASTNode):
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
