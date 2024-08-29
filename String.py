course= "Python for Beginners"
print(course.upper())   #UPPER le original string ma change gardaina infact it create new one
print(course.lower())


print(course.find('o')) #index dinxa & if duita o xa bhane agadi ko o ko index dinxa
print(course.find('Python'))


print(course.replace('for', '4'))


print('Python' in course)
for x in "banana":
    print(x)

#slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])


#split
a = "Hello, World!"
print(a.split("*")) # returns ['Hello', ' World!']


#concatination 1
a = "Hello"
b = "World"
c = a + b
print(c)

#Concatination 2
a = "Hello"
b = "World"
c = a + " " + b
print(c)


#Format strings
age = 36
txt = "My name is John, I am " + str(age)
print(txt)

#        OR
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Modifier in {}
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)