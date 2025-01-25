print("Enter Password to check strength :")
s=input()

numberOfChars=False
upperCase=False
lowerCase=False
digits=False
special_chars=False

if(len(s)>=8):
    numberOfChars=True

for i in s:
    # print(ord(i))
    if(i>="0" and i<"9"):
        digits=True
    if(ord(i)>=ord("a") and ord(i)<=ord("z")):
        lowerCase=True
    if(ord(i)>=ord("A") and ord(i)<=ord("Z")):
        upperCase=True 
    else:
        special_chars=True

# print(numberOfChars,upperCase,lowerCase,digits,special_chars)

if( numberOfChars and upperCase and lowerCase and digits and special_chars):
    print("Strong Password.")
else:
    print("Weak Password.")
