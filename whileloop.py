"""
increment dina parxa otherwise infinite chalxa
"""

i = 1
while i < 6:
  print(i)
  i += 1

print("*********************")


# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


print("*********************")


# CONTINUE statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


print("*************************")


# ELSE statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")