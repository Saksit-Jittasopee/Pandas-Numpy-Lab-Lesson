# YOUR CODE HERE
nums = int(input())
key_list = []
x = dict()

for i in range (nums):
    key = int(input())
    key_list.append(key)

for count in range (nums):
    if key_list[count]%2 == 0:
        value = 'even'
        x[key_list[count]] = value
    else:
        value = 'odd'
        x[key_list[count]] = value
print(x)