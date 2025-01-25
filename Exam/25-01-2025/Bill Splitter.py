print("Enter Total bill, number of people: ")
bill,num=map(int,input().split())

print("Enter tip Percentage: ")
tip=int(input())

print(f"Each person has to pay : {bill/num + (((bill/num)*tip)/100)}")