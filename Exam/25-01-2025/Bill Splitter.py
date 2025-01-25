print("Enter Total bill, number of people: ")
bill,numberOfPeople=map(int,input().split())

print("Enter tip Percentage: ")
tip=int(input())

print(f"Each person has to pay : {bill/numberOfPeople + (((bill/numberOfPeople)*tip)/100)}")