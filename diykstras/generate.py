import random

class GenerateGraph:
    
    def __init__(self):
        self.dict = {}
        self.nodes = []
        self.graphSize = None
        pass

    def clearDict(self):
        self.dict = {}
        pass

    def generateNodes(self):
        graphSize = random.randint(5, 8) #determines the size of graph
        iteration = 0
        while (iteration <= graphSize):
            self.nodes.append("A") #ensure A (which is the start point) is always in the graph
            nodeChoices= ["B", "C", "D", "E", "F", "G", "H", "I"]
            indiciesUsed = [] #list of indicies used to avoid repeated nodes
            num = self.generateUnique(indiciesUsed, len(nodeChoices) - 1)
            newNode = nodeChoices[num]
            self.nodes.append(newNode)
            iteration =+ iteration
        pass

    def generateUnique(self, numList, length):
        num = random.randint(0, length)
        while (num in numList):
            num = random.randint(0, length)
            
        return num
        pass

    def createWeightings(self):
        pass