a=-1
b=0
n=int(input("Enter the number of terms: "))
print(a,b,sep=" ",end=" ")
for i in range(n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c