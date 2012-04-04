class Vertex():
    '''
    Vertex/Node
    '''

    def __init__(self, name, data=None):
        '''
        Vertex(string, object)

        Keyword arguments:
        name -- idenifying name of vertex
        data -- data object assoisated with the vertex/node
        '''

        self.name = name
        self.edges = []
        self.data = data

    def addEdge(self,v2,weight=None):
        '''
        addEdge(Vertex, integer)

        Adds a directed edge to the vertex

        Keyword arguments:
        v2     -- Vertex the current vertex should be connected to,
                  this is a directed edge. Going from v1 (this) to v2.
        weight -- Optional weight/distance of the edge.
        '''

        self.edges.append(Edge(self,v2,weight))


class Edge():
    '''
    Edge
    '''
    def __init__(self,v1,v2,weight=None):
        '''
        Edge(Vertex, Vertex, int) 

        Directed Edge

        Keyword arguments:
        v1     -- Start vertex 
        v2     -- End vertex
        weight -- Optional weight/distance of the edge
        '''

        self.v1 = v1
        self.v2 = v2
        self.weight = weight

class Graph():

    def __init__(self,name=None):
        '''
        Graph(string)

        Keyword arguments:
        name  -- Optional name of the graph
        '''

        self.vertices = {}

        if not name:
            self.name = 'Undefined'
        else:
            self.name = name

    def addVertex(self,vertex):
        '''
        addVertex(Vertex) 

        Adds a vertex to the graph

        Keyword arguments:
        vertex -- Vertex object
        '''

        self.vertices[vertex.name] = vertex

    def vertex(self,name):
        '''
        vertex(string)

        Finds a given vertex in the graph

        Keyword arguments:
        name   -- name of the vertex
        '''

        try:
            return self.vertices[name]
        except:
            return None

    def v(self,name):
        '''
        v(string)

        Uses vertex() to find a given vertex in the graph

        Keyword arguments:
        name   -- name of the vertex
        '''

        return self.vertex(name)

    def edges(self):
        '''
        edges()

        Return all the edges in the graph
        '''

        edges = []
        for v in self.vertices.values():
            for e in v.edges:
                edges.append(e)
        return edges

        return self.vertex(name)
    
    def addEdge(self,v1,v2,weight=None):
        '''
        addEdge(Vertex, Vertex, integer) 

        Adds a directed edge to a vertex 

        Keyword arguments:
        v1     -- Start vertex 
        v2     -- End vertex
        weight -- Optional weight/distance of the edge
        '''

        v1.addEdge(v2,weight)

    def copy(self,g):
        '''
        copy(Graph) -> Graph

        Return a copy of the given graph 'g'
        '''

        for vr in self.vertices.values():
            g.addVertex(Vertex(vr.name))

        for vertex in self.vertices.values():
            for e in vertex.edges:
                g.addEdge(g.v(e.v1.name),g.v(e.v2.name),e.weight)

        return g

    def printGraph(self):
        '''
        printGraph()

        Prints a simple textual representation of the graph
        '''

        for v in self.vertices.values():
            print v.name, [(v.v2.name, v.weight) for v in v.edges]


class Directed(Graph):

    def reverse(self):
        '''
        reverse() -> Graph

        Creates a new directed graph, and adds 
        all the edges in the reverted direction.

        Return reversed graph
        '''

        gr = Directed('Reversed')
        for vr in self.vertices.values():
            gr.addVertex(Vertex(vr.name))
              
        for vertex in self.vertices.values():
            for e in vertex.edges:
                gr.addEdge(gr.v(e.v2.name),gr.v(e.v1.name),e.weight)

        return gr

    def copy(self):
        '''
        copy() -> Graph

        Return a copy of the graph
        '''

        g = Directed()
        return Graph.copy(self,g)
    

class Undirected(Graph):

    def addEdge(self,v1,v2,weight=None):
        '''
        addEdge(Vertex, Vertex, integer) 

        Adds an undirected edge (an edge from
        v1 -> v2 AND an edge from v2 -> v1).

        '''
        v1.addEdge(v2,weight)
        v2.addEdge(v1,weight)
    
    def copy(self):
        '''
        copy() -> Graph

        Return a copy of the graph
        '''

        g = Undirected()
        return Graph.copy(self,g)
