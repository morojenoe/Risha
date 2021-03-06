import abc


class ASTNode(metaclass=abc.ABCMeta):
    def __init__(self, row, col):
        super().__init__()
        self._row = row
        self._col = col

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @abc.abstractclassmethod
    def accept_print_visitor(self, visitor):
        pass

    @abc.abstractclassmethod
    def accept_before_after(self, visitor):
        pass


class AliasDeclaration(ASTNode):
    def __init__(self, identifier, type_id, row, col):
        super().__init__(row, col)
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
    def __init__(self, expression, row, col):
        super().__init__(row, col)
        self.expression = expression

    def accept_print_visitor(self, visitor):
        visitor.visit_enclosed_in_paren_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_enclosed_in_paren_before(self)
        self.expression.accept_before_after(visitor)
        visitor.visit_enclosed_in_paren_after(self)


class Identifier(ASTNode):
    def __init__(self, identifier, row, col):
        super().__init__(row, col)
        self._identifier = identifier

    def accept_print_visitor(self, visitor):
        visitor.visit_identifier_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_identifier_before(self)
        visitor.visit_identifier_after(self)

    def as_string(self):
        return self._identifier

    def to_string(self):
        return self._identifier

    @property
    def identifier(self):
        return self._identifier


class OperatorFunction(ASTNode):
    def __init__(self, operator, row, col):
        super().__init__(row, col)
        self.operator = operator

    def accept_print_visitor(self, visitor):
        visitor.visit_operator_function_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_operator_function_before(self)
        visitor.visit_operator_function_after(self)


class SimpleType(ASTNode):
    def __init__(self, type_name, row, col):
        super().__init__(row, col)
        self.type_name = type_name

    def accept_print_visitor(self, visitor):
        visitor.visit_simple_type_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_simple_type_before(self)
        visitor.visit_simple_type_after(self)

    @property
    def name(self):
        return self.type_name


class IdentifierCheck(ASTNode):
    def __init__(self, node, row, col):
        super().__init__(row, col)
        self.node = node

    def accept_print_visitor(self, visitor):
        visitor.visit_identifier_check_before(self)

    def accept_before_after(self, visitor):
        visitor.visit_identifier_check_before(self)
        self.node.accept_before_after(visitor)
        visitor.visit_identifier_check_after(self)
