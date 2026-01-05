# YOUR CODE HERE
list = []
x = input()
list.append(x)
if x == 'a':
    list.remove('a')
elif x == 'e':
    list.remove('e')
elif x == 'i':
    list.remove('i')
elif x == 'o':
    list.remove('o')
elif x == 'u':
    list.remove('u')
while True:
    if x == '0':
        list.remove('0')
        break
    else:
        x = input()
        list.append(x)
        if x == 'a':
            list.remove('a')
        elif x == 'e':
            list.remove('e')
        elif x == 'i':
            list.remove('i')
        elif x == 'o':
            list.remove('o')
        elif x == 'u':
            list.remove('u')
print(list)