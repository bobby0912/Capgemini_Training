#c/5 = f-32/9 = k-273/5
def cel_fah(t):
    return ((9*t)/5)+32
def cel_kel(t):
    return t+273

def fah_cel(t):
    return (5*(t-32))/9
def fah_kel(t):
    return (5*(t-32))/9 + 273

def kel_cel(t):
    return t-273
def kel_fah(t):
    return ((t-273)/5)*9 +32

while True:
    print("Enter Temparature:")
    t=int(input())
    print("\n1. Celcius\n2. Fahrenheit\n3. Kelvin\n4. Exit\nEnter the first unit: ")
    option1=int(input())
    if(option1>4):
        print("Invalid option.\n")
        continue
    print("\n1. Celcius\n2. Fahrenheit\n3. Kelvin\nEnter the second unit: ")
    option2=int(input())
    if(option2>3):
        print("Invalid option.\n")
        continue
    if(option1==option2):
        print("Same units.\n")
    if(option1==1 and option2==2):
        print(cel_fah(t))
    elif(option1==1 and option2==3):
        print(cel_kel(t))
    elif(option1==2 and option2==1):
        print(fah_cel(t))
    elif(option1==2 and option2==3):
        print(fah_kel(t))
    elif(option1==3 and option2==1):
        print(kel_cel(t))
    elif(option1==3 and option2==2):
        print(kel_fah(t))
    
    
