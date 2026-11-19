from jinja2.bccache import bc_version

def dfs(graph, start):
    if not graph.has_node(start):
        raise KeyError(start)
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in reversed(list(graph.neighbors(node))):
            if neighbor not in visited:
                stack.append(neighbor)

    return tuple(order)