def checkPassword(str):
    numberOfChars=False
    upperCase=False
    lowerCase=False
    digits=False
    special_chars=False

    if(len(str)>=8):
        numberOfChars=True

    for i in str:
        if(i.isupper()):
            upperCase=True
        if(i.islower()):
            lowerCase=True
        if(i.isdigit()):
            digits=True
        if(not i.isalnum()):
            special_chars=True
        if(numberOfChars and upperCase and lowerCase and digits and special_chars):
            return("Strong Password")
            
    return("Weak Password")

def main():
    try:
        print("Enter Password to check strength :")
        str=input()
        print(checkPassword(str))
    except ValueError as e:
        print(f"Invalid Input {e}")
        return

if __name__ == "__main__":
    main()


