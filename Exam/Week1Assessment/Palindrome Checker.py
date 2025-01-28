def checkPalindrome(str):
    # return str==str[::-1]
    for i in range(len(str)//2):
        if(str[i]!=str[len(str)-i-1]):
            return False
    return True

def main():
    try:
        while True:
            print("Enter a string to check whether it is a palindrome or not: ")
            str=input()

            if(checkPalindrome(str)):
                print("string is Palindrome.")
            else:
                print("stirng is not a palindrome.")
            
            print("press 1 to continue: ")
            option=int(input())

            if(option!=1):
                break
            
    except ValueError as e:
        print(f"Invalid Input {e}")
        return
    
if __name__ == "__main__":
    main()