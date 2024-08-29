class Person:
    name="Archana"
    occupation= "Student"
    networth= 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()
c=Person()
print(a.name)
a.name="Amrita"
a.occupation= "Intern"
# print(a.name, a.occupation)

b.name="Ashbin"
b.occupation="+2"

a.info()
b.info()
c.info() # yesma chai default value aayera basyo kina bhane mathi hamile c.name c.occupation gareko xaina
