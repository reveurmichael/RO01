import networkx as nx
import matplotlib.pyplot as plt
import random

def recursive_tsp(G, current_node, visited, path_length, min_path):
    if len(visited) == len(G.nodes):
        # If all nodes have been visited, return to the starting node
        return path_length + G[current_node][visited[0]]['weight'], visited + [visited[0]]

    for neighbor in G.neighbors(current_node):
        if neighbor not in visited:
            new_visited = visited + [neighbor]
            new_length = path_length + G[current_node][neighbor]['weight']
            if new_length < min_path[0]:
                min_path = recursive_tsp(G, neighbor, new_visited, new_length, min_path)

    return min_path

def draw_tsp_path(G, path, title):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)] + [(path[-1], path[0])], edge_color='r', width=2)
    plt.title(title)
    plt.show()

# Create a graph with 7 nodes
G = nx.complete_graph(7)

# Assign random weights to the edges
for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)  # Assigning random weights between 1 and 10

# Choose a starting node
start_node = 0

# Find the optimal TSP path using recursive algorithm
min_path = recursive_tsp(G, start_node, [start_node], 0, (float('inf'), []))[1]
print("Optimal TSP Path:", min_path)

# Visualize the TSP path
draw_tsp_path(G, min_path, "Optimal TSP Path")
