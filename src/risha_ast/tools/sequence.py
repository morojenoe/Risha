import warnings
from ..sequence import Sequence
from ..risha_ast import AliasDeclaration


def get_alias_declarations(sequence):
    if not isinstance(sequence, Sequence):
        warnings.warn('Parameter must be an instance of risha_ast.Sequence')
        return None
    return filter(lambda e: isinstance(e, AliasDeclaration), sequence)
