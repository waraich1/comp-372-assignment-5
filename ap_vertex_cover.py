import random
import time
from Graph import Graph


def gen_random(n):
  return random.randint(0,n-1)


def approximate_vertex(E,minK):
    C = []
    E_tag = E.copy()
    while len(E_tag) > 0:
        c = E_tag.pop(gen_random(len(E_tag)))
        C.append(c[0])
        C.append(c[1])
        for e in E_tag:
            if e[0] in C or e[1] in C:
                E_tag.remove(e)
    res = len(C)
    return [C,res < minK] 

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
  minK = random.randint(0,15)
  vertex_cover.append(approximate_vertex(edges,minK))
  if not vertex_cover[-1][1]:
    print("The value vertex cover is more than k"+" = " + str(minK))
  else:
    print("The value vertex cover is less than k"+" = " + str(minK)+ " "+"with vertex cover  " + str(vertex_cover[-1][0]))
end = time.time()
print(f"run took {end-start} seconds")


