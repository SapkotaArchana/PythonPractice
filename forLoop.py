fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

  # BREAK
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)    # apple banana print hunxa
    if x == "banana":
        break
    print(x)        # break comes before the print yesle apple matrai print garxa


# CONTINUE Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# range() function
for x in range(6):
    print(x)
for x in range(2, 6):
  print(x)
for x in range(2, 30, 3): # 2 bata suru hunxa to 20 and increment by 3
  print(x)

print("****************************")


# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished")
# this will print from 0 to 5 and then also of else block

# Not to print the else block we need to use break
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# Nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


# pass
for x in [0, 1, 2]:
  pass