class Bank:
    def __init__(self, initial_amount):
        self.__balance = initial_amount

    def deposit(self, amount):
        if amount < 100 or amount % 10 != 0:
            return "Invalid deposit amount!"
        self.__balance += amount
        return f"{amount}₹ deposited successfully."

    def withdraw(self, amount):
        if amount < 100 or amount % 10 != 0:
            return "Invalid withdrawal amount!"
        if amount > self.__balance:
            return "Insufficient balance!"
        self.__balance -= amount
        return f"{amount}₹ withdrawn successfully."

    def total_balance(self):
        return f"Current Balance: {self.__balance}₹"


def menu():
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


bank = Bank(6000)

while True:
    menu()
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if choice == 1:
        amount = int(input("Enter amount: "))
        print(bank.deposit(amount))

    elif choice == 2:
        amount = int(input("Enter amount: "))
        print(bank.withdraw(amount))

    elif choice == 3:
        print(bank.total_balance())

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
