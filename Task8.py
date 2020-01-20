# Ques1

n = int(input("Enter a number:"))

for i in range(11):
    try:
        b = n/i
    except ZeroDivisionError:
        print("Can not divide by zero")
    else:
        print(b)

"""------------------------------------------------------------------------------------------------------------------------"""

# Ques2

u = input("Enter numbers with space").split()
u = [int(i) for i in u]
for v in range(len(u)+1):
    try:
        print(u[v])
    except IndexError:
        print("Index out of range")

"""-------------------------------------------------------------------------------------------------------------------------"""

# Ques 3
r = input("Enter three resistance with space:").split()

r = list(map(int, r))


def series_sum(r):
    tt = 0
    for l in r:
        tt += l
    print(tt)

def parallel_sum(r):
    tt = 0
    for l in r:
        tt += 1/l
    print(1/tt)



series_sum(r)
parallel_sum(r)