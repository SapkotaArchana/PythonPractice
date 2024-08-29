"""
Sets are used to store multiple items in a single variable.
Set items are unordered, unchangeable, and do not allow duplicate values.
index or key use garna mildaina
duplicates not allowed
set le eutai order ma print gardaina
"""

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)      # this will ignore repeated values


# The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}
print(set1)


# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))
print(thisset)


# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
   print(x)


# Add an item to a set, using the add() method:
# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
# thisset.remove("mango")  this will show error
print(thisset)

# we can use discard method to remove items and If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
# thisset.remove("mango")  this will not show error
print(thisset)


# thisset.pop()  {remove a ramdom item from set)
# thisset.clear() {empty set print garxa}
# del thisset  {delete set completely}


# Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)    # we can wse | operator also (set1 | set2) tara yo use garda chai set to set matrai join hunxa tara union() use garda set sanga list ra tuple pani union hunxa ra result set ma dinxa
print(set3)


# update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items.

# intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)   # we can use & also
print(set3)


# intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)    # we can use - operator also (set1-set2)
print(set3)

# Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


# symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)   # we can use ^ operator also( set1^set2)
print(set3)


# symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
# output: {"google", "microsoft", "banana", "cherry"}