"""
mini function haru banauna sajilo hunxa, argument ddherai linxa tara return euta matrai garnu parxa
ek line mai kaam garaune bela ma use hunxa
function lai function ma pass garna pani milxa
"""

# def double(x):
#     return x*2

double = lambda x: x*2
cube = lambda x: x*x*x

print(double(5))
print(cube(5))
print("***********************************")
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
print("*************************************")

def appl(fx, value):
    return 6 + fx(value)
print(appl(cube, 2))
# or
print(appl(lambda x: x*x, 2))
