# Ques.1
fseries = []
z = 0
while z <= 50:
    if len(fseries) < 1:
        fseries.append(0)
    elif fseries[-1] == 0:
        fseries.append(1)
    else:
        z = fseries[-1] + fseries[-2]
        if z <= 50:
            fseries.append(z)
print(fseries)


"""--------------------------------------------------------------------------------------"""

#Ques.2

#Let ABC be a triangle of side AB, BC, CA
a = int(input("enter the length of AB"))
b = int(input("enter the length of BC"))
c = int(input("enter the length of CA"))

if b == a == c:
    print("ABC is an equilateral triangle")

elif a != b != c:
    print("ABC is a scalene triangle")

else:
    print("ABC is an isosceles triangle")


"""--------------------------------------------------------------------------------------"""

#Ques.3
aa = int(input("Enter first number:"))
bb = int(input("Enter second number:"))

def gcp(aa, bb):
    p = 1
    for u in range(1, aa+1):
        if aa % u == 0 and bb % u == 0:
            p = u
        else:
            continue
    return p
print(gcp(aa, bb))

"""-------------------------------------------------------------------------------------------------------------"""

# Ques.4
s = 0
for y in range(0, 11, 2):
    s += y
print(f"sum off even numbers form 0 to 10 is '{s}'")