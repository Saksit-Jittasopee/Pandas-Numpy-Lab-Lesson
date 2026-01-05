# YOUR CODE HERE
n = int(input())
while n<=1 or n%2==0:
    n = int(input())
    continue
if n>1 and n%2!=0:
    for i in range(n):
        stars = '*'
        for j in range(n-1):
            if i==j or i+j==n-1 or j==0:
                print('*', end=' ')
            else:
                print('-', end=' ')
        print(stars)