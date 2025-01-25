# import sys
print("Enter List of numbers: ")
arr=list(map(int,input().split()))

max1=max2=-1e9+7

for i in arr:
    if(max1<i):
        max2=max1
        max1=i
    if(max2<i and i!=max1):
        max2=i

# print(max1)
print(f"Second Largest element in the list is: {max2}")






# arr.sort(reverse=True)

# print("Second largest element in the list is :")
# print(arr[1])