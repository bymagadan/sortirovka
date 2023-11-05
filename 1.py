import random

num = 10
a = []
for i in range(num):
    a.append(random.randint(1, 20))

print(a)

for i in range(num - 1):
    for j in range(num - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
