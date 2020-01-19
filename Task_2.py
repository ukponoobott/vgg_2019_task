bank = {

}


def create_account():
    """Create a new account"""
    print("Thank you for your interest in Banking with us,\nPlease enter your details correctly")
    print("=========================================\n=========================================")
    email = input("Enter your email  ")
    # check if account id already exists
    if email in bank.keys():
        print("Account with this email already exists")
    else:
        password = input("Enter your password  ")
        # initialize the balance to $0.0
        balance = 0.0
        bank[email] = {"password": password, "balance": balance}
        print(bank)
        print("Account created successfully, Proceed to make a transaction")


def transaction():
    """Authenticate users before they carry out transactions on the account"""
    print("Dear Customer, Welcome!")
    print("                                         \n                                         ")
    email = input("Please enter your email  ")
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


def deposit(email):
    """Deposit funds"""
    amount = int(input("Please Enter an amount you want to deposit"))
    current_balance = bank[email]["balance"]
    bank[email]["balance"] = current_balance + amount
    new_balance = bank[email]["balance"]
    print("You have deposited ", amount, "Your new balance is ", new_balance)


def withdraw(email):
    """Withdraw funds"""
    withdrawal_amount = int(input("Please enter an amount to withdraw"))
    current_balance = bank[email]["balance"]
    # check if there is sufficient balance for the transaction
    if current_balance < withdrawal_amount:
        print("Insufficient funds, your current balance is", current_balance)
        print("Would you make a DEPOSIT now? Yes or No")
        option = input()
        if option.lower() == "yes":
            deposit(email)
        elif option.lower() == "no":
            print("Thank you for banking with us!")
            quit()
        else:
            print("Invalid selection")
    else:
        bank[email]["balance"] = current_balance - withdrawal_amount
        new_balance = bank[email]["balance"]
        print("You have withdrawn", withdrawal_amount, "Your new balance is ", new_balance)


def transfer(email):
    """Transfer funds"""
    recipient = input("Please enter the beneficiary's email id")
    if recipient not in bank.keys():
        print("Beneficiary account does not exist, Please try again")
        transfer(email)
    transfer_amount = int(input("Please enter the amount to transfer"))
    current_balance = bank[email]["balance"]
    # check if there is sufficient balance for the transaction
    if current_balance < transfer_amount:
        print("Insufficient funds, your current balance is", current_balance)
        print("Would you make a DEPOSIT now? Yes or No")
        option = input()
        if option.lower() == "yes":
            deposit(email)
        elif option.lower() == "no":
            print("Thank you for banking with us!")
            quit()
        else:
            print("Invalid selection")
    else:
        bank[email]["balance"] = current_balance - transfer_amount
        new_balance = bank[email]["balance"]
        recipient_balance = bank[recipient]["balance"]
        bank[recipient]["balance"] = recipient_balance + transfer_amount
        print("You have transferred", transfer_amount, "to", recipient, "Your new balance is ", new_balance)


while True:
    prompt = input("Press 1: Create Account\nPress 2: Transaction ")

    if prompt == "1":
        create_account()

    elif prompt == "2":
        transaction()
