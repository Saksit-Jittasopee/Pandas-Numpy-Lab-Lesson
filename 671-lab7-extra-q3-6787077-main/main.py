# YOUR CODE HERE
n = int(input())

A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

B = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += A[i][k] * B[k][j]

print(A)
print(B)
print(result)
