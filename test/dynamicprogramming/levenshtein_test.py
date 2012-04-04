import unittest
import dynamicprogramming.levenshtein

class LevenshteinTestCase(unittest.TestCase):

    def setUp(self):
        self.leven = dynamicprogramming.levenshtein

    def tearDown(self):
        self.leven = None

    def test_equal_word(self):
        self.assertEqual(self.leven.distance('abc','abc'), 0)

    def test_equal_object(self):
        s = 'abc'
        self.assertEqual(self.leven.distance(s,s), 0)

    def test_empty_string(self):
        self.assertEqual(self.leven.distance('',''), 0)

    def test_distance_of_replace(self):
        self.assertEqual(self.leven.distance('abc','def'), 3)

    def test_distance_of_delete(self):
        self.assertEqual(self.leven.distance('hello','helo'), 1)

    def test_distance_of_insertion(self):
        self.assertEqual(self.leven.distance('helo','hello'), 1)

    def test_distance_of_insert_delete_replace(self):
        self.assertEqual(self.leven.distance('abchellohelo','defhelohello'), 5)

    def test_distance_with_space(self):
        self.assertEqual(self.leven.distance('abc hello helo','def helo hello'), 5)

