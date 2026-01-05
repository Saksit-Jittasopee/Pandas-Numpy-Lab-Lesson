# YOUR CODE HERE
'''
Example of Function Uses:
multiply_even_numbers([2,3,4,5,6]) # 48
'''
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
def multiply_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    if not even_numbers:
        return -1
    result = 1
    for num in even_numbers:
        result = result * num
    return result
x = multiply_even_numbers(lst)
print(x)
