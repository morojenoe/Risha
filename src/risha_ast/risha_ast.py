import abc


class ASTNode(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def accept_print_visitor(self, visitor):
        pass

    @abc.abstractclassmethod
    def accept_before_after(self, visitor):
        pass


class CommaSeparatedList(ASTNode):
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_comma_separated_list_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_comma_separated_list_before(self)
        for element in self.elements:
            element.accept_before_after(visitor)
        visitor.visit_comma_separated_list_after(self)


class AliasDeclaration(ASTNode):
    def __init__(self, identifier, type_id):
        self.identifier = identifier
        self.type_id = type_id

    def accept_print_visitor(self, visitor):
        visitor.visit_alias_declaration_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_alias_declaration_before(self)
        self.identifier.accept_before_after(visitor)
        self.type_id.accept_before_after(visitor)
        visitor.visit_alias_declaration_after(self)


class EnclosedInParenthesis(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_enclosed_in_paren_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_enclosed_in_paren_before(self)
        self.expression.accept_before_after(visitor)
        visitor.visit_enclosed_in_paren_after(self)


class Identifier(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept_print_visitor(self, visitor):
        visitor.visit_identifier_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_identifier_before(self)
        visitor.visit_identifier_after(self)


class OperatorFunction(ASTNode):
    def __init__(self, operator):
        self.operator = operator

    def accept_print_visitor(self, visitor):
        visitor.visit_operator_function_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_operator_function_before(self)
        visitor.visit_operator_function_after(self)


class SimpleType(ASTNode):
    def __init__(self, type_name):
        self.type_name = type_name

    def accept_print_visitor(self, visitor):
        visitor.visit_simple_type_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_simple_type_before(self)
        visitor.visit_simple_type_after(self)
