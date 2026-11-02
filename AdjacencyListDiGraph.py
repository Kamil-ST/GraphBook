from base_graph import BaseGraph, Node, Edge


class AdjacencyListDiGraph(BaseGraph):
    def __init__(self, *, allow_loops: bool = False) -> None:
        super().__init__(is_directed=True, allow_loops=allow_loops)
        self._adj = {}

    def add_node(self, node: Node) -> None:
        if node not in self._adj: self._adj[node] = {}

    def add_edge(self, u: Node, v: Node, weight: float | None = None) -> None:
        if u == v and self.allow_loops == False: raise ValueError("Loops are not allowed")
        if u not in self._adj: raise KeyError(u)
        if v not in self._adj: raise KeyError(v)
        self._adj[u][v] = weight

    def remove_node(self, node: Node) -> None:
        if node not in self._adj: raise KeyError("node not in nodes")
        del self._adj[node]
        for v in self._adj.values():
            v.pop(node, None)

    def remove_edge(self, u: Node, v: Node) -> None:
        if u not in self._adj: raise KeyError("")
        if v not in self._adj: raise KeyError("")
        if v not in self._adj: raise KeyError((u, v))
        del self._adj[u][v]

    def has_node(self, node: Node) -> bool:
        return node in self._adj

    def has_edge(self, u: Node, v: Node) -> bool:
        if v not in self._adj: return False
        if u not in self._adj: return False
        if v in self._adj[u]: return True

    def neighbors(self, node: Node):
        if node not in self._adj: raise KeyError("")
        return self._adj[node]

    def nodes(self):
        return list(self._adj.keys())

    def edges(self):
        for u in self._adj:
            for v in self._adj[u]:
                yield u, v, self._adj[u][v]

    def edge_weight(self, u: Node, v: Node):
        if u in self._adj and v in self._adj[u]:
            return self._adj[u][v]
        else:
            raise KeyError("")
