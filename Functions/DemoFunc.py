"""
block of code which only runs when it is called.
can pass data, known as parameters, into a function.
A function can return data as a result.
"""


def my_function():
    print("Hello this is a function!")
my_function()

# Passing arguments
def my_function(self):
  print(self + " Sapkota")
my_function("Archana")
my_function("Amrit")
my_function("Ashmin")

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# Arguments with *. If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print(kids)
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# key = value syntax in arguments
def my_function(child3, child2, child1):
  print("The middle child is " + child2)
my_function(child1 = "Amrit", child2 = "Archana", child3 = "Ashmin")


# **Kwargs
def my_function(**kid):
  print("Her last name is " + kid["lname"])
my_function(fname = "Archana", lname = "Sapkota")

# Passing a list as arguments
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

"""
-> Position only arguments
def my_function(x, /): 
  print(x)
my_function(3)
Hamile , / rakhera tala my_function(x=3) rakhyo bhane error aauxa
"""


"""
-> Keyword only arguments
def my_function(*,x): 
  print(x)
my_function(x=3)
Hamile *,/ rakhera tala my_function(3) rakhyo bhane error aauxa
"""