

class SchoolMember:

    curr_year = 2021
    
    def printName(self):
        return self.getName()

    def calcYearBorn(self):
        return self.curr_year - self.getAge()

class Teacher(SchoolMember):
    def __init__(self, name, age ):
        self.name  = name
        self.age = age

    def getAge(self):
        return self.age
    def getName(self):
        return self.name

frank = Teacher("Frank", 32)


print(frank.printName(), frank.calcYearBorn())