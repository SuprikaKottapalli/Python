# Define a dictionary to store bank accounts and their balances
bank_accounts = {}

def create_account(account_num):
    bank_accounts[account_num] = 0  # Initialize the balance to zero

def check_balance(account_num):
    if account_num in bank_accounts:
        return bank_accounts[account_num]
    else:
        print("Account doesn't exist.")
        create_new = input("Do you want to create a new account? (yes/no): ")
        if create_new.lower() == "yes":
            create_account(account_num)
            return 0
        else:
            print("Exiting application.")

def withdraw_amount(account_num, withdraw_amount):
    if account_num in bank_accounts:
        if bank_accounts[account_num] >= withdraw_amount:
            bank_accounts[account_num] -= withdraw_amount
            print("Withdrawal successful.")
            return bank_accounts[account_num]
        else:
            print("Insufficient balance for withdrawal.")
    else:
        print("Account doesn't exist.")
        create_new = input("Do you want to create a new account? (yes/no): ")
        if create_new.lower() == "yes":
            create_account(account_num)
            return 0
        else:
            print("Exiting application.")

def deposit_amount(account_num, deposit_amount):
    if account_num in bank_accounts:
        bank_accounts[account_num] += deposit_amount
        print("Deposit successful.")
        return bank_accounts[account_num]
    else:
        print("Account doesn't exist.")
        create_new = input("Do you want to create a new account? (yes/no): ")
        if create_new.lower() == "yes":
            create_account(account_num)
            return 0
        else:
            print("Exiting application.")



# code without errors

while True:
    print("1. Check Balance")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        account_num = input("Enter your account number: ")
        balance = check_balance(account_num)
        print(f"Balance: {balance}")
    elif choice == 2:
        account_num = input("Enter your account number: ")
        withdrawal_amt = float(input("Enter the withdrawal amount: "))
        balance = withdraw_amount(account_num, withdrawal_amt)  # Use a different variable name
        print(f"Updated Balance: {balance}")
    elif choice == 3:
        account_num = input("Enter your account number: ")
        deposit_amt = float(input("Enter the deposit amount: "))
        balance = deposit_amount(account_num, deposit_amt)  # Use a different variable name
        print(f"Updated Balance: {balance}")
    elif choice == 4:
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Rest of your code
