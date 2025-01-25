balance = 0
while True:
    print("\n1. Check Balance \n2. Deposit Money\n3. Withdraw Money \n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"Your balance is {balance}.")
    elif choice == 2:
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print(f"Your balance is {balance}.")
    elif choice == 3:
        amount = int(input("Enter the amount to withdraw: "))
        if balance >= amount:
            balance -= amount
            print(f"Your balance is {balance}.")
        else:
            print("Insufficient balance.")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
