from .risha_ast import ASTNode, Sequence, CommaSeparatedList


class ClassHead(ASTNode):
    def __init__(self, class_key, class_name):
        self.class_key = class_key
        self.class_name = class_name

    def accept_print_visitor(self, visitor):
        visitor.visit_class_head_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_class_head_before(self)
        visitor.visit_class_head_after(self)


class ClassDefinition(ASTNode):
    def __init__(self, class_head, member_specification):
        self.class_head = class_head
        self.member_specification = member_specification

    def accept_print_visitor(self, visitor):
        visitor.visit_class_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_class_before(self)
        self.class_head.accept_before_after(visitor)
        self.member_specification.accept_before_after(visitor)
        visitor.visit_class_after(self)


class MemberSpecification(Sequence):
    def add(self, element):
        self.elements.insert(0, element)
        return self


class MemberDeclarator(ASTNode):
    def __init__(self, declarator, initializer):
        self.declarator = declarator
        self.initializer = initializer

    def accept_print_visitor(self, visitor):
        visitor.visit_member_declarator_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_member_declarator_before(self)
        self.declarator.accept_before_after(visitor)
        if self.initializer is not None:
            self.initializer.accept_before_after(visitor)
        visitor.visit_member_declarator_after(self)


class MemberDeclaratorList(CommaSeparatedList):
    pass
