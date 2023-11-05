import random


def gen():
    n = []
    for i in range(V):
        n.append(random.randint(1, 20))
    return n


def qwe(arr):
    for i in range(V-1):
        for j in range(V - i - 1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n [j+1], n[j]
def sel_sort(arr):
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range (i+1, n):
            if arr[j] < arr[m]:
                m = j
            arr[i], arr [m] = arr[m], arr[i]
V = 10
n = gen()
print(n)
sel_sort(n)
print(n)
