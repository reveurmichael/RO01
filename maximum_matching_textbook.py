import networkx as nx
import matplotlib.pyplot as plt

class Hungarian:
    def __init__(self, n_u, n_v, edges):
        # Initialize the Hungarian class with the number of vertices in sets U and V, and the list of edges
        self.num_vertices_U = n_u
        self.num_vertices_V = n_v
        self.G = nx.Graph()  # Create an empty undirected graph using NetworkX
        self.total_num = n_u + n_v  # Total number of vertices in both sets
        self.matching = {}  # Dictionary to store matching pairs
        self.visited = []  # List to track visited vertices during the matching process

        # Add edges to the bipartite graph
        self.G.add_edges_from(edges)  # Add edges to the graph from the provided list

        # Initialize matching dictionary with -1 for all vertices
        for i in range(self.total_num):
            self.matching[i] = -1

    def run(self):
        # Step 0: Initialization
        # No vertices marked initially

        total_matching = 0  # Counter to keep track of the total number of matchings found
        while True:
            # Step 1: Search for an augmenting path
            self.visited = [False] * self.num_vertices_V  # Reset visited list for each vertex in set U
            if not self.find_augmenting_path():
                break  # Step 3: No more augmenting paths found, exit loop

            # Step 2: Improvement of matching
            self.improve_matching()

            total_matching += 1  # Increment total matching count
            self.draw_graph()  # Visualize the current matching
            print("total_matching increased by 1")  # Print a message indicating a matching was found

        print("Total =", total_matching)  # Print the total number of matchings found
        for u, v in self.matching.items():
            if v != -1:
                print(u, "->", v)  # Print the matching pairs
        self.draw_graph()  # Final visualization of the bipartite graph with all matchings

    def find_augmenting_path(self):
        # Step 1.0: Mark all unsaturated vertices in set U
        for x in range(self.num_vertices_U):
            if self.matching[x] == -1:
                self.visited[x] = True  # Mark unsaturated vertices in set U

        for x in range(self.num_vertices_U):
            if not self.visited[x]:  # Step 1.1: If all marked vertices are examined, exit loop
                continue

            # Step 1.2: For each edge [x, y] not in the matching
            for y in self.G.neighbors(x):
                if self.matching[x] != y:
                    continue  # Skip edges in the matching

                if not self.visited[y - self.num_vertices_U]:  # If y is not marked
                    self.visited[y - self.num_vertices_U] = True  # Mark y
                    break  # Return to Step 1.1

            else:  # Step 1.3: If y is unsaturated, it's the end of an augmenting path
                if self.matching[x] == -1:
                    return True  # Augmenting path found

                # Step 1.3 (continued): If y is saturated, find unique edge [x, y] in the matching
                for y in self.G.neighbors(x):
                    if self.matching[x] == y:
                        self.matching[x] = y  # Update matching
                        self.matching[y] = x
                        break  # Return to Step 1.1

        return False  # No augmenting path found

    def improve_matching(self):
        for x in range(self.num_vertices_U):
            if self.matching[x] == -1:
                continue  # Skip unsaturated vertices

            y = self.matching[x]
            self.matching.pop(x)
            self.matching.pop(y)

    def draw_graph(self):
        # Draw the bipartite graph with matching edges highlighted
        pos = nx.bipartite_layout(self.G, nodes=range(self.num_vertices_U))  # Compute the layout for visualization
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', font_weight='bold')  # Draw the graph
        matching_edges = [(u, v) for u, v in self.matching.items() if v != -1]  # Get matching edges
        nx.draw_networkx_edges(self.G, pos, edgelist=matching_edges, edge_color='red', width=2)  # Highlight matching edges
        plt.show()  # Show the graph visualization


if __name__ == "__main__":
    edges = [(0, 4), (0, 5), (1, 5), (1, 6), (2, 4), (2, 5), (3, 6), (1, 7), (3, 7)]
    # Create an instance of the Hungarian class with specified parameters and edges
    hungarian = Hungarian(4, 4, edges)
    hungarian.run()  # Run the Hungarian algorithm to find matchings
