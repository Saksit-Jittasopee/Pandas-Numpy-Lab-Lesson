# YOUR CODE HERE
n = int(input())
if n > 0:
    for n in range(1,n+1):
        if n%15 == 0:
            print('Fizz Buzz', end=' ')
        elif n%3 == 0:
            print('Fizz', end=' ')
        elif n%5 == 0:
            print('Buzz', end=' ')
        else:
            print(n, end=' ') 
else:
    while n < 1:
        n = int(input()) 
        if n > 0:
            for n in range(1,n+1):
                if n%15 == 0:
                    print('Fizz Buzz', end=' ')
                elif n%3 == 0:
                    print('Fizz', end=' ')
                elif n%5 == 0:
                    print('Buzz', end=' ')
                else:
                    print(n, end=' ') 