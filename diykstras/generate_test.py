import unittest
from generate import GenerateGraph
from typing import List, Tuple

class Test(unittest.TestCase):

    def testCreateConnections(self):
        graphGen = GenerateGraph()
        graphGen.nodes = ["A", "B", "C"]
        self.assertEqual(graphGen.createConnections(), set((("A", "B"),  ("A", "C"),  ("B", "C"), ("B", "A"), ("C", "A"), ("C", "B"))))


    

if __name__ == '__main__':
    unittest.main()