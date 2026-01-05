# YOUR CODE HERE
x = int(input())
n1 = 0
n2 = 1
number = n1
count = 0

while count < x:
    count += 1
    print(number, end=' ')
    if count%5==0:
        print()
    n1, n2 = n2, number
    number = n1 + n2