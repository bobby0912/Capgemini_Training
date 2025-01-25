while True:
    print("Enter a string to check whether it is a palindrome or not: ")
    str=input()
    if(str==str[::-1]):
        print("string is Palindrome.")
    else:
        print("stirng is not a palindrome.")
    
    print("press 1 to continue: ")
    option=int(input())

    if(option!=1):
        break