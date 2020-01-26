# Ques 1
print(sum([i for i in range(12)]))

# Ques 2
l = [1, 2, 65, 846, 668, 765468, 779]
print([i for i in l if i % 2 == 0])

# Ques 3
m = {1, 32, 654, 7}
mm = m.copy()
m1 = {mm.remove(a) for a in m if a % 2 == 0}
print(mm)

# Ques 4
dd = {1: 2, 2: 3, 3: 4}
r = 1
for k in dd:
    r *= dd[k]
print(r)