# YOUR CODE HERE
listA = []
k = int(input()) #input k
A = input() #input A
while True:
    if A == 'q': #if A == 'q' do break
        break
    else:
        listA.append(A) #if A != 'q' loop input
        A = input()
sum = 0
if len(listA) < k: #if listA < k
    print('Invalid')
else:
    for i in range(k): 
        sum = sum + float(listA[i]) #front
        sum = sum + float(listA[-(i+1)]) #back
    print(sum)