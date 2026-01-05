# YOUR CODE HERE
m = int(input())
if m>1:
    for i in range(m):
        for j in range(1,m):
            stars = '*' * (2*i+1)
            line = '-' * (m-i-1)
        print(line + stars + line)
else:
    print('*')