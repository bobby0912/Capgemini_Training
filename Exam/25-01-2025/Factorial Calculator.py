def fact(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x


print("Enter a number to calculate factorial: ")
n=int(input())

if(n<0):
    print("the given number is negative")
else:
    print(fact(n))