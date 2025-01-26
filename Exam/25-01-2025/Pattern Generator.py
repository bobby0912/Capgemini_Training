def generatePattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()

def generateReversePattern(n):
    for i in range(1,n+1):
        for j in range(n+1-i):
            print("*",end="")
        print()

def main():
    try:
        print("Enter number of lines of pattern to generate right angled triangle: ")
        n=int(input())
        generatePattern(n)

        print("press 1 to print the pattern in reverse: ")
        option=int(input())

        if(option==1):
            generateReversePattern(n)
        else:
            print("invalid option")
            return
    except ValueError as e:
        print(f"Invalid Input {e}")
        return

if __name__ == "__main__":
    main()
    