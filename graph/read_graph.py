from graph.Graph import Graph
import re
def read_graph(file_url: str) -> Graph:
  graph = Graph()

  with open(file_url, "r") as file:
    file.seek(3) # ir a la segunda linea

    for node_1, line in enumerate(file):
      for node_2, col in enumerate(line.replace("\n", "").split()):
        if (int(col) != 0):
          graph.add_edge((node_1 + 1, node_2 + 1))
          
  return graph