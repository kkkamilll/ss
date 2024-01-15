k = int(input())

A = [0, 0]
for i in range(k-1):
    A = [A, A]

print(A)