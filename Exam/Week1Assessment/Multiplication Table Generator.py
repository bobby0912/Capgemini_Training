def printTable(num,x):
    for i in range(1,x+1):
        print(num,"*",i,"=",num*i)

def main():
    try:
        print("Enter number and range:")
        num,x=map(int,input().split())

        if(x<0):
            raise ValueError("The given number is negative")

        print("Multiplication table:\n")
        printTable(num,x)
        
    except ValueError as e:
        print(f"Invalid Input {e}")
        return

if __name__ == "__main__":
    main()