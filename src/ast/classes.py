from .risha_ast import ASTNode, CommaSeparatedList, Sequence


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


class MemberSpecification(Sequence):
    def add(self, element):
        self.elements.insert(0, element)
        return self


class MemberDeclarator(ASTNode):
    def __init__(self, declarator, initializer):
        self.declarator = declarator
        self.initializer = initializer

    def accept(self, visitor):
        visitor.visit_member_declarator(self)


class MemberDeclaratorList(CommaSeparatedList):
    pass


class MemberDeclaration(ASTNode):
    def __init__(self, specifiers, declarator_list):
        self.specifiers = specifiers
        self.declarator_list = declarator_list

    def accept(self, visitor):
        visitor.visit_member_declaration(self)
