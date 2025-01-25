print("Enter text to check word count: ")
str=input()

arr=list(str.split(" "))
# print(arr)
arr.remove("")

print(len(arr))