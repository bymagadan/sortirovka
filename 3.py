import random
import time
f = open('out.txt', 'w')
def gen(size):
    a = []
    for i in range(size):
        a.append(random.randint(0, 9))
    a.append(10)
    return a

def find(cv, qw):
    i = 0
    while i < len(cv):
        if cv[i] == qw:
            return i
        i += 1
    return -1

size = 1000000
iter = 100
a = gen(size)

start = time.time()

for i in range(iter):
    a.index(10)
def test(iter, size):
    start = time.time()
  
end = (time.time() - start) / iter

print(f'в начале: {end}')   


a[size // 2] = 11
start = time.time()
for i in range(iter):
    a.index(11)
end = (time.time() - start) / iter
print(f'в середине: {end}')

a[-1] = 12
start = time.time()
for i in range(iter):
    a.index(12)
end = (time.time() - start) / iter
print(f'в конце: {end}')
