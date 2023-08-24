class BankAccount:
    def __init__(self, account_num):
        self.account_num = account_num
        self.balance = 0

    def create_account(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def withdraw_amount(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            return True
        else:
            return False

    def deposit_amount(self, deposit_amount):
        self.balance += deposit_amount
        return True

# Main program loop
while True:
    print("1. Check Balance")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        account_num = input("Enter your account number: ")
        account = BankAccount(account_num)
        balance = account.check_balance()
        print(f"Balance: {balance}")
    elif choice == 2:
        account_num = input("Enter your account number: ")
        withdrawal_amt = float(input("Enter the withdrawal amount: "))
        account = BankAccount(account_num)
        if account.withdraw_amount(withdrawal_amt):
            print("Withdrawal successful.")
        else:
            print("Insufficient balance for withdrawal.")
    elif choice == 3:
        account_num = input("Enter your account number: ")
        deposit_amt = float(input("Enter the deposit amount: "))
        account = BankAccount(account_num)
        account.deposit_amount(deposit_amt)
        print("Deposit successful.")
    elif choice == 4:
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
