temperature= 25

if(temperature >30):
    print("It's a hot day")
elif temperature >20: #(20,30)
    print("It's a nice day")
elif temperature > 10: #(10,20)
    print("It's a bit cold day")
else:
    print("It's a cold day")
print("Done")

#   ELIF

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#   OR
a = 2
b = 330
print("A is greater.") if a > b else print("B is greater.")

# with 3 conditions
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# AND condition in if statement
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# NOT keyword
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# NESTED if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# if statements cannot be empty, but if you for some reason have an
# if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass