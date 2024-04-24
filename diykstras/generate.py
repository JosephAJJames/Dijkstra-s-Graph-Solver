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
            if num == None:
                return None
            newNode = nodeChoices[num]
            self.nodes.append(newNode)
            iteration = iteration + 1
            print("stuck in big loop")
        pass

    def insertNodesIntoDict(self):
        for x in self.nodes:
            self.dict[x] = "None"
        pass

    def generateUnique(self, numList, length):
        allNums = set(range(length + 1))
        usedNums = set(numList)
        unusedList = list(allNums - usedNums) #generate set of unused numbers

        if len(unusedList) == 0: #if there are no unused numbers
            return None, numList

        num = random.choice(unusedList) #pick a random number from the unused list

        numList.append(num)
        return num, numList
        pass

    def allPossibleConnections(self):
        allCons = set()
        pass

    def createConnections(self):
        currentConnections = set()

        pass
    
    def createWeightings(self):
        pass

    def generateGraph(self):
        self.generateNodes()
        self.insertNodesIntoDict()
        self.allPossibleConnections()
        self.createConnections()
        self.createWeightings()
        return self.dict

graphGenerator = GenerateGraph()
for x in range(0, 4):
    graphGenerator.generateNodes()
    graphGenerator.printNodes()
    graphGenerator.insertNodesIntoDict()
    print(graphGenerator.dict)
    graphGenerator.clearDict()