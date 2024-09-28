# Python Banking Program

def show_balance(balance):
    print(f"\nYour Balance is ${balance: .2f}\n")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("\nAmount must be greater then $0\n")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > balance:
        print("\nInsufficient funds!\n")
        return 0
    elif amount < 0:
        print("\nAmount must be greater then $0\n")
        return 0
    else:
        return amount

def app():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4' :
            is_running = False
        else:
            print("\n==================")
            print("  Invalid Choice!")
            print("==================\n")


    print("\n==================")
    print("    THANK YOU!")
    print("==================\n")


if __name__ == '__main__':
    app()