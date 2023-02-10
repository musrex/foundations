

class Dog:
    def __init__(self, name):
        self.name = name
        print(name)
        

    def sniff(self):
        return "sniff"

    def bark(self):
        print('bark')

d = Dog("Lean")
d.bark()
