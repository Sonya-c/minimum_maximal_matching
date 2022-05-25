from typing import List, Tuple, Dict


class Graph:
  edges: List[Tuple[any, any]]
  nodes: Dict[any, List[any]]

  def __init__(self,
               nodes: Dict[any, List[any]] = {},
               edges: List[Tuple[any, any]] = []
              ) -> None:
    self.nodes = nodes
    self.edges = edges

  
  def add_node(self, node: any) -> None:
    """Añade un vertice a la lista de vertices

    Args:
      node (any): nodo para añadir
    """
    self.nodes[node] = self.nodes.get(node, []) # crear un nodo vacio

    
  def add_edge(self, edge: Tuple[any, any]) -> None:
    """Añade una aristas al conjunto de aristas

    Args:
      edge (Tuple[any, any]): Es una tupla de nodos (los extremos de la arista)
    """
    # añadir el vertice a la lista de vertice
    if not any(sorted(e) == sorted(edge) for e in self.edges):
      self.edges.append(edge) 

    # Añadir nodos si no exiten
    self.nodes[edge[0]] = self.nodes.get(edge[0], [])
    self.nodes[edge[1]] = self.nodes.get(edge[1], [])

    # Añadir los nodos adyacentes
    
    if (edge[1] not in self.nodes[edge[0]]):
      self.nodes[edge[0]].append(edge[1])

    if (edge[0] not in self.nodes[edge[1]]):
      self.nodes[edge[1]].append(edge[0])
    

  def get_nodes(self) -> Dict[any, List[any]]:
    """Regresa el diccionario de nodos

    Returns: 
      Dict[any, List[any]]
    """
    return self.nodes

  
  def get_edges(self) -> List[Tuple[any, any]]:
    """Regresa el conjunto de artistas como una lista de tuplas

    Returns: 
      List[Tuple[any, any]]
    """
    return self.edges

  
  def remove_node(self, node: any) -> None:
    """Dado un nodo, eliminar ese nodo de la lista de nodos y todas las aristas que lo contienen

    Args: 
      node (any)
    """ 
    if node in self.nodes:
      del self.nodes[node] # eliminar el nodo
  
      # eliminar ese nodo del conjunto de vecinos de los nodos sobrantes
      for neighbours in self.nodes.values():
        try:
          neighbours.remove(node)
        except ValueError:
          pass

    # eliminar el nodo del conjunto de aristas
    edges = list(self.edges)
    for edge in edges:
      if (edge[0] == node or edge[1] == node):
        self.edges.remove(edge)

  
  def remove_edge(self, edge: Tuple[any]) -> None:
    """Elimina una arista del conjunto de aristas

    Args: 
      edge (Tuple[any]): arista a eliminar
    """
    
    # eliminar de la lista de nodos

    if (any(sorted(e) == sorted(edge) for e in self.edges)):
      self.edges.remove(edge)

      try:
        self.nodes.get(edge[0], []).remove(edge[1])
      except ValueError:
        pass
        
      try:
        self.nodes.get(edge[1], []).remove(edge[0])
      except ValueError:
          pass

  def node_len(self) -> int:
    return len(self.nodes)
  
  def edges_len(self) -> int:
    return len(self.edges)
