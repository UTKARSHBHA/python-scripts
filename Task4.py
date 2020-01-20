# Ques.1
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        continue
print()
"""------------------------------------------------------------------------------------------------------"""

# Ques.2

def add(*args):
    tt = 0
    for i in args:
        tt += i
    return tt
print(f"The sum is {add(5, 4, 55, 56)}")

"""------------------------------------------------------------------------------------------------"""

# Ques.3
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

list = [a, b, c]
list.sort()

print(f"the median of the three values is {list[1]}")

