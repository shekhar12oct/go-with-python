class stackOperation(object):

    # Initialising the stack with empty list
    def __init__(self):
        self.items = []

    def push(self,ele):
        self.items.append(ele)


    def pop(self):
        self.items.remove(len(self.items)-1)


    def sizeof(self):
        return len(self.items)

    def peak(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

