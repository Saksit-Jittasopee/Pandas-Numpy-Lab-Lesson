# YOUR CODE HERE
n = int(input())
mail_dict = {}
for i in range(n):
    email = input()
    num = int(input())
    mail_dict[email] = num
x = []
for email, count in mail_dict.items():
    if count % 2 == 0:
        x.append(email)
if x:
    for email in x:
        print(email)
else:
    print('Not Found')
