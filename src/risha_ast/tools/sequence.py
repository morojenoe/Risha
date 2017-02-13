import warnings
from ..sequence import Sequence
from ..risha_ast import AliasDeclaration
from ..declarators.functions import FunctionDefinition


def get_alias_declarations(sequence):
    if not isinstance(sequence, Sequence):
        warnings.warn('Parameter must be an instance of risha_ast.Sequence')
        return None
    return filter(lambda elem: isinstance(elem, AliasDeclaration), sequence)


def get_functions(sequence):
    if not isinstance(sequence, Sequence):
        warnings.warn('Parameter must be an instance of risha_ast.Sequence')
        return None
    return filter(lambda elem: isinstance(elem, FunctionDefinition), sequence)
