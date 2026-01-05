# YOUR CODE HERE
x = input()
remove_symbols = ''

for i in x:
    if i.isalnum():
        remove_symbols += i
        
if remove_symbols == '':
    print("empty")
else:
    print(remove_symbols)
