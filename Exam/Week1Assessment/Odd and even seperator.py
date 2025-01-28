def main():
    print("Enter a List of number to Seperate into odd and even lists: ")
    try:    
        arr=list(map(int,input().split()))

        odd=[]
        even=[]

        for i in arr:
            if(i%2==0):
                even.append(i)
            else:
                odd.append(i)
        print(f"Even List: {even}")
        print(f"Odd List: {odd}")
    except ValueError as e:
        print(f"Invalid Input {e}")
        return

if __name__ == "__main__":
    main()