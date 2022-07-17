import itertools
from Graph import Graph
import time
import random

def get_sub_graphs(G, k):
    r = range(0, G.size)
    combs = list(itertools.combinations(r, k))
    return combs

def is_vertex(G, comb):
    edges_touched = 0
    
    for e in G.E:
        if e[0] in comb or e[1] in comb:
            edges_touched += 1

    return True if edges_touched == len(G.E) else False
    
def find_minimum_vertex(G,minK):
  result = [None,False]
  for k in range (1, G.size):
      combs = get_sub_graphs(G, k)
      for comb in combs:
          if is_vertex(G, comb) and len(comb) < minK:
              result = [comb,True]
  return result


start = time.time()
graphs = Graph.make_graphs()
for g in graphs:
  minK = random.randint(0,10)
  result = find_minimum_vertex(g,minK)
  if not result[1]:
    print("The value vertex cover is more than k"+" = " + str(minK))
  else:
    print("The value vertex cover is less than k"+" = " + str(minK)+ " "+"with vertex cover  " + str(result[0]))

end = time.time()
print(f"run took {end-start} seconds")