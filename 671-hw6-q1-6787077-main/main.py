# YOUR CODE HERE
count = 0
n = int(input())
while n <=1 or n >=1000 :
    n = int(input())

while True:
    for i in range(2,n+1):
        if i == 2 or i == 3 or i == 5 or i ==7 or i==11 or i==13 or i==17 or i==19 or i==23 or i==29 or i==31:
            print(i, end=' ')
            count += 1
        elif i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0 or i%13==0 or i%17==0 or i%19==0 or i%23==0 or i%29==0 or i%31==0:
            continue
        else:
            print(i, end=' ')
            count += 1
        if n == i :
            break
    print()
    print('Total prime numbers:',count)
    break