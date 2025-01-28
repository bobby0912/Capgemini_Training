def getInput():
    return input()

def main():
    str=getInput()
    convertToWords(str)

def convertToWords(str):
    list1=[]
    temp=''
    for i in str:
        if i!=' ':
            temp+=i
        elif i==' ' and temp!='':
            list1.append(temp)
            temp=''
    if(temp!=""):
        list1.append(temp)
    print(list1)
    return list1

main()