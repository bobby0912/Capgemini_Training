def assignGrade(percentage):
    if(percentage>=91):
        return("A")
    elif(percentage>=75):
        return("B")
    elif(percentage>=40):
        return("C")
    else:
        return("Fail")

def main():
    try:
        print("student Name:")
        name=input()
        marks = list(map(int, input("Enter marks in 5 subjects out of 100.").split()))

        print(f"Student Name: {name}")
        print(f"Total marks:{sum(marks)}")

        percentage=sum(marks)/500
        
        print(f"Percentage{percentage}")
        print(f"Grade : {assignGrade(percentage)}")
        
    except ValueError as e:
        print(f"Invalid Input {e}")
        return  
    
if __name__ == "__main__":
    main()
