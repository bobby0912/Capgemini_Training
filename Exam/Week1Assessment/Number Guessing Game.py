import random

def guessTheNumber(random_number):
    # while True:
    try:
        print("Guess the number:")
        num=int(input())
        if(num==random_number):
            print("uh Guessed it!")
            return
        elif(num < random_number):
            print("Too Low")
        else :
            print("Too High")
    except ValueError as e:
        print(f"Invalid Input {e}")
    guessTheNumber(random_number)

def generateRandomNumber():
    return random.randint(1,100)

def main():
    random_number=generateRandomNumber()
    print("random number generated")
    guessTheNumber(random_number)

if __name__ == "__main__":
    main()
