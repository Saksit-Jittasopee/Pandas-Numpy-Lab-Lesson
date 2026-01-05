# YOUR CODE HERE
n = int(input())
shopping_list = []
total = 0
for i in range (n):
    name = input()
    quantity = int(input())
    price = float(input())
    x = {'name':name,
         'quantity':quantity,
         'price':price,
        }
    shopping_list.append(x)
    total = total + (quantity*price)
print(shopping_list)
print(total)