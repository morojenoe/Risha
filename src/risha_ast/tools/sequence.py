import warnings
from ..sequence import Sequence


def filter_sequence(sequence, ast_node):
    if not isinstance(sequence, Sequence):
        warnings.warn('Parameter must be an instance of risha_ast.Sequence')
        return None
    return filter(lambda elem: isinstance(elem, ast_node), sequence)
