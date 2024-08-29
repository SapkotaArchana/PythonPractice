"""
used to store multiple items in a single variable.
List items are ordered(the items have a defined order, and that order will not change),
changeable(we can change, add, and remove items in a list),
and allow duplicate values.
List items are indexed
"""
thislist = ["apple", "banana", "apple", "cherry"]
print(thislist)
print(thislist[3])


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-2])             # negative indexing
print(thislist[2:5])            # ranges of items print 3rd, 4th, and 5th
print(thislist[:4])             # agadi ko 4 ota print hunxa
print(thislist[2:])             # agadi ko duita xodera aru print hunxa
print(thislist[-4:-1])          # oragne dekhi mango samma tara mango include hudaina so orange, kiwi, melon
#  if item exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#  changing the item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#  banana ra cherry ma blackcurrant ra watermelon aauxa
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# this replace banana and cherry by watermelon
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert items at specified index
# index 2 paxi watermelon basxa
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# append() method- to add an item to the end of the list
list=["Archana", "Amrit", "Ashmin"]
list.append("Saranya")
print(list)

# extend- To append elements from another list to the current list
list1=["apple","banana","mango"]
list2=["Archana", "Amrit","Ashmin"]
list1.extend(list2)
print(list1)
# print(list2) garyo bhane Archana amrit ashmin matrai print hunxa kinaki mathi list1 extend list2 gareko xa
# list2 extend list1 garnu xa bhane print pani list 2 garda archana amrit ashmin apple banana mango print hunxa


# extend use tuple list dictionaries jun sanga ni garna milxa
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
 # output- apple banana cherry kiwi orange in list ma print garxa


 # Removing list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#  output- apple cherry
# if banana double xa bhane 1st ko banana matrai remove garxa arko banana print hunxa


# specified index remove garna pop() use garne
thislist.pop(0)
print(thislist)
# apple hatxa ra cherry matrai print hunxa kinaki banana agi hatiskayo
# pop ma number halena bhane last ko list hatxa

# del keyword- this also remove specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# index halena bhane completely remove garxa
# del thislist garda purai hatxa ani yo lekhda print(thislist) lekhna pardaina lekhyo bhane kaam gardaina

# clear() method- purai content hatauxa
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# output=[] empty list


# For Loop in list
list=["Archana","Ashmin", "Amrit"]
for x in list:
    print(x)

#  Using range() and len() functions
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
# mathi ko jastai output aauxa aauna chai


# While Loop
thislist = ["apple", "banana", "cherry", "mango"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]
print(newlist)


# We can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# Sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort in descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
