from typing import List, Tuple, Dict


class Graph:
  edges: List[Tuple[int, int]]
  nodes: Dict[int, List[int]]
  
  def __init__(self,
               nodes: Dict[int, List[int]] = {},
               edges: List[Tuple[int, int]] = []
              ) -> None:
    self.nodes = nodes
    self.edges = edges

  
  def add_node(self, node: int) -> None:
    """Añade un vertice a la lista de vertices

    Args:
      node (int): nodo para añadir
    """
    self.nodes[node] = self.nodes.get(node, []) # crear un nodo vacio

    
  def add_edge(self, edge: Tuple[int, int]) -> None:
    """Añade una aristas al conjunto de aristas

    Args:
      edge (Tuple[int, int]): Es una tupla de nodos (los extremos de la arista)
    """
    self.edges.append(edge) # añadir el vertice a la lista de vertice

    # Añadir nodos si no exiten
    self.nodes[edge[0]] = self.nodes.get(edge[0], [])
    self.nodes[edge[1]] = self.nodes.get(edge[1], [])

    # Añadir los nodos adyacentes
    self.nodes[edge[0]].append(edge[1])
    self.nodes[edge[1]].append(edge[0])
    

  def get_nodes(self) -> Dict[int, List[int]]:
    """Regresa el diccionario de nodos

    Returns: 
      Dict[int, List[int]]
    """
    return self.nodes

  
  def get_edges(self) -> List[Tuple[int, int]]:
    """Regresa el conjunto de artistas como una lista de tuplas

    Returns: 
      List[Tuple[int, int]]
    """
    return self.edges
  
  def remove_node(self, node: int) -> None:
    """Dado un nodo, eliminar ese nodo de la lista de nodos y todas las aristas que lo contienen

    Args: 
      node (int)
    """  
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

  
  def remove_edge(self, edge: Tuple[int]) -> None:
    """Elimina una arista del conjunto de aristas

    Args: 
      edge (Tuple[int]): arista a eliminar
    """
    
    # eliminar de la lista de nodos
    self.edges.remove(edge)

    self.nodes.get(edge[0], []).remove(edge[1])
    self.nodes.get(edge[1], []).remove(edge[0])

    
  def node_len(self) -> int:
    return len(self.nodes)

  
  def edges_len(self) -> int:
    return len(self.edges)
