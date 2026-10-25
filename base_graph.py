from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Hashable, Iterable

Node = Hashable
Edge = tuple[Node, Node, float | None]


class BaseGraph(ABC):
    """
    Bazowa klasa abstrakcyjna dla grafu prostego.

    Kontrakt:
    - graf może być skierowany lub nieskierowany,
    - pętle są dozwolone tylko przy allow_loops=True,
    - graf nie jest multigrafem,
    - ponowne add_edge(u, v, weight) aktualizuje wagę istniejącej krawędzi,
    - add_edge wymaga istnienia obu wierzchołków.
    """

    def __init__(self, *, is_directed: bool = False, allow_loops: bool = False) -> None:
        self._is_directed = is_directed
        self._allow_loops = allow_loops

    @property
    def is_directed(self) -> bool:
        return self._is_directed

    @property
    def allow_loops(self) -> bool:
        return self._allow_loops

    @abstractmethod
    def add_node(self, node: Node) -> None:
        ...

    @abstractmethod
    def add_edge(self, u: Node, v: Node, weight: float | None = None) -> None:
        ...

    @abstractmethod
    def remove_node(self, node: Node) -> None:
        ...

    @abstractmethod
    def remove_edge(self, u: Node, v: Node) -> None:
        ...

    @abstractmethod
    def has_node(self, node: Node) -> bool:
        ...

    @abstractmethod
    def has_edge(self, u: Node, v: Node) -> bool:
        ...

    @abstractmethod
    def neighbors(self, node: Node) -> Iterable[Node]:
        ...

    @abstractmethod
    def nodes(self) -> Iterable[Node]:
        ...

    @abstractmethod
    def edges(self) -> Iterable[Edge]:
        ...

    @abstractmethod
    def edge_weight(self, u: Node, v: Node) -> float | None:
        ...

    def __contains__(self, node: Node) -> bool:
        return self.has_node(node)

    def __iter__(self):
        return iter(self.nodes())

    def __len__(self) -> int:
        return self.number_of_nodes()

    def number_of_nodes(self) -> int:
        return sum(1 for _ in self.nodes())

    def number_of_edges(self) -> int:
        return sum(1 for _ in self.edges())

    def degree(self, node: Node) -> int:
        if self.is_directed:
            raise TypeError("Use out_degree or in_degree for directed graphs.")
        return sum(1 for _ in self.neighbors(node))

    def out_degree(self, node: Node) -> int:
        return sum(1 for _ in self.neighbors(node))

    def in_degree(self, node: Node) -> int:
        if not self.has_node(node):
            raise KeyError(node)
        return sum(1 for u in self.nodes() if self.has_edge(u, node))
