from .risha_ast import ASTNode
from src.risha_ast import CommaSeparatedList


class BinaryOperation(ASTNode):
    def __init__(self, first_expression, operation, second_expression):
        self.left_expression = first_expression
        self.operation = operation
        self.right_expression = second_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_binary_operation_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_binary_operation_before(self)
        self.left_expression.accept_before_after(visitor)
        self.right_expression.accept_before_after(visitor)
        visitor.visit_binary_operation_after(self)


class TernaryOperation(ASTNode):
    def __init__(self, logical_expression, true_expression, false_expression):
        self.logical_expression = logical_expression
        self.true_expression = true_expression
        self.false_expression = false_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_ternary_operation_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_ternary_operation_before(self)
        self.logical_expression.accept_before_after(visitor)
        self.true_expression.accept_before_after(visitor)
        self.false_expression.accept_before_after(visitor)
        visitor.visit_ternary_operation_after(self)


class CastExpression(ASTNode):
    def __init__(self, cast_expression, new_type):
        self.cast_expression = cast_expression
        self.new_type = new_type

    def accept_print_visitor(self, visitor):
        visitor.visit_cast_expression_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_cast_expression_before(self)
        self.new_type.accept_before_after(visitor)
        self.cast_expression.accept_before_after(visitor)
        visitor.visit_cast_expression_after(self)


class Expression(CommaSeparatedList):
    pass


class PrefixUnaryExpression(ASTNode):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_prefix_unary_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_prefix_unary_before(self)
        self.expression.accept_before_after(visitor)
        visitor.visit_prefix_unary_after(self)


class PostfixUnaryExpression(ASTNode):
    def __init__(self, expression, operator):
        self.expression = expression
        self.operator = operator

    def accept_print_visitor(self, visitor):
        visitor.visit_postfix_unary_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_postfix_unary_before(self)
        self.expression.accept_before_after(visitor)
        visitor.visit_postfix_unary_after(self)


class FunctionCall(ASTNode):
    def __init__(self, function, parameters):
        self.function = function
        self.parameters = parameters

    def accept_print_visitor(self, visitor):
        visitor.visit_function_call_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_function_call_before(self)
        self.function.accept_before_after(visitor)
        self.parameters.accept_before_after(visitor)
        visitor.visit_function_call_after(self)


class ArraySubscription(ASTNode):
    def __init__(self, array_expression, subscript_expression):
        self.array_expression = array_expression
        self.subscript_expression = subscript_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_array_subscription_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_array_subscription_before(self)
        self.array_expression.accept_before_after(visitor)
        self.subscript_expression.accept_before_after(visitor)
        visitor.visit_array_subscription_after(self)


class ClassMemberAccess(ASTNode):
    def __init__(self, object_expression, member_expression):
        self.object_expression = object_expression
        self.member_expression = member_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_member_access_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_member_access_before(self)
        self.object_expression.accept_before_after(visitor)
        self.member_expression.accept_before_after(visitor)
        visitor.visit_member_access_after(self)


class AssignmentExpression(ASTNode):
    def __init__(self, expression, operator, initializer):
        self.expression = expression
        self.operator = operator
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_assignment_expression_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_assignment_expression_before(self)
        self.expression.accept_before_after(visitor)
        self.initializer.accept_before_after(visitor)
        visitor.visit_assignment_expression_after(self)
