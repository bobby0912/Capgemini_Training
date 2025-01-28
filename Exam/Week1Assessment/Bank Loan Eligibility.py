def checkLoanEligibility(salary,age,credit_score):
    if(salary>=10000 and age>=20 and credit_score>600):
        return("Load Approved.")
    else:
        # return("")
        if(credit_score<600):
            return("Loan Rejected.Your credit score is too Low")

        elif(age<21 and age>60):
            return("Loan Rejected.You age must be between 21 and 60 years.")

        elif(salary<10000):
            return("Loan Rejected.Your salary is low.")

def main():

    print("Enter Salary, Age and Credit score: ")

    try:
        salary,age,credit_score=map(int,input().split())
        print(checkLoanEligibility(salary,age,credit_score))
    except ValueError as e:
        print(f"Invalid Input {e}")
        return


    


if __name__ == "__main__":
    main()
