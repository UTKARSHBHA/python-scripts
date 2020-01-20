# Ques 1

l = [2 , 5 , 10]


def mul(l):
    tt = 1
    for a in l:
        tt *= a
    return tt

print(mul(l))

"""-----------------------------------------------------------------------------------------------------------------------------------------"""

# Ques 2

def z(u):
    if u in range(y+1):
        print(f"{u} is in range {y}")
    else:
        print(f"{u} is not in range {y}")

u = int(input("enter a number:"))
y = int(input("enter range from zero:"))

z(u)