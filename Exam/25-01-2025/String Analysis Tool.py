print("Enter a string :")
s=input()

vowels=0
consonants=0
digits=0
special_chars=0
# vowel_string="aeiouAEIOU"

for i in s:
    # print(ord(i))
    if(i>="0" and i<"9"):
        digits+=1
    elif(ord(i)>=ord("a") and ord(i)<=ord("z")) or (ord(i)>=ord("A") and ord(i)<=ord("Z")):
        if(i=='a' or i=='A' or i=='e' or i=='E'or i=='i' or i=='I'or i=='o' or i=='O'or i=='u' or i=='U'):
            vowels+=1
        else:
            consonants+=1
    
    else:
        special_chars+=1

print(f"Total vowels : {vowels}")
print(f"Total consonants : {consonants}")
print(f"Total digits : {digits}")
print(f"Total special Characters : {special_chars}")
print(s[::-1])