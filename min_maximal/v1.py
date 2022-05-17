from graph import Graph, remove_adj

def min_maximal(graph: Graph, match=[]):

  if (graph.edges_len() == 0):
    # Hay mas vertices que analizar
    print(match)
    return 

  else:
    
    for edge in graph.get_edges():
      
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
      min_maximal(graph_i, match_i)