# YOUR CODE HERE
x = int(input())
y = int(input())
count = 0
if y > 0:
    while count != y:
        count += 1
        ans = x*count
        print(x, end= '*')
        print(str(count)+'='+str(ans))
else:
    print('Unable to create a table')

