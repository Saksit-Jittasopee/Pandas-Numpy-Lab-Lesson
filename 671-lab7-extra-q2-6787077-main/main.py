# YOUR CODE HERE
x = []
for i in range(10):
    num = int(input())
    x.append(num)
notzero = [num for num in x if num != 0]
zero = x.count(0)
result = notzero + [0] * zero
print(result)
