print("Enter Weight(in kgs) and height(in m) to calculate BMI :")
weight , height =map(float,input().split())

bmi=weight/(height**2)
print(f"Your BMI is {round(bmi,2)}")

if(bmi<18.5):
    print("Underweight.")
elif(bmi<25):
    print("Normal.")
elif(bmi<30):
    print("Overweight.")
else:
    print("Obese.")
