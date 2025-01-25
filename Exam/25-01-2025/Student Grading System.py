print("student Name:")
name=input()
marks = list(map(int, input("Enter marks in 5 subjects out of 100.").split()))

# print("List:", user_input)

print(f"Total marks:{sum(marks)}")
percentage=sum(marks)/500
print(f"Percentage{percentage}")

print("Grade : ")
if(percentage>=91):
    print("A")
elif(percentage>=75):
    print("B")
elif(percentage>=40):
    print("C")
else:
    print("Fail")
