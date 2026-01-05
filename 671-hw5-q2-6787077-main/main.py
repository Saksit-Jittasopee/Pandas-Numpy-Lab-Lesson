# YOUR CODE HERE
count = 0
x = int(input())
y = int(input())
d = int(input())
for i in range (x,y+1):
    num = i%d
    if num == 0:
        count += 1
        print(i, end = ' ')
print('count='+str(count))