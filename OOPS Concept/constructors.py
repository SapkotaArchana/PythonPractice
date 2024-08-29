class Person:

    def __init__(self, name, occupation):
        print("This is constructor")
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Archana","Sdet")
b = Person("Amrit", "graduated student")

a.info()
b.info()