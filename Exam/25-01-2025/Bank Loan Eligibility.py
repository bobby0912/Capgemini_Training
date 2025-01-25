print("Enter Salary, Age and Credit score: ")
salary,age,credit_score=map(int,input().split())


if(salary>=10000 and age>=20 and credit_score>600):
    print("Load Approved.")
else:
    print("Loan Rejected.")
    if(credit_score<600):
        print("Your credit score is too Low")

    elif(age<21):
        print("You are too young.")

    elif(salary<10000):
        print("Your salary is low.")


