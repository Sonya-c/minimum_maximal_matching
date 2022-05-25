from graph import Graph

def max_edge(nodes):
  node_1, len_1 = None, 0
  node_2, len_2 = None, 0
  
  for n1 in nodes.keys():
    if (len(nodes[n1]) >= len_1 and node_2 != n1):
      len_1 = len(nodes[n1])
      
      for n2 in nodes[n1]:
        if (len(nodes[n2]) >= len_2 and n1 != n2):
          len_2 = len(nodes[n2])
          node_1 = n1
          node_2 = n2

  return (node_1, node_2)
  
def min_maximal(graph: Graph, match=[], min_match=[]):

  if (graph.edges_len() == 0):
    # Hay mas vertices que analizar
    if (len(min_match) == 0 or len(match) < len(min_match)):
      return match
  else:
    
    # (1) seleccionar un vertice
    edge = max_edge(graph.get_nodes())
    
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