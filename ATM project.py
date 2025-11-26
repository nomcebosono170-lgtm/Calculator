# Simple ATM program
balance = 1000 

while True:
    print("\n==== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter yout choice: ")

    if choice == "1":
        print(f"Your balance is R{balance}")
    elif choice =="2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposit R{amount}. New balance: R{balance}")
    elif choice =="3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance: 
            balance -= amount
            print(f"Withdrew R{amount}. Remaining balance: R{balance}")
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Try again.")