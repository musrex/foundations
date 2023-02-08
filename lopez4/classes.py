class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print("I don't know what I say.")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Chicken(Pet):
    pass

p = Pet("Lean", 30)
p.speak()
c = Cat("Pappo", 16)
c.speak()
d = Dog("Fly", 3)
d.speak()
f = Chicken("Bubbles",1)
f.speak()