
import networkx as nx
import matplotlib.pyplot as plt

from graph.Graph import Graph

def print_graph(graph: Graph):
  G = nx.Graph()
  
   
  G.add_edges_from(graph.get_edges())
  G.add_nodes_from(graph.get_nodes())
  pos = nx.spring_layout(G)
  nx.draw_networkx(G, pos)

  plt.axis('equal')
  plt.savefig("graph.png")
  plt.show()