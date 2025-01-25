print("Enter number of lines of pattern to generate right angled triangle: ")
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

print("press 1 to print the pattern in reverse: ")
option=int(input())

if(option==1):
    for i in range(1,n+1):
        for j in range(n+1-i):
            print("*",end="")
        print()
else:
    print("invalid option")
    