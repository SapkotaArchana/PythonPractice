"""
modes of file opening: read, write, append, create
"""

# Reading a file
# f = open("readfile.txt", "r")
# # print(f)
# txt = f.read()
# print(txt)
# f.close()


# writing a file
f = open("myfile.txt","w")
f.write("Hello World!!")
f.close()

# appending file
# f = open("myfile.txt","a")
# f.write("Hello World!!")
# f.close()

# with statement automatically closes file
with open("myfile.txt","a") as f:
    f.write("This is with statement")

