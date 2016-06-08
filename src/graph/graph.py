from .algorithms import get_cycle, is_cycle_exist, get_topological_ordering


class OrientedGraph:
    def __init__(self):
        self._graph = {}

    def add_edge(self, v, u):
        if v in self._graph:
            self._graph[v].append(u)
        else:
            self._graph[v] = [u]

    def get_all_vertexes(self):
        return self._graph.keys()

    def get_neighbors(self, v):
        return self._graph[v]

    def is_cycle_exist(self):
        return is_cycle_exist(self)

    def get_any_cycle(self):
        return get_cycle(self)

    def get_topological_ordering(self):
        return get_topological_ordering(self)
