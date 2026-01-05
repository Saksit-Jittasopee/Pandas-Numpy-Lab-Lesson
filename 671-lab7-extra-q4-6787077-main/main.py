# YOUR CODE HERE
A = []
for i in range(5):
    num = float(input())
    A.append(num)

x = float(input())

list = []
for num in A:
    if num > x:
        list.append('g')
    elif num < x:
        list.append('s')
    else:
        list.append('e')
print(list)
