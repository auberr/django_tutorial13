from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

    @staticmethod
    def isAdult(age):
        return age > 18
    

# person = Person('Adam', 19)
# person.display()

# person1 = Person.fromBirthYear('John', 1985)
# person1.display()

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

print(Person.isAdult(22))