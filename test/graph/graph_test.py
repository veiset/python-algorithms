import unittest
import graph.graph as graph

class CreateGraphTestCase(unittest.TestCase):

    def test_empty_directed_graph(self):
        g = graph.Directed()
        self.assertIsNotNone(g)

    def test_empty_undirected_graph(self):
        g = graph.Undirected()
        self.assertIsNotNone(g)

    def test_graph_name_undirected(self):
        g = graph.Undirected('Name of Graph')
        self.assertEqual('Name of Graph', g.name)

    def test_graph_name_directed(self):
        g = graph.Directed('Name of Graph')
        self.assertEqual('Name of Graph', g.name)


class DirectedGraphTestCase(unittest.TestCase):

    def setUp(self):
        self.g = graph.Directed('Test')

    def tearDown(self):
        self.g = None
    
    def test_add_vertex_with_string_name(self):
        v = graph.Vertex('A')
        self.g.addVertex(v)

    def test_add_vertex_with_int_name(self):
        v = graph.Vertex(1)
        self.g.addVertex(v)

    def test_get_vertex_string(self):
        v = graph.Vertex('A')
        self.g.addVertex(v)
        self.assertEqual(self.g.v('A'),v)

    def test_get_vertex_int(self):
        v = graph.Vertex(1)
        self.g.addVertex(v)
        self.assertEqual(self.g.v(1),v)

    def test_edge_between_two_vertices(self):
        v1 = graph.Vertex('A')
        v2 = graph.Vertex('B')
        self.g.addVertex(v1)
        self.g.addVertex(v2)
        self.g.addEdge(v1, v2)
        self.assertEqual(len(self.g.edges()),1)

    def test_reverse_of_graph(self):
        v1 = graph.Vertex('A')
        v2 = graph.Vertex('B')
        self.g.addVertex(v1)
        self.g.addVertex(v2)
        self.g.addEdge(v1, v2)

        gr = self.g.reverse()
        self.assertEqual(len(gr.v('A').edges),0)
        self.assertEqual(len(gr.v('B').edges),1)

        self.assertEqual(len(gr.v('A').edges),len(self.g.v('B').edges))
        self.assertEqual(len(gr.v('B').edges),len(self.g.v('A').edges))


class UndirectedGraphTestCase(unittest.TestCase):

    def setUp(self):
        self.g = graph.Undirected('Test')

    def tearDown(self):
        self.g = None

    def test_edge_between_two_vertices(self):
        v1 = graph.Vertex('A')
        v2 = graph.Vertex('B')
        self.g.addVertex(v1)
        self.g.addVertex(v2)
        self.g.addEdge(v1, v2)

        # the length of g.edges() in an undirected graph
        # should be twice of the number of edges added,
        # as an edge is added in both directions. 
        self.assertEqual(len(self.g.edges()),2)



