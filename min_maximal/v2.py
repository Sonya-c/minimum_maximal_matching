from graph import Graph, remove_adj

def max_edge(graph):
  return (0,0)
  
def min_maximal(graph, match=[]):
  # seleccionar la artista de mayor grado
  edge = max_edge(graph)

  graph_i = Graph(graph)
  match_i = list(match)

  # seleccionar un vertice y marcarlo
  graph_i.remove_edge(edge)
  match_i.append(edge)

  # remover todas las aristas adyacentes
  # a los estremos de la aristas
  remove_adj(edge[0], graph_i)
  remove_adj(edge[1], graph_i)

  # repetir
  min_maximal(graph, match)