import abc


class ASTNode(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def accept_print_visitor(self, visitor):
        pass


class Sequence(ASTNode):
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_sequence_before(self)


class CommaSeparatedList(ASTNode):
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_comma_separated_list_before(self)


class Node(ASTNode):
    def __init__(self, *args):
        self.childs = list(args)

    def accept_print_visitor(self, visitor):
        for child in self.childs:
            if child is None:
                continue
            if isinstance(child, ASTNode):
                child.accept_print_visitor(visitor)
            elif isinstance(child, list):
                for children_of_child in child:
                    children_of_child.accept_print_visitor(visitor)
            else:
                visitor.visit_before(child)


class AliasDeclaration(ASTNode):
    def __init__(self, identifier, type_id):
        self.identifier = identifier
        self.type_id = type_id

    def accept_print_visitor(self, visitor):
        visitor.visit_alias_declaration_before(self)


class EnclosedInParenthesis(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_enclosed_in_paren_before(self)


class Identifier(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept_print_visitor(self, visitor):
        visitor.visit_identifier_before(self)


class DeclaratorWithSpecifiers(ASTNode):
    def __init__(self, specifiers, declarator):
        self.specifiers = specifiers
        self.declarator = declarator

    def accept_print_visitor(self, visitor):
        visitor.visit_declarator_with_specifiers_before(self)


class OperatorFunction(ASTNode):
    def __init__(self, operator):
        self.operator = operator

    def accept_print_visitor(self, visitor):
        visitor.visit_operator_function_before(self)


class SimpleType(ASTNode):
    def __init__(self, type_name):
        self.type_name = type_name

    def accept_print_visitor(self, visitor):
        visitor.visit_simple_type_before(self)
