# YOUR CODE HERE
num = int(input())
student_dict = {}
for i in range(num):
    firstname = input() 
    lastname = input()  
    score = float(input()) 
    student_dict[(firstname, lastname)] = score
max_score = max(student_dict.values())
for (firstname, lastname), score in student_dict.items():
    if score == max_score:
        print(f"Firstname: {firstname}, Last name: {lastname}")