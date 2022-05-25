from graph.Graph import Graph
import random

def random_graph(m: int):
  V = [i for i in range(1, m + 1)]
  graph = Graph()

  while len(graph.get_edges()) < m:
    v1 = random.choice(V)
    v2 = random.choice([v for v in V if v != v1])
    graph.add_edge((v1, v2))
  
  return graph