class Researcher:
    def __init__(self,name,age,points):
        self.name = name
        self.age = int(age)
        self.points = float(points)
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getPoints(self):
        return self.points
    def getAverage(self):
        return self.points / self.age

def main():
    name = "Paulo"
    age = 22
    points = 11
    p = Researcher("Fernandes", age, 22)
    print(p.getName(), p.getPoints(), p.getAverage())
    

class English:
    def __init__(self):
        self.country = "UK"
    def greeting(self):
        print("Good Day")

class French:
    def __init__(self):
        self.country = "France"
    def greeting(self):
        print("Bonjour")

def salute(origin):
    origin.greeting()

def main():
    Shakespeare = English()
    Moliere = French()

    print("William says: ", end="")
    salute(Shakespeare)
    print("Jean-Baptiste says: ", end="")
    salute(Moliere)

main()
