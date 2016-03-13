from .risha_ast import ASTNode, CommaSeparatedList


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


class MemberDeclarator(ASTNode):
    def __init__(self, declarator, initializer):
        self.declarator = declarator
        self.initializer = initializer

    def accept(self, visitor):
        visitor.visit_member_declarator(self)


class MemberDeclaratorList(CommaSeparatedList):
    pass
