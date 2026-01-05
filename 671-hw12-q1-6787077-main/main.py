# YOUR CODE HERE

#----   function   ----#


n = int(input())
nums_list = []
for i in range(n):
    nums_list.append(int(input()))
def sum_even_numbers(nums_list):
    even_numbers = [num for num in nums_list if num % 2 == 0]
    result = 0
    for num in even_numbers:
        result = result + num
    return result
print(sum_even_numbers(nums_list))

#----loop to get the data for the list----#


#----print and call the function----#

