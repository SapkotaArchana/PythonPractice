class Dog:
    # attribute
    attri= "mammal"

    # Instance attribute / constructor
    def __init__(self, name):
        self.name= name

    # methods banako
    def speak(self):
        print("My name is {}". format(self.name))

# object instantiation
Rodger= Dog("Rodger")
Tommy= Dog("Tommy")

# accessing class methods
Rodger.speak()
Tommy.speak()






