import networkx as nx
import matplotlib.pyplot as plt

'''
In this code:

We define a function BIPAR that takes a graph G as input.
We initialize dictionaries colors and examined to keep track of colors and nodes' examination status.
We use a stack P to process nodes while checking for bipartiteness.
We initialize node 1 as red and start exploring the graph from there.
We assign colors 'red' and 'green' to nodes in alternating layers and check for conflicts in adjacent nodes' colors to determine bipartiteness.
We use NetworkX to visualize the bipartite graph with nodes colored according to their assigned colors.
Finally, we print whether the graph is bipartite or not based on the algorithm's result.
'''
def BIPAR(G):
    n = len(G.nodes)
    colors = {}  # Dictionary to store colors for each node
    examined = {}  # Dictionary to track examined nodes
    P = []  # Stack to store nodes for processing

    # Initialize colors and examined status for each node
    for i in range(1, n + 1):
        colors[i] = 'red' if i == 1 else 'white'  # Initialize colors, node 1 is initially red
        examined[i] = False

    bipartite = True  # Flag to track if the graph is bipartite

    # Process nodes using a stack
    P.append(1)  # Start with node 1
    while len(P) > 0:
        i = P.pop()  # Get the current node from the stack
        if colors[i] == 'red':
            for j in G.neighbors(i):
                if colors[j] == 'red':  # If a neighbor has the same color as i, the graph is not bipartite
                    bipartite = False
                if colors[j] == 'white':  # Assign the opposite color to the neighbor and add it to the stack
                    colors[j] = 'green'
                    P.append(j)
        else:  # i is green
            for j in G.neighbors(i):
                if colors[j] == 'green':  # If a neighbor has the same color as i, the graph is not bipartite
                    bipartite = False
                if colors[j] == 'white':  # Assign the opposite color to the neighbor and add it to the stack
                    colors[j] = 'red'
                    P.append(j)

    # Draw the bipartite graph with colors
    pos = nx.spring_layout(G)  # Position nodes using a spring layout
    node_colors = [colors[node] for node in G.nodes]  # Get node colors for visualization
    nx.draw(G, pos, with_labels=True, node_color=node_colors, font_color='black', font_weight='bold')
    plt.show()

    # Print the result
    if bipartite:
        print("G is bipartite")
    else:
        print("G is not bipartite")


# Create a sample graph
G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 6)]
G.add_edges_from(edges)

# Run the BIPAR algorithm on the graph and draw the result
BIPAR(G)
