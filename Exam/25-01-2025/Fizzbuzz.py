def main():
    try:
        print("Enter two numbers to print fizzbuzz in range: ")
        start,end=map(int,input().split())

        for i in range(start,end+1):
            if(i%15==0):
                print("FizzBuzz ",end=" ")
            elif(i%3==0):
                print("Fizz ",end=" ")
            elif(i%5==0):
                print("Buzz ",end=" ")
            else:
                print(i,end=" ")
    except ValueError as e:
        print(f"Invalid Input {e}")
        return
    
if __name__ == "__main__":
    main()