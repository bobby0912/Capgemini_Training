print("Enter year to check it is leap or not: ")
year=int(input())

if(year%4==0):
    if(year%100==0 and year%400==0):
        print("Leap year.")
    else:
        print("Not a Leap Year.")
else:
    print("Not a Leap Year.")