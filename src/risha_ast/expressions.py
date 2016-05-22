from src.risha_ast import ASTNode, CommaSeparatedList


class BinaryOperation(ASTNode):
    def __init__(self, first_expression, operation, second_expression):
        self.left_expression = first_expression
        self.operation = operation
        self.right_expression = second_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_binary_operation(self)


class TernaryOperation(ASTNode):
    def __init__(self, logical_expression, true_expression, false_expression):
        self.logical_expression = logical_expression
        self.true_expression = true_expression
        self.false_expression = false_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_ternary_operation(self)


class CastExpression(ASTNode):
    def __init__(self, cast_expression, new_type):
        self.cast_expression = cast_expression
        self.new_type = new_type

    def accept_print_visitor(self, visitor):
        visitor.visit_cast_expression(self)


class Expression(CommaSeparatedList):
    pass


class PrefixUnaryExpression(ASTNode):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_prefix_unary(self)


class PostfixUnaryExpression(ASTNode):
    def __init__(self, expression, operator):
        self.expression = expression
        self.operator = operator

    def accept_print_visitor(self, visitor):
        visitor.visit_postfix_unary(self)


class FunctionCall(ASTNode):
    def __init__(self, function, parameters):
        self.function = function
        self.parameters = parameters

    def accept_print_visitor(self, visitor):
        visitor.visit_function_call(self)


class ArraySubscription(ASTNode):
    def __init__(self, array_expression, subscript_expression):
        self.array_expression = array_expression
        self.subscript_expression = subscript_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_array_subscription(self)


class ClassMemberAccess(ASTNode):
    def __init__(self, object_expression, member_expression):
        self.object_expression = object_expression
        self.member_expression = member_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_member_access(self)


class AssignmentExpression(ASTNode):
    def __init__(self, expression, operator, initializer):
        self.expression = expression
        self.operator = operator
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_assignment_expression(self)
