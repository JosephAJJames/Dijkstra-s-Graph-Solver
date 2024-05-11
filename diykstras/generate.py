import random



#https://csacademy.com/app/graph_editor/ graph editor


class GenerateGraph:
    
    def __init__(self):
        self.dict = {}
        self.nodes = []
        self.graphSizeMax = 8
        self.graphSize = 0
        pass

    def clearDict(self) -> None:
        self.dict = {}
        self.nodes = []
        pass

    def printDict(self) -> None:
        for x in self.dict:
            
            print(x + " :{}".format(self.dict.get(x)))

    def printNodes(self) -> None:
        print(self.nodes)
        pass


    def generateNodes(self) -> None:
        graphSize = random.randint(5, self.graphSizeMax) #determines the size of graph(between 5 to 8)
        self.graphSize = graphSize
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

    def insertNodesIntoDict(self) -> None:
        for x in self.nodes:
            self.dict[x] = None
        pass

    def generateUnique(self, numList: list[int], length: int) -> (int, list[int]):
        allNums = set(range(length + 1))
        usedNums = set(numList)
        unusedList = list(allNums - usedNums) #generate set of unused numbers

        if len(unusedList) == 0: #if there are no unused numbers
            return None, numList

        num = random.choice(unusedList) #pick a random number from the unused list

        numList.append(num)
        return num, numList
        pass

    def generateOpositeConnections(self, curCons: list[tuple((str, str))]) -> list[tuple((str, str))]:
        for x in range(0, len(curCons)):
            originalTuple = curCons[x]
            first = originalTuple[0]
            second = originalTuple[1]
            mirroredTuple = tuple((second, first))
            curCons.append(mirroredTuple)
        return curCons

    def allPossibleConnections(self) -> set():
        allCons = set()
        nodesConsiderd = []
        for x in range(0, len(self.nodes)):
            for y in range(0, len(self.nodes)):
                if x != y:
                    myTuple = tuple((self.nodes[x], self.nodes[y]))
                    allCons.add(myTuple)
        return allCons

    def createConnections(self) -> list[tuple((str, str))]:
        allCons = self.allPossibleConnections()
        curCons = []
        print(self.nodes)
        for x in range(0, self.graphSize + 5):
            element = random.choice(list(allCons))
            curCons.append(element)
            allCons = set(allCons - {element})
        curCons = self.generateOpositeConnections(curCons)
        #print("########\n" , curCons)
        return curCons
    
    def addConnections(self, cons:list[tuple((str, str))]) -> None:
        for x in self.dict:
            if self.dict[x] is None or self.dict[x] == "None":
                self.dict[x] = set()

        print("working")
        for x in cons:
            self.dict[x[0]].add(x[1])
            print("added to set")

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
for x in range(0, 1):
    graphGenerator.generateNodes()
    graphGenerator.printNodes()
    graphGenerator.insertNodesIntoDict()
    print(graphGenerator.dict)
    cons = graphGenerator.createConnections()
    print("########\n", cons)
    graphGenerator.addConnections(cons)
    graphGenerator.printDict()
    graphGenerator.clearDict()