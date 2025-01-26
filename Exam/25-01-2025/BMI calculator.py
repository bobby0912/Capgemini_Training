def calculateBMI(weight:float,height:float):
    bmi=round(weight/(height**2),2)
    if(bmi<18.5):
        return(f"{bmi} Underweight.")
    elif(bmi<25):
        return(f"{bmi} Normal.")
    elif(bmi<30):
        return(f"{bmi} Overweight.")
    else:
        return(f"{bmi} Obese.")

def main():
    try:
        print("Enter Weight(in kgs) and height(in m) to calculate BMI :")
        weight , height =map(float,input().split())
        print(f"Your BMI is {calculateBMI(weight,height)}")
    except ValueError as e:
        print(f"Invalid Input {e}")
        return
    
if __name__ == "__main__":
    main()




