# YOUR CODE HERE
x = []
m = int(input()) #row
n = int(input()) #column

for i in range(m): #row
    y = []
    for j in range(n): #column
        matrix = int(input()) #input matrix
        y.append(matrix)
    x.append(y)
print(x)

zero_check = []*n #check if column have 0
count_zero = 0
for i in range(n):
    for j in range(m):
        if x[j][i] == 0:
            count_zero += 1
    print(count_zero,end=' ')
    count_zero = 0