import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            yield node
            stack.extend(reversed(list(graph.neighbors(node))))

def draw_graph_with_dfs(graph, start):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))
    visited = set()
    visited_edges = set()
    prev_node = None

    for i, node in enumerate(dfs(graph, start)):
        # Draw graph
        nx.draw(graph, pos, with_labels=True, node_size=800, arrows=True)

        # Update visited nodes and edges
        visited.add(node)
        if i > 0:
            visited_edges.add((prev_node, node))

        # Draw visited nodes and edges in red, unvisited in blue
        node_colors = ['red' if n in visited else 'blue' for n in graph.nodes()]
        edge_colors = ['red' if (u, v) in visited_edges or (v, u) in visited_edges else 'blue' for u, v in graph.edges()]

        nx.draw_networkx_nodes(graph, pos, node_color=node_colors)
        nx.draw_networkx_edges(graph, pos, edge_color=edge_colors)

        # Update previous node
        prev_node = node

        plt.title(f'Depth First Search (DFS) - Step {i+1}')
        plt.pause(1)  # Pause to show each step
        plt.clf()

# Example usage:
G = nx.DiGraph()  # Directed graph
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
draw_graph_with_dfs(G, 1)
plt.show()