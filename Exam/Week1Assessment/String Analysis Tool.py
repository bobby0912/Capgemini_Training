def analyzeString(s):
    vowels=consonants=digits=special_chars=0

    for i in s:
        if(i.isdigit()):
            digits+=1
        elif i.isalpha():
            if(i=='a' or i=='A' or i=='e' or i=='E'or i=='i' or i=='I'or i=='o' or i=='O'or i=='u' or i=='U'):
                vowels+=1
            else:
                consonants+=1
        
        else:
            special_chars+=1
    return vowels,consonants,digits,special_chars
    
def reverseString(s):
    return s[::-1]
    
def main():
    try:
        print("Enter a string :")
        s=input()
        vowels,consonants,digits,special_chars=analyzeString(s)
        print(f"Total vowels : {vowels}")
        print(f"Total consonants : {consonants}")
        print(f"Total digits : {digits}")
        print(f"Total special Characters : {special_chars}")
        print("Reversed String : ",{reverseString(s)})
        
    except ValueError as e: 
        print(f"Invalid Input {e}")
        return

if __name__ == "__main__":
    main()