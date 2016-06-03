from .risha_ast import ASTNode, CommaSeparatedList
from .sequence import Sequence


class ClassHead(ASTNode):
    def __init__(self, class_key, class_name):
        self._class_key = class_key
        self._class_name = class_name

    def accept_print_visitor(self, visitor):
        visitor.visit_class_head_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_class_head_before(self)
        visitor.visit_class_head_after(self)

    def name_as_string(self):
        return self._class_name.as_string()

    @property
    def class_key(self):
        return self._class_key

    @property
    def class_name(self):
        return self._class_name


class ClassDefinition(ASTNode):
    def __init__(self, class_head, member_specification):
        self._class_head = class_head
        self._members = member_specification

    def accept_print_visitor(self, visitor):
        visitor.visit_class_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_class_before(self)
        self._class_head.accept_before_after(visitor)
        self._members.accept_before_after(visitor)
        visitor.visit_class_after(self)

    @property
    def name_as_string(self):
        return self._class_head.name_as_string

    @property
    def class_head(self):
        return self._class_head

    @property
    def members(self):
        return self._members

    @property
    def name(self):
        return self._class_head.class_name


class MemberSpecification(Sequence):
    def add(self, element):
        self.elements.insert(0, element)
        return self


class MemberDeclaratorList(CommaSeparatedList):
    pass
