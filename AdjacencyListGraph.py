
from base_graph import BaseGraph, Node


class AdjacencyListGraph(BaseGraph):
    def __init__(self,*,allow_loops:bool = False)->None:
        super().__init__(is_directed=False,allow_loops=allow_loops)
        self._adj:dict[Node,dict[Node,float]] = {}

    def add_node(self,node:Node)->None:
        if node not in self._adj: self._adj[node] = {}
    def has_node(self, node: Node) -> bool:
        return node in self._adj
    def nodes(self)->list[Node]:
        return list(self._adj)
    def add_edge(self,u:Node,v:Node,weight:float|None)->None:
        if u==v and not self.allow_loops: raise ValueError("Brak wierzcholkow")
        if u not in self._adj: raise KeyError("")
        if v not in self._adj: raise KeyError("")
        self._adj[u][v] = weight
        self._adj[v][u] = weight
    def has_edge(self,u:Node,v:Node)->bool:
        return u in self._adj and v in self._adj[u]
    def neighbors(self,node:Node)->list[Node]:
        return list(self._adj[node])
    def edges(self):
        visited = set()
        for u in self._adj:
            for v,w in self._adj[u].items():
                if  v not in visited:
                    yield (u,v,w)
            visited.add(u)
    def edge_weight(self, u: Node, v: Node) -> float|None:
        if u not in self._adj: raise KeyError("")
        if v not in self._adj: raise KeyError("")
        return self._adj[u][v]

