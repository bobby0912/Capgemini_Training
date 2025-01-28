def isPrime(num):
    if(num==1):
        return False
    for i in range (2, num-1):
        if(num%i==0):
            return False
    return True

def main():
    try:
        print("Enter two numbers: ")
        a,b=map(int,input().split())

        for i in range(a,b):
            if isPrime(i)==True:
                print(f"{i} is a prime number.")
                
    except ValueError as e:
        print(f"Invalid Input {e}")
        return
    
if __name__ == "__main__":
    main()