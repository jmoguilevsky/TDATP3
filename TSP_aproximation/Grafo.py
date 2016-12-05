# -*- coding: utf-8 -*-

class Digraph(object):
  """Grafo no dirigido con un número fijo de vértices.

  Los vértices son siempre números enteros no negativos. El primer vértice
  es 0.

  El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
  creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
  nuevas aristas.
  """
  def __init__(g, V):
    """Construye un grafo sin aristas de V vértices.
    """
    g.edges = {}
    g.vertices = V
    for v in xrange(V):
    	g.edges[v] = []

  def V(g):
    """Número de vértices en el grafo.
    """
    return g.vertices

  def E(g):
    """Número de aristas en el grafo.
    """
    return sum([len(g.edges[e]) for e in g.edges])

  def adj_e(g, v):
    """Itera sobre los aristas incidentes _desde_ v.
    """
    return iter(g.edges[v])

  def adj(g, v):
    """Itera sobre los vértices adyacentes a ‘v’.
    """
    return iter([e.destiny for e in g.edges[v]])

  def add_edge(g, u, v, weight=0):
    """Añade una arista al grafo.
    """
    g.edges[u].append(Edge(u,v,weight))
    g.edges[v].append(Edge(v,u,weight))


  def __iter__(g):
    """Itera de 0 a V."""
    return iter(xrange(g.V()))

  def iter_edges(g):
    """Itera sobre todas las aristas del grafo.

    Las aristas devueltas tienen los siguientes atributos de solo lectura:

        • e.src
        • e.dst
        • e.weight
    """
    return iter([x for e in g.edges for x in g.edges[e	]])



  def MST_kruskal(g):
    A = []
    """inicializo cada vertice como un set"""
    s = g.kruskal_initial_sets()

    sorted_edges = g.sort_nondecreasing(g.iter_edges())
    for edge in sorted_edges:
        u = edge.destiny
        v = edge.source
        """ si no pertenecen al mismo arbol agrego la arista y uno los sets"""
        if g.find_set(v,s) != g.find_set(u,s):
            A.append(edge)
            g.union(u,v,s)
    """ Devuelvo un grafo aciclico (arbol) con las aristas de peso minimo obtenidas """
    result = Digraph(g.V())
    for edge in A:
        result.add_edge(edge.source,edge.destiny,edge.weight)
    return result

  def kruskal_initial_sets(g):
    """
        Crea un set (arbol) por cada vertice del grafo.
    """
    sets= []
    for v in g.__iter__():
        s = set()
        s.add(v)
        sets.append(s)
    return sets

  def find_set(g, vertex, sets):
    """ Devuelve el indice del arbol al cual pertenece el vertice dado"""
    for set in sets:
        if vertex in set:
            return sets.index(set)
    return null

  def union(g, u, v, sets):
    """ Une los arboles pertenecientes a los dos vertices "u" y "v" dados """
    for set in sets:
        if v in set:
            v_set = set
    for set in sets:
        if u in set:
            u_index= sets.index(set)
    for vertex in v_set:
        sets[u_index].add(vertex)
    sets.remove(v_set)

  def sort_nondecreasing(g, v_edges_iter):
    """ Devuelve a partir de un iterador de aristas, estas ultimas en una lista
    """
    result = []
    for edge in v_edges_iter:
        result.append(edge)
    if len(result) > 0:
        result = sorted(result, key=edge_key)
        return result
    return null

def edge_key(edge):
    return edge.weight




class Edge(object):
	"""Arista de un grafo.
	"""
  	def __init__(self, src, dst, weight):
		self.source = src
		self.destiny = dst
		self.weight = weight

	def __eq__(self, other):
		if (not isinstance(other, self.__class__) ) or other == None:
			return False
		return (self.source == other.source) and (self.destiny == other.destiny) and (self.weight == other.weight)

	def __cmp__(self, other):
		if other == None: return -1
		return (self.source == other.source) and (self.destiny == other.destiny) and (self.weight == other.weight)

	def __str__(self):
		return "origin: " + str(self.source) + ", destiny: " + str(self.destiny) + ", weight: " + str(self.weight)
