# ATM System

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter your name: ")
        while True:
            try:
                initial_balance = float(input("Enter initial balance: "))
                if initial_balance < 0:
                    print("Balance cannot be negative. Please try again.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        self.accounts[name] = initial_balance
        print(f"Account created successfully for {name} with initial balance {initial_balance}.")

    def deposit(self, name):
        if name in self.accounts:
            while True:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    if amount < 0:
                        print("Amount cannot be negative. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")
                    
            self.accounts[name] += amount
            print(f"{amount} deposited successfully. New balance: {self.accounts[name]}")
        else:
            print("Account not found!")

    def withdraw(self, name):
        if name in self.accounts:
            while True:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount < 0:
                        print("Amount cannot be negative. Please try again.")
                    elif amount > self.accounts[name]:
                        print("Insufficient balance. Try a lower amount.")
                    else:
                        self.accounts[name] -= amount
                        print(f"{amount} withdrawn successfully. New balance: {self.accounts[name]}")
                        break
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print("Account not found!")

    def check_balance(self, name):
        if name in self.accounts:
            print(f"Current balance for {name}: {self.accounts[name]}")
        else:
            print("Account not found!")

    def main(self):
        while True:
            print("\n1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Balance Inquiry")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                name = input("Enter your name: ")
                self.deposit(name)
            elif choice == '3':
                name = input("Enter your name: ")
                self.withdraw(name)
            elif choice == '4':
                name = input("Enter your name: ")
                self.check_balance(name)
            elif choice == '5':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

# Run the ATM system
atm = ATM()
atm.main()
