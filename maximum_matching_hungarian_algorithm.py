import networkx as nx
import matplotlib.pyplot as plt


class Hungarian:
    def __init__(self, n_u, n_v, edges):
        self.num_vertices_U = n_u
        self.num_vertices_V = n_v
        self.G = nx.Graph()
        self.total_num = n_u + n_v
        self.matching = {}
        self.visited = []

        # Add edges to the bipartite graph
        self.G.add_edges_from(edges)

        for i in range(self.total_num):
            self.matching[i] = -1

    def run(self):
        total_matching = 0
        for i in range(self.num_vertices_U):
            self.visited = [False] * self.num_vertices_V
            if self.find_augmenting_path(i):
                total_matching += 1
                self.draw_graph()
                print("total_matching increased by 1")

        print("Total =", total_matching)
        for u, v in self.matching.items():
            if v != -1:
                print(u, "->", v)
        self.draw_graph()

    def draw_graph(self):
        # Draw the bipartite graph with matching edges highlighted
        pos = nx.bipartite_layout(self.G, nodes=range(self.num_vertices_U))
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
        matching_edges = [(u, v) for u, v in self.matching.items() if v != -1]
        nx.draw_networkx_edges(self.G, pos, edgelist=matching_edges, edge_color='red', width=2)
        plt.show()

    def find_augmenting_path(self, u):
        for v in range(self.num_vertices_U, self.total_num):
            if self.G.has_edge(u, v) and not self.visited[v - self.num_vertices_U]:
                self.visited[v - self.num_vertices_U] = True
                if self.matching[v] == -1 or self.find_augmenting_path(self.matching[v]):
                    self.matching[v] = u
                    self.matching[u] = v
                    return True
        return False


if __name__ == "__main__":
    edges = [(0, 4), (0, 5), (1, 5), (1, 6), (2, 4), (2, 5), (3, 6), (1, 7), (3, 7)]
    hungarian = Hungarian(4, 4, edges)
    hungarian.run()
