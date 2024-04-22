import random

class GenerateGraph:
    
    def __init__(self):
        self.dict = {}
        self.nodes = []
        self.graphSizeMax = 8
        pass

    def clearDict(self):
        self.dict = {}
        self.nodes = []
        pass

    def printNodes(self):
        print(self.nodes)
        pass

    def generateNodes(self):
        graphSize = random.randint(5, self.graphSizeMax) #determines the size of graph(between 5 to 8)
        iteration = 0
        self.nodes.append("A") #ensure A (which is the start point) is always in the graph
        indiciesUsed = [] #list of indicies used to avoid repeated nodes
        while (iteration <= graphSize):
            nodeChoices= ["B", "C", "D", "E", "F", "G", "H", "I"]
            num, numList = self.generateUnique(indiciesUsed, len(nodeChoices) - 1)
            indiciesUsed = numList
            newNode = nodeChoices[num]
            self.nodes.append(newNode)
            iteration = iteration + 1
        pass

    def generateUnique(self, numList, length):
        num = random.randint(0, length)
        if num in numList:
            while (num in numList):
                num = random.randint(0, length)
                #print("stuck in small loop")
        numList.append(num)
        return num, numList
        pass

    def createConnections(self):

        pass
    
    def createWeightings(self):
        pass

graphGenerator = GenerateGraph()
for x in range(0, 4):
    graphGenerator.generateNodes()
    graphGenerator.printNodes()
    graphGenerator.clearDict()