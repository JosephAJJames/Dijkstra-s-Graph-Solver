import random

class GenerateGraph:
    
    def __init__(self):
        self.dict = {}
        self.nodes = []
        pass

    def clearDict(self):
        self.dict = {}
        pass

    def generateNodes(self):
        self.nodes.append("A") #ensure A (which is the start point) is always in the graph
        nodeChoices= ["B", "C", "D", "E", "F", "G", "H", "I"]
        indiciesUsed = [] #list of indicies used to avoid repeated nodes
        num = random.randint(0, len(indiciesUsed) - 1)
        if num in indiciesUsed:
            while (num in indiciesUsed):
                num = random.randint(0, len(indiciesUsed) - 1)
    
        newNode = nodeChoices[num]
        self.nodes.append(newNode)
        pass

    def createWeightings(self):
        pass