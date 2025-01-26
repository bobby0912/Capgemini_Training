#c/5 = f-32/9 = k-273/5
def celsiusToFahrenheit(t):
    return ((9*t)/5)+32
def celsiusToKelvin(t):
    return t+273

def fahrenheitToCelsius(t):
    return (5*(t-32))/9
def fahrenheitToKelvin(t):
    return (5*(t-32))/9 + 273

def kelvinToCelsius(t):
    return t-273
def kelvinToFahrenheit(t):
    return ((t-273)/5)*9 +32

def main():
    try:
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
                print(celsiusToFahrenheit(t))
            elif(option1==1 and option2==3):
                print(celsiusToKelvin(t))
            elif(option1==2 and option2==1):
                print(fahrenheitToCelsius(t))
            elif(option1==2 and option2==3):
                print(fahrenheitToKelvin(t))
            elif(option1==3 and option2==1):
                print(kelvinToCelsius(t))
            elif(option1==3 and option2==2):
                print(kelvinToFahrenheit(t))
            else:
                print("Invalid option.\n")
    
    except ValueError as e: 
        print(f"Invalid Input {e}")
        return
    
if __name__ == "__main__":
    main()
    
    
