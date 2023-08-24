class BankAccount:
    def __init__(self, account_num):
        self.account_num = account_num
        self.balance = 0

    def create_account(self):
        self.balance = 0
        print("Your Account Num is : ",account_num)

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

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_num):
        for account in self.accounts:
            if account.account_num == account_num:
                return None
        
        new_account = BankAccount(account_num)
        self.accounts.append(new_account)
        return new_account

    def get_account(self, account_num):
        for account in self.accounts:
            if account.account_num == account_num:
                return account
        return None

# Main program loop
bank = Bank()

while True:
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        account_num = input("Enter a new account number: ")
        account = bank.create_account(account_num)
        if account:
            print(f"Account {account_num} created.")
        else:
            print(f"Account {account_num} already exists.")
    elif choice == 2:
        account_num = input("Enter your account number: ")
        account = bank.get_account(account_num)
        if account:
            print("1. Check Balance")
            print("2. Withdraw Amount")
            print("3. Deposit Amount")
            sub_choice = int(input("Enter your choice: "))
            if sub_choice == 1:
                balance = account.check_balance()
                print(f"Balance: {balance}")
            elif sub_choice == 2:
                withdrawal_amt = float(input("Enter the withdrawal amount: "))
                if account.withdraw_amount(withdrawal_amt):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance for withdrawal.")
            elif sub_choice == 3:
                deposit_amt = float(input("Enter the deposit amount: "))
                account.deposit_amount(deposit_amt)
                print("Deposit successful.")
            else:
                print("Invalid choice.")
        else:
            print(f"Account {account_num} does not exist.")
    elif choice == 3:
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
