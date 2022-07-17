import random
import time
from Graph import Graph


def gen_random(n):
  return random.randint(0,n-1)


def approximate_vertex(E):
    C = []
    E_tag = E.copy()
    while len(E_tag) > 0:
        c = E_tag.pop(gen_random(len(E_tag)))
        C.append(c[0])
        C.append(c[1])
        for e in E_tag:
            if e[0] in C or e[1] in C:
                E_tag.remove(e)
    return len(C)

def get_edges(adj_matrix):
    edges = []
    for i in range(len(adj_matrix)):
        for j in range(i, len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                edges.append((i, j))
    return edges

start = time.time()
graphs = Graph.make_graphs()
vertex_cover = []
for g in graphs:
  edges = get_edges(g.cover_graph)
  vertex_cover.append(approximate_vertex(edges))
end = time.time()
print(vertex_cover)
print(f"run took {end-start} seconds")


