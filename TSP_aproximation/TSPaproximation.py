from Grafo import edge_key

def TSP_tour_aproximation(g,initial_vertex):
    MST = g.MST_kruskal()
    vertices = []
    inexistent_parent = -1
    vertices = preorder(MST,initial_vertex,vertices,inexistent_parent)
    vertices.append(initial_vertex)
    return vertices


def preorder(g,initial_vertex,vertices,parent_vertex):
    current_vertex = initial_vertex;
    vertices.append(current_vertex)
    edges = []

    """ Obtengo las aristas de los hijos del vertice actual"""
    for edge in g.adj_e(current_vertex):
        if edge.source != parent_vertex and edge.destiny != parent_vertex:
            edges.append(edge)

    """ Las ordeno de menor a mayor peso"""
    edges = sorted(edges, key=edge_key)

    """ voy agregando vertices en profundidad recursivamente empezando por los
    de menor peso """
    for e in edges:
        if e.source != current_vertex and e.source not in vertices:
            vertices = preorder(g,e.source,vertices,current_vertex)
        elif e.destiny != current_vertex and e.destiny not in vertices:
            vertices = preorder(g,e.destiny,vertices,current_vertex)

    return vertices
