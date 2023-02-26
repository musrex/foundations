class Terminal():
    
    def __init__(self):
        self.items = []

    # This method adds transports from the east
    # or, adds elements to the deque from the right
    def east(self, thing):
        self.items.append(thing)
    
    # This method adds transports from the west
    # or, adds elements to the deque from the left
    def west(self, thing):
        self.items.insert(0,thing)

    
    def size(self):
        return len(self.items)
    #def remove(self):
    #    return self.items.pop(0)

    #def __init__(self):
    #    self.items = []
    #def IsEmpty(self):
    #    return self.items == []
    #def enqueue(self,item):
    #    self.items.append(item)
    #
    #def front(self):
    #    return self.items[len(self.items)-1]
    #def size(self):
    #    return len(self.items)
    def display(self):
        print(self.items)