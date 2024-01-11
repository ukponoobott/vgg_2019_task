"""
A command line banking application with the following functionality;
- Create account
- Perform transactions when user is authenticated
    - Check balance
    - Deposit funds
    - Withdraw funds
    - Transfer funds
"""

# mock data for testing
bank = {
    "user@gmail.com": {"password": "12345", "balance": 2500.00}
}


def create_account():
    """Create a new account"""
    print("Thank you for your interest in Banking with us,\nPlease enter your details correctly")
    print("=========================================\n=========================================")
    email = input("Enter your email  ").lower()
    # check if account id already exists
    if ("@" in email) and ("." in email):
        if email in bank.keys():
            print("Account with this email already exists")
        else:
            password = input("Enter your password  ")
            # initialize the balance to $0.0
            balance = 0.0
            bank[email] = {"password": password, "balance": balance}
            print(bank)
            print("Account created successfully, Proceed to make a transaction")
    else:
        print("Email is not valid, Please try again")
        create_account()


def transaction():
    """Authenticate users before they carry out transactions on the account"""
    print("Dear Customer, Welcome!")
    print("                                         \n                                         ")
    email = input("Please enter your email  ").lower()
    # check if user exists or not
    if email not in bank.keys():
        print("Sorry Account does not exist, Please Create account")
    else:
        password = input("Please enter your password  ")
        # check if supplied password matches with the saved password to authenticate user
        if password == bank[email]["password"]:
            print("Dear Customer, you have been authenticated")
            print("Please proceed to select a transaction type")
            print("=========================================\n=========================================")
            print("                                         \n                                         ")
            # user is authenticated give option for transactions available
            transaction_prompt = input("Press 1: Check balance\nPress 2: Deposit\nPress 3: Withdraw\nPress4: Transfer")
            print("                                         \n                                         ")
            if transaction_prompt == "1":
                check_balance(email)

            elif transaction_prompt == "2":
                deposit(email)

            elif transaction_prompt == "3":
                withdraw(email)

            elif transaction_prompt == "4":
                transfer(email)

            else:
                print("You have made an invalid selection, please try again")

        else:
            print("Incorrect Password, User not Authorized")
            create_account()


def check_balance(email):
    """Check account balance"""
    # query data structure to get current user balance
    balance = bank[email]["balance"]
    print("Your balance is ", balance)
    print("===============================")
    print("Thank you for banking with us")
    quit()


def deposit(email):
    """Deposit funds"""
    amount = input("Please Enter an amount you want to deposit")
    while True:
        try:
            valid_amount = float(amount)
            if valid_amount > 0.0:
                break
            else:
                print("Invalid amount, please enter figures only")
                amount = input("Please Enter an amount you want to deposit")
        except ValueError:
            print("Invalid amount, please enter figures only")
            amount = input("Please Enter an amount you want to deposit")
    current_balance = bank[email]["balance"]
    bank[email]["balance"] = current_balance + valid_amount
    new_balance = bank[email]["balance"]
    print("You have deposited ", valid_amount, "Your new balance is ", new_balance)
    print("===============================")
    print("Thank you for banking with us")


def withdraw(email):
    """Withdraw funds"""
    withdrawal_amount = input("Please enter an amount to withdraw")
    # check if there is sufficient balance for the transaction
    while True:
        try:
            valid_withdrawal_amount = float(withdrawal_amount)
            if valid_withdrawal_amount > 0.0:
                break
            else:
                print("Invalid amount, please enter figures only")
                withdrawal_amount = input("Please enter an amount to withdraw")
        except ValueError:
            print("Invalid amount, please enter figures only")
            withdrawal_amount = input("Please enter an amount to withdraw")
    current_balance = bank[email]["balance"]
    if current_balance < valid_withdrawal_amount:
        print("Insufficient funds, your current balance is", current_balance)
        print("Would you make a DEPOSIT now? Yes or No")
        option = input()
        if option.lower() == "yes":
            deposit(email)
        elif option.lower() == "no":
            print("===============================")
            print("Thank you for banking with us")
            quit()
        else:
            print("Invalid selection")
    else:
        bank[email]["balance"] = current_balance - valid_withdrawal_amount
        new_balance = bank[email]["balance"]
        print("You have withdrawn", withdrawal_amount, "Your new balance is ", new_balance)
        print("===============================")
        print("Thank you for banking with us")


def transfer(email):
    """Transfer funds"""
    recipient = input("Please enter the beneficiary's email id").lower()
    if recipient not in bank.keys():
        print("Beneficiary account does not exist, Please try again")
        transfer(email)
    transfer_amount = input("Please enter the amount to transfer")
    while True:
        try:
            valid_amount = float(transfer_amount)
            if valid_amount > 0.0:
                break
            else:
                print("Invalid amount, please enter figures only")
                transfer_amount = input("Please enter the amount to transfer")
        except ValueError:
            print("Invalid amount, please enter figures only")
            transfer_amount = input("Please enter the amount to transfer")
    current_balance = bank[email]["balance"]
    # check if there is sufficient balance for the transaction
    if current_balance < valid_amount:
        print("Insufficient funds, your current balance is", current_balance)
        print("Would you make a DEPOSIT now? Yes or No")
        option = input()
        if option.lower() == "yes":
            deposit(email)
        elif option.lower() == "no":
            print("===============================")
            print("Thank you for banking with us")
            quit()
        else:
            print("Invalid selection")
    else:
        bank[email]["balance"] = current_balance - valid_amount
        new_balance = bank[email]["balance"]
        recipient_balance = bank[recipient]["balance"]
        bank[recipient]["balance"] = recipient_balance + valid_amount
        print("You have transferred", valid_amount, "to", recipient, "Your new balance is ", new_balance)
        print("===============================")
        print("Thank you for banking with us")


prompt = input("Press 1: Create Account \nPress 2: Transaction \nPress q to quit ")
while True:
    if prompt == "1" or prompt == "2" or prompt == "q":
        break
    else:
        print("Invalid selection")
        prompt = input("Press 1: Create Account \nPress 2: Transaction \nPress q to quit ")
if prompt == "1":
    create_account()
elif prompt == "2":
    transaction()
elif prompt == "q":
    print("Thank you, Goodbye!!!")
    quit()
