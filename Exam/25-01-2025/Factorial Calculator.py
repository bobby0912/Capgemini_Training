def factorial(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x

def main():
    try:
        print("Enter a number to calculate factorial: ")
        n=int(input())

        if(n<0):
            raise ValueError("the given number is negative")
        else:
            print(factorial(n))

    except ValueError as e:
        print(f"Invalid Input {e}")
        return

if __name__ == "__main__":
    main()