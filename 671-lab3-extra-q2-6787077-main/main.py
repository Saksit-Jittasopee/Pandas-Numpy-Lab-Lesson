# YOUR CODE HERE
member = input()
size = input()
topping = input()

if size == 'M':
    s = 50
    if topping == 'Y':
     s = 50
    if topping == 'N':
     s = 50-10
if size == 'L':
    s = 60
    if topping == 'Y':
     s = 60
    if topping == 'N':
     s = 60-10

if member == 'Y':
   m = 10/100
   discount = s*m
   price = float(s) - discount
if member == 'N':
   price = float(s)
print('Total price:', round(price,2))