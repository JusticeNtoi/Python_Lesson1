# Python Banking Program


def show_balance(balance):
    print(f"\n-------------------------------")
    print(f"Balance: ${balance: .2f}")
    print(f"===============================\n")


def deposit(balance):
    while True:
        try:
            amount = float(input("Enter an amount to be deposited: "))

            if amount <= 0:
                print("\nAmount must be greater than $0\n")
                continue
            else:
                print(f"\nSuccessfully deposited: ${amount:.2f}.")
                print(f"Current balance: ${balance + amount:.2f}\n")
                return amount
        except ValueError:
            print(f"\nInvalid input Amount!\n")


def withdraw(balance):
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            amount = float(input("Enter an amount to be withdrawn: "))

            if amount > balance:
                print(f"\nInsufficient funds!")
                print(f"Current balance: ${balance:.2f}\n")
                return 0
            elif amount <= 0:
                print(f"\nAmount must be greater than $0")
                print(f"Current balance: ${balance:.2f}\n")
                continue
            else:
                print(f"\nSuccessfully withdrawn: ${amount:.2f}.")
                print(f"Current balance: ${balance - amount:.2f}\n")
                return amount
        except ValueError:
            print(f"\nInvalid input Amount!\n")

        attempts += 1

    print("\nMaximum attempts reached.\n")
    return 0


def app():
    balance = 0.0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("\n==================")
            print("  Invalid Choice!")
            print("==================\n")

    print("\n==================")
    print("    THANK YOU!")
    print("==================\n")


if __name__ == "__main__":
    app()
