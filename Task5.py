# Ques 1

lis = "honey singh"
print(len(lis))

"""-------------------------------------------------------------------------------------------"""

# Ques 2

i = input("Enter words with space:")
l = i.split()

m = 0
for n in range(len(l)):
    if len(l[n]) > m:
        m = len(l[n])
print(m)

"""--------------------------------------------------------------------------------------------------------------"""

# Ques 3

lis2 = ["goku", "vagita", "gohan", "goten", "picolo"]

for i in range(0,len(lis2), 2):
    lis2[i] = "#"

print(lis2)

"""--------------------------------------------------------------------------------------------------------------"""

# Ques 4

lis3 = []
lis4 = ["freeza", "cell"]

def empty(u):
    if len(u) == 0:
        print("List is empty")
    else:
        print("List is not empty")

empty(lis3)
empty(lis4)

"""---------------------------------------------------------------------------------------------------------------"""

# Ques 5

lis5 = ["naruto", "sasuke"]

lis6 = lis5[:]

print(lis6)