def billSplitter(bill,numberOfPeople,tip):
    return round((bill+bill*(tip/100))/numberOfPeople,2)

def main():
    try:
        print("Enter Total bill, number of people: ")
        bill,numberOfPeople=map(int,input().split())

        print("Enter tip Percentage: ")
        tip=int(input())
        print(f"Each person has to pay : {billSplitter(bill,numberOfPeople,tip)}")  
    
    except ValueError as e:
        print(f"Invalid Input {e}")
        return


if __name__ == "__main__":
    main()