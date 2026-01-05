# YOUR CODE HERE
'''
Example of Function Uses:
list_manipulation([1,2,3], "remove", "end", 1) # [1,2]
list_manipulation([1,2,3], "remove", "beginning",1) #  [2,3]
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''
def list_manipulation(A, command, location, value):
    if command == 'remove' and location == 'end':
        A.pop()
    elif command == 'remove' and location == 'beginning':
        A.pop(0)
    elif command == 'add' and location == 'end':
        A.append(value)
    elif command == 'add' and location == 'beginning':
        A.insert(0, value)
    return A

A = []
for i in range(3):
    A.append(input())
command = input()
location = input()
value = input()

output = list_manipulation(A, command, location, value)
print(output)
