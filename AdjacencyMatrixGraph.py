from base_graph import BaseGraph, Node, Edge


_NO_EDGE = object()


class AdjacencyMatrixGraph(BaseGraph):
    def __init__(self, *, allow_loops: bool = False) -> None:
        super().__init__(is_directed=False, allow_loops=allow_loops)
        self._nodes = []
        self._index = {}
        self._matrix = []

    def add_node(self, node: Node) -> None:
        if node in self._index:
            return

        self._index[node] = len(self._nodes)
        self._nodes.append(node)

        for row in self._matrix:
            row.append(_NO_EDGE)

        self._matrix.append([_NO_EDGE] * len(self._nodes))

    def add_edge(self, u: Node, v: Node, weight: float | None = None) -> None:
        if u not in self._nodes: raise KeyError()
        if v not in self._nodes: raise KeyError()
        if u==v and self._allow_loops == False: raise ValueError()
        i = self._index[u]
        j = self._index[v]
        self._matrix[i][j] = weight
        self._matrix[j][i] = weight


    def remove_node(self, node: Node) -> None:
        # 1. Sprawdź, czy node istnieje.
        # 2. Usuń odpowiedni element z _nodes.
        # 3. Usuń wiersz i kolumnę z macierzy.
        # 4. Przebuduj _index.
        if node not in self._nodes: raise KeyError()
        i = self._index[node]
        self._matrix.pop(i)
        for row in self._matrix:
            row.pop(i)
        self._nodes.pop(i)
        self._index.clear()
        for n,e in enumerate(self._nodes):
            self._index[e] = n

    def remove_edge(self, u: Node, v: Node) -> None:
        # Ustaw oba pola macierzy na _NO_EDGE.
        if u not in self._nodes: raise KeyError()
        if v not in self._nodes: raise KeyError()
        self._matrix[self._nodes.index(u)][self._nodes.index(v)] = _NO_EDGE
        self._matrix[self._nodes.index(v)][self._nodes.index(u)] = _NO_EDGE
    def has_node(self, node: Node) -> bool:
        return node in self._index

    def has_edge(self, u: Node, v: Node) -> bool:
        # Krawędź istnieje wtedy i tylko wtedy,
        # gdy komórka macierzy nie jest _NO_EDGE.
        if u not in self._nodes: raise KeyError()
        if v not in self._nodes: raise KeyError()
        i = self._index[u]
        j = self._index[v]
        if self._matrix[i][j] is not _NO_EDGE: return True
        else: return False
    def neighbors(self, node: Node):
        # Zwróć te wierzchołki, których komórki w wierszu
        # nie są równe _NO_EDGE.
        result = []
        if node not in self._nodes: raise KeyError()
        j = self._index[node]
        for i in range(len(self._matrix[j])):
            if self._matrix[j][i] is not _NO_EDGE:
                result.append(self._nodes[i])
        return result

    def nodes(self):
        return tuple(self._nodes)

    def edges(self):
        # Ponieważ graf jest nieskierowany, każdą krawędź
        # zwracaj tylko raz.
        for i in range(len(self._matrix)):
            for j in range(i,len(self._matrix[i])):
                if self._matrix[i][j] is not _NO_EDGE:
                    yield (self._nodes[i],self._nodes[j],self._matrix[i][j])

    def edge_weight(self, u: Node, v: Node):
        # Jeśli krawędź nie istnieje, zgłoś KeyError.
        # W przeciwnym razie zwróć wagę, nawet jeśli jest nią None.
        if not self.has_edge(u,v): raise KeyError()
        i = self._index[u]
        j = self._index[v]
        return self._matrix[i][j]


