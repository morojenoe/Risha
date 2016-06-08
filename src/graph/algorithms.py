import enum


class VertexState(enum.Enum):
    UnVisited = 1
    Visited = 2
    Finished = 3


def _find_cycle(v, graph, used, stack):
    used[v] = VertexState.Visited
    stack.append(v)

    for u in graph.get_neighbors(v):
        if used[u] == VertexState.UnVisited:
            _find_cycle(u, graph, used, stack)
        if used[u] == VertexState.Visited:
            return stack[stack.index(u):]
    stack.pop()
    used[v] = VertexState.Finished
    return None


def get_cycle(graph):
    used = {}
    for v in graph.get_all_vertexes():
        used[v] = VertexState.UnVisited
    for v in graph.get_all_vertexes():
        if used[v] == VertexState.UnVisited:
            cycle = _find_cycle(v, graph, used, [])
            if cycle is not None:
                return cycle
    return None


def is_cycle_exist(graph):
    cycle = get_cycle(graph)
    return True if cycle is not None else False


def _topo_sort(v, graph, used, order):
    used[v] = VertexState.Visited
    for u in graph.get_neighbors(v):
        if used[u] == VertexState.UnVisited:
            _find_cycle(u, graph, used, order)
    order.append(v)


def get_topological_ordering(graph):
    used = {}
    for v in graph.get_all_vertexes():
        used[v] = VertexState.UnVisited
    order = []
    for v in graph.get_all_vertexes():
        if used[v] == VertexState.UnVisited:
            _topo_sort(v, graph, used, order)
    order.reverse()
    return order
