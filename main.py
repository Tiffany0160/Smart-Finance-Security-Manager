# Simple ATM System

balance = 1000  # starting balance

print("=== SIMPLE ATM SYSTEM ===")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"Your current balance is: R{balance}")

    elif choice == "2":
        deposit = float(input("Enter amount to deposit: R"))
        if deposit > 0:
            balance += deposit
            print(f"Successfully deposited R{deposit}")
        else:
            print("Invalid deposit amount!")

    elif choice == "3":
        withdraw = float(input("Enter amount to withdraw: R"))
        if withdraw > balance:
            print("Insufficient funds!")
        elif withdraw <= 0:
            print("Invalid withdrawal amount!")
        else:
            balance -= withdraw
            print(f"Successfully withdrew R{withdraw}")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-4.")