# try:
#     l=[1,2,3,4]
#     i=int(input("Enter the index:"))
#     print(l[i])
# except Exception as e:
#     print(e)
# finally:
#     print("This is always executed")
# print("Some important lines of code")



def func():
    try:
        l=[1,2,3,4]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("This is always executed")
x= func()
print(x)