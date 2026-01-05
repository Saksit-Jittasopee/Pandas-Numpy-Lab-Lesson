# YOUR CODE HERE
list = []
x = input()
list.append(x)
dup = 0
while True:
    if x == '-1':
        list.remove('-1')
        break
    else:
        x = input()
        list.append(x)
list.sort()

dup = {}

for i in list:
    if i in dup:
        dup[i] += 1
    else:
        dup[i] = 1

for i in list:
    if i in dup:
        print(f'{i}={dup[i]}',end=' ')
        del dup[i]