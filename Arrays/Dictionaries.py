"""
used to store data values in key:value pairs.
is a collection which is ordered*, changeable and do not allow duplicates.

"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# accessing item using get()
x = thisdict.get("model")
print(x)    # prints dict_keys(['brand', 'model', 'year'])

# Getting keys
x=thisdict.keys()
print(x)    # prints dict_values(['Ford', 'Mustang', 2020])

# getting list of values
x = thisdict.values()
print(x)

# items() method returns each item in  in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)   # prints dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

# Data types(String, int, boolean, and list data types:)
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# output print garya xaina just input kasari dine bhanera hereko ho

# Adding new key and value
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}


# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Update dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#   OR
thisdict.update({"color": "red"})
print(thisdict)
#      OR
thisdict["gear"] = "one"
print(thisdict)


# Removing items using pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item
thisdict.popitem()

# The del keyword removes the item with the specified key name:
del thisdict["model"]
# The del keyword can also delete the dictionary completely:
del thisdict
# clear() empties the dictionary
thisdict.clear()


# converting dictionaries to data frame nested ko case ma
# import pandas as pd
# df.pd.DataFrame(emp_details['Employee'])
# print(df)
