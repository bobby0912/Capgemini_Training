import random
random_number=random.randint(1,100)
while True:
    print("Guess the number:")
    num=int(input())
    if(num==random_number):
        print("uh Guessed it!")
        break
    elif(num>random_number):
        print("Low")
    else :
        print("High")