
class UndirectedGraph(object):
    """ Class representing Graph Data Structure"""

    def __init__(self, graph_data={}):
        self.__graph_data = graph_data

    def vertices(self):
        return list(self.__graph_data.keys())

    def edges(self):
        return self.__get_edges()

    def graph(self):
        return self.__graph_data

    def __get_edges(self):
        edges = list()
        vertices = self.vertices()
        for vertex in vertices:
            for nearby_vertex in self.graph()[vertex]:
                if {vertex: nearby_vertex} not in edges:
                    edges.append({vertex: nearby_vertex})
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.vertices():
            return self.graph().update({vertex: list()})

    def add_edge(self, edge):
        if edge not in self.edges():
            return self.graph().update(edge)
