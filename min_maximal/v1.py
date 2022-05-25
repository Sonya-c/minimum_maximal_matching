from graph import Graph

def min_maximal(graph: Graph, match=[], min_match=[]):
  
  if (graph.edges_len() == 0):
    # Hay mas vertices que analizar
    if (len(min_match) == 0 or len(match) < len(min_match)):
      return match
  else:
    
    for edge in graph.get_edges(): # (1) seleccionar un vertice
      match_i = list(match)
      graph_i = Graph(
        dict(graph.get_nodes()),
        list(graph.get_edges())
      )
      
      # añadir la aristas al emparejamiento
      # y eliminar esa arista del grafo
      match_i.append(edge)
      graph_i.remove_node(edge[0])
      graph_i.remove_node(edge[1])

      min_match = min_maximal(graph_i, match_i, min_match)

  return min_match