# YOUR CODE HERE
numbers = []

while True:
    x = input()
    
    if x == 'q':
        break
    
    else:
        number = float(x)
        numbers.append(number)

sum = 0
for num in numbers:
    sum += num

ave = sum / len(numbers)

import statistics
for num in numbers:
    std_deviation = statistics.stdev(numbers)

print(round(ave, 2), round(std_deviation, 2))