def isListPalindrome(arr):
    # arr2=arr[::-1]
    # print(arr2)
    return arr==arr[::-1]

def getInput():
    return list(input("enter string: "))

def main():
    arr=getInput()
    print(isListPalindrome(arr))

main()