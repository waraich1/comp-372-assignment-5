import math
import random


def make_adj(size,adj_mat):
        edges = []
        for i in range(size):
            for j in range(i, size):
                if adj_mat[i][j] == 1:
                    edges.append((i, j))
        return edges

class Graph:
    def __init__(self, adj_mat,n):
        self.cover_graph = adj_mat
        self.size = n
        self.E = make_adj(n, self.cover_graph)
        self.V = range(n)

    def make_graphs():
      def random_adjacency_matrix():
        n = random.randint(4, 16)
        matrix = [[random.randint(0,1) for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = random.randint(0,1)    
                matrix[i][j] = matrix[j][i]

        for i in range(n):
            matrix[i][i] = 0
    
        return [matrix,n]
      graphs = []
      for i in range(101):
        graph = random_adjacency_matrix()
        graphs.append(Graph(graph[0],graph[1]))
      return graphs
        