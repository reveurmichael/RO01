"""
Reference: https://yasenh.github.io/post/hungarian-algorithm-1/
"""

import networkx as nx  # Importing the NetworkX library for graph operations
import matplotlib.pyplot as plt  # Importing matplotlib for graph visualization

class Hungarian:
    def __init__(self, n_u, n_v, edges):
        # Initialize the Hungarian class with the number of vertices in sets U and V, and the list of edges
        self.num_vertices_U = n_u
        self.num_vertices_V = n_v
        self.G = nx.Graph()  # Create an empty undirected graph using NetworkX
        self.total_num = n_u + n_v  # Total number of vertices in both sets
        self.matching = {}  # Dictionary to store matching pairs
        self.visited = {}  # List to track visited vertices during the matching process

        # Add edges to the bipartite graph
        self.G.add_edges_from(edges)  # Add edges to the graph from the provided list

        # Initialize matching dictionary with -1 for all vertices
        for i in range(self.total_num):
            self.matching[i] = -1

        for v in range(self.num_vertices_U, self.total_num):
            self.visited[v] = False

    def run(self):
        total_matching = 0  # Counter to keep track of the total number of matchings found
        for i in range(self.num_vertices_U):
            print(f"Check Left node {i}")
            # Reset visited list for each vertex in set U
            for v in range(self.num_vertices_U, self.total_num):
                self.visited[v] = False
            if self.find_matching_with_augmenting_path(-1, i):  # Find matching using augmenting paths
                total_matching += 1  # Increment total matching count
                print("total_matching increased by 1")  # Print a message indicating a matching was found
                self.draw_graph()  # Visualize the current matching


        print("Final result")
        print("Total =", total_matching)  # Print the total number of matchings found
        for u, v in self.matching.items():
            if v != -1:
                print(u, "->", v)  # Print the matching pairs
        self.draw_graph()  # Final visualization of the bipartite graph with all matchings

    def find_matching_with_augmenting_path(self, caller, u):
        # Iterate through vertices in set V
        if u == -1:
            return
        print(f"find_matching_with_augmenting_path by {caller} for Left node {u}")
        for v in range(self.num_vertices_U, self.total_num):
            # Check if there is an edge between vertices from U and V and if v has not been visited
            if self.G.has_edge(u, v) and not self.visited[v]:
                print(f"check Right node {v} for Left node {u}")
                self.visited[v] = True  # Mark v as visited
                '''
                If v is not matched, we match it with u.
                If v is already matched, we explore other vertices in U
                to find a possible matching, following the unmatched -> matched -> unmatched pattern.
                '''
                to_update_matching = False
                if self.matching[v] == -1:
                    print(f"new matching found because self.matching[{v}] == -1")
                    to_update_matching = True
                if self.find_matching_with_augmenting_path(u, self.matching[v]):
                    print(f"new matching found because self.find_matching_with_augmenting_path({caller}, self.matching"
                          f"[{v}]) "
                          f"== True")
                    to_update_matching = True
                if to_update_matching:
                    print(f"matching found for node {u} and node {v}. No need to go further for the Right side.")
                    self.matching[v] = u  # Update the matching pairs
                    self.matching[u] = v
                    return True  # Matching found
        print(f"No matching found for Left node {u}")
        return False  # No matching found for u

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
