from node import *
import random

class Discriminator():
    def __init__(self, nodes, inputSize, label):
        self.label = label
        self.nodes = []
        taken = []
        for i in range(nodes):
            positions = []
            for i in range(inputSize/nodes):
                n = random.randint(1, inputSize)
                if taken.count(n) == 0:
                    positions.append(n)
            self.nodes.append(Node(positions))

    def train(self, img):
        for i in self.nodes:
            i.inputTraining(img)

    def getNodesResponse(self, img):
        return sum([i.patternSearch(img) for i in self.nodes])
