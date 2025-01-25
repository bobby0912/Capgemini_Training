print("Enter a List of number to Seperate into odd and even lists: ")
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