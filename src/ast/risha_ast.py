import abc


class ASTNode(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def accept(self, visitor):
        pass


class Sequence(ASTNode):
    def __init__(self):
        self.sequence = []

    def add(self, element):
        self.sequence.append(element)
        return self

    def accept(self, visitor):
        visitor.visit_sequence(self)


class CommaSeparatedList(ASTNode):
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)
        return self

    def accept(self, visitor):
        visitor.visit_comma_separated_list(self)


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


class AliasDeclaration(ASTNode):
    def __init__(self, identifier, type_id):
        self.identifier = identifier
        self.type_id = type_id

    def accept(self, visitor):
        visitor.visit_alias_declaration(self)


class EnclosedInParenthesis(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_enclosed_in_paren(self)


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
