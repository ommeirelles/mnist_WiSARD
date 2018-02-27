class Node():
    def __init__ (self, positions):
        self.table = []
        self.positions = positions
        max = len("{0:b}".format(2**len(positions))) - 1
        for i in range(2**len(positions)):
            x = (('0' * max) + "{0:b}".format(i))
            x = x[len(x)-max:]
            self.table.append({x: 0})

    def inputTraining(self, img):
        pattern = ''.join(str(k) for k in [1 if img[i-1] > 0 else 0 for i in self.positions])
        index, item = [(index, k.keys()[0]) for index,k in enumerate(self.table) if k.keys()[0] == pattern][0]
        self.table[index][item] = 1

    def patternSearch(self, img):
        pattern = ''.join(str(k) for k in [1 if img[i-1] > 0 else 0 for i in self.positions])
        return 1 if len([i for i in self.table if i.keys()[0] == pattern and i[i.keys()[0]] == 1]) > 0 else 0