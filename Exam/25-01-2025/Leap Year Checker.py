def main():
    try:
        print("Enter year to check it is leap or not: ")
        year=int(input())
        # Check if the year is divisible by 4
        # not every 100 years is a leap year unless it is divisible by 400
        if(year%4==0):
            if(year%100==0 and year%400==0):
                print("Leap year.")
            else:
                print("Not a Leap Year.")
        else:
            print("Not a Leap Year.")
    except ValueError as e:
        print(f"Invalid Input {e}")
        return
if __name__ == "__main__":
    main()