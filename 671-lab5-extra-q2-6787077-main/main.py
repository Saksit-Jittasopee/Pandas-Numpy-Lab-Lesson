# YOUR CODE HERE
a = int(input())
b = int(input())
if a > b:
    a, b = b, a
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print(a)
