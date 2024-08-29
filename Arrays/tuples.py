"""
A tuple is a collection which is ordered and unchangeable.
Tuple items are ordered, unchangeable, and allow duplicate values.
index hunxa
allow duplicate values

"""


thistuple = ("apple", "banana", "cherry")
print(thistuple)

# duplicate items
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# data types
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# changing tuple value
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# tuple immutable hunxa so append use garna mildaina pahila list ma convert garne ani append() use garne\
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#     OR
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)


# Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Assigning as a list using *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#      OR

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# while Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# To join tuples add and multiply
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)   # ('a', 'b', 'c', 1, 2, 3)

tuple3=tuple1*2
print(tuple3)   # ('a', 'b', 'c', 'a', 'b', 'c')


# Tuple Methods
# 1) count() -> Returns the number of times a specified value occurs in a tuple
# 2) index() -> Searches the tuple for a specified value and returns the position of where it was found