balance = 0

def main():
    while True:
        print("\n1. Check Balance \n2. Deposit Money\n3. Withdraw Money \n4. Exit")
        choice = int(input("Enter your choice: "))
        # Check balance option
        if choice == 1:
            print(f"Your balance is {balance}.")
        # Deposit money option
        elif choice == 2:
            amount = int(input("Enter the amount to deposit: "))
            balance += amount
            print(f"Your balance is {balance}.")
        # Withdraw money option
        elif choice == 3:
            amount = int(input("Enter the amount to withdraw: "))
            if balance >= amount:
                balance -= amount
                print(f"Your balance is {balance}.")
            else:
                print("Insufficient balance.")
        # Exit option
        elif choice == 4:
            break
        # Invalid choice
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
