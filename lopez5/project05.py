class Student:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = str(age)

    def display(self):
        print(f'''
Student
Name = {self.name}
Age = {self.age}''')

class Doctor(Student):
    def __init__(self, name, age, hopsital):
        super().__init__(name, age)
        self.hospital = str(hopsital)

    def display(self):
        print(f'''
Doctor
Name = {self.name}
Age = {self.age}
Hospital = {self.hospital}''')

class Engineer(Student):
    def __init__(self, name, age, courses):
        super().__init__(name, age)
        self.courses = str(courses)

    def display(self):
        print(f'''
Engineer        
Name = {self.name}
Age = {self.age}
Courses = {self.courses}''')

s1 = Student("Leandro", 30)
m1 = Doctor("Ithiel", 55, "Day Kimball Healthcare")
e1 = Engineer("Marcelo", 49, "Network Engineering")
s1.display()
m1.display()
e1.display()