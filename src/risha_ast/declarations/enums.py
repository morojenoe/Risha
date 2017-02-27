from ..risha_ast import ASTNode


class EnumDefinition(ASTNode):
    def __init__(self, enum_head, enumerators):
        self.enum_head = enum_head
        self.enumerators = enumerators if enumerators is not None else []

    def accept_print_visitor(self, visitor):
        visitor.visit_enum_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_enum_before(self)
        self.enum_head.accept_before_after(visitor)
        self.enumerators.accept_before_after(visitor)
        visitor.visit_enum_after(self)

    @property
    def identifier(self):
        return self.enum_head.identifier


class EnumKey(ASTNode):
    def __init__(self, enum_key):
        self.enum_key = enum_key

    def accept_print_visitor(self, visitor):
        visitor.visit_enum_key_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_enum_key_before(self)
        visitor.visit_enum_key_after(self)


class EnumHead(ASTNode):
    def __init__(self, enum_key, identifier):
        self.enum_key = enum_key
        self.identifier = identifier

    def accept_print_visitor(self, visitor):
        visitor.visit_enum_head_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_enum_head_before(self)
        self.enum_key.accept_before_after(visitor)
        if self.identifier is not None:
            self.identifier.accept_before_after(visitor)
        visitor.visit_enum_head_after(self)


class Enumerator(ASTNode):
    def __init__(self, enumerator, const_expression):
        self.enumerator = enumerator
        self.const_expression = const_expression

    def accept_print_visitor(self, visitor):
        visitor.visit_enumerator_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_enumerator_before(self)
        self.enumerator.accept_before_after(visitor)
        if self.const_expression is not None:
            self.const_expression.accept_before_after(visitor)
        visitor.visit_enumerator_after(self)


class EnumeratorList(ASTNode):
    def __init__(self):
        self.enumerators = []

    def add_enumerator(self, enumerator):
        self.enumerators.append(enumerator)
        return self

    def accept_print_visitor(self, visitor):
        visitor.visit_enumerator_list_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_enumerator_list_before(self)
        for enumerator in self.enumerators:
            enumerator.accept_before_after(visitor)
        visitor.visit_enumerator_list_after(self)
