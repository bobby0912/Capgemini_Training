print("Enter number and range:")
num,x=map(int,input().split())

print("Multiplication table:\n")
for i in range(1,x+1):
    print(f"{num} x {i} = {num*i}")

