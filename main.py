import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{Fore.GREEN}Deposit successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{Fore.GREEN}Withdrawal successful. Current balance: {self.balance}")
        else:
            print(f"{Fore.RED}Insufficient funds. Current balance: {self.balance}")

    def check_balance(self):
        print(f"{Fore.GREEN}Current balance: {self.balance}")

def main():
    bank = Bank()

    while True:
        print(f"\n{Fore.GREEN}Bank Management System")
        print(f"{Fore.GREEN}1. Deposit")
        print(f"{Fore.GREEN}2. Withdraw")
        print(f"{Fore.GREEN}3. Check Balance")
        print(f"{Fore.GREEN}4. Exit")

        choice = input(f"{Fore.GREEN}Enter your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input(f"{Fore.GREEN}Enter the deposit amount: "))
            bank.deposit(amount)
        elif choice == '2':
            amount = float(input(f"{Fore.GREEN}Enter the withdrawal amount: "))
            bank.withdraw(amount)
        elif choice == '3':
            bank.check_balance()
        elif choice == '4':
            print(f"{Fore.CYAN}Exiting the Bank Management System. Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
