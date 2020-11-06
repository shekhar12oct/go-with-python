class dequeOperation(object):

    def __init__(self):
        self.items = []

    def sizeof(self):
        return len(self.items)

    def addFront(self,eleF):
        self.items.append(eleF)

    def addRear(self,eleB):
        self.items.insert(0,eleB)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []