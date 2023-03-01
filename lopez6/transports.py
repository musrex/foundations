# This object is a deque. Short for "double-ended queue,"
# it is a queue that can accept input from either side
class Terminal():
    
    def __init__(self):
        self.items = []
        

    # This method adds transports from the east
    # or, adds elements to the deque from the right
    def east(self, thing):
        return self.items.append(thing)
    
    # This method adds transports from the west
    # or, adds elements to the deque from the left
    def west(self, thing):
        return self.items.insert(0,thing)

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)
