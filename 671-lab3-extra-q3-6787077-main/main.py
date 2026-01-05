# YOUR CODE HERE
Lab = float(input())
Assignment = float(input())
Quiz = float(input())
CheckPointExam = float(input())
Project = float(input())
score = Lab/12*10 + Assignment/12*10 + Quiz/12*10 + CheckPointExam/80*50 + Project/100*20
if score>=85:
    print('Grade: A')
elif score>=80:
    print('Grade: B+')
elif score>=75:
    print('Grade: B')
elif score>=70:
    print('Grade: C+')
elif score>=65:
    print('Grade: C')
elif score>=60:
    print('Grade: D+')
elif score>=50:
    print('Grade: D')
else:
    print('Grade: F')