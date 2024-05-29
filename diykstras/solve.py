from generate import GenerateGraph


class Solve:
    
    def __init__(self):
        self.graph = GenerateGraph()
        self.graph.generateGraph()

    def printGraph(self):
        self.graph.printDict()


solver = Solve()
solver.printGraph()