"""
A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
Private attributes start with "__".
"""

# Python program to
# demonstrate private members
# "__" double underscore represents private attribute.
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# print(obj1.c) will raise an AttributeError i.e 'Base' object has no attribute 'c'
# obj2 = Derived()  will also raise an AtrributeError as private member of
# base class is called inside derived class i.e 'Derived' object has no attribute '_Derived__c'
