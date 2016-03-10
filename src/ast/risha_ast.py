import abc


class ASTNode(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def accept(self, visitor):
        pass


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


class ForLoop(ASTNode):
    def __init__(self, for_init_statement, condition, expression, statement):
        self.for_init_statement = for_init_statement
        self.condition = condition
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        visitor.visit_for(self)


class CompoundStatement(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        visitor.visit_compound_statement(self)


class AliasDeclaration(ASTNode):
    def __init__(self, identifier, type_id):
        self.identifier = identifier
        self.type_id = type_id

    def accept(self, visitor):
        visitor.visit_alias_declaration(self)


class IfStatement(ASTNode):
    def __init__(self, condition, statement, else_statement):
        self.condition = condition
        self.statement = statement
        self.else_statement = else_statement

    def accept(self, visitor):
        visitor.visit_if(self)


class EnclosedInParenthesis(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_enclosed_in_paren(self)


class DeclSpecifierSeq(ASTNode):
    def __init__(self):
        self.decl_specifiers = []

    def add_decl_specifier(self, decl_specifier):
        self.decl_specifiers.append(decl_specifier)
        return self

    def accept(self, visitor):
        visitor.visit_decl_specifier_seq(self)


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
