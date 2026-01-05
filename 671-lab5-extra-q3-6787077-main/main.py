# YOUR CODE HERE
x = int(input())  
y = int(input())
term = 0
for i in range(1, y+1):
    term = term*10+x
    print(term, end='')
    if i < y:
        print(',', end='')
