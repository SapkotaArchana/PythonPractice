
# readline()- read one line
# f = open('readfile.txt', 'r')
# print(f.read(5))      # return 5 character of files
f = open("D:\\readfile.txt", "r")
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line, type(line))
        break
f.close()


f = open("D:\\readfile.txt", "r")
print(f.readline())
print(f.readline())
f.close()


f = open("readfile.txt", "r")
for x in f:
  print(x)



#writelines()