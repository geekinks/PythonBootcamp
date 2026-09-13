# ============================================================
#                    🏦 GEEK BANK
#              ACCOUNT MANAGEMENT SYSTEM
# ============================================================

accounts = {}


# ------------------------------------------------------------
# CREATE ACCOUNT
# ------------------------------------------------------------
def create_account():

    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter your full name: ")

    while True:
        pin = input("Create a 4-digit PIN: ")

        if pin.isdigit() and len(pin) == 4:
            break

        print("❌ PIN must contain exactly 4 digits.")

    # Generate account number
    account_number = str(1001 + len(accounts))

    accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("\n✅ Account created successfully!")
    print("🏦 Bank: Geek Bank")
    print("👤 Name:", name)
    print("💳 Account Number:", account_number)
    print("💰 Opening Balance: ₦0.00")


# ------------------------------------------------------------
# LOGIN
# ------------------------------------------------------------
def login():

    print("\n========== LOGIN ==========")

    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if account_number not in accounts:
        print("❌ Account not found.")
        return None

    if accounts[account_number]["pin"] != pin:
        print("❌ Incorrect PIN.")
        return None

    print("\n✅ Login successful!")
    print("Welcome,", accounts[account_number]["name"])

    return account_number


# ------------------------------------------------------------
# VIEW ACCOUNT DETAILS
# ------------------------------------------------------------
def account_details(account_number):

    account = accounts[account_number]

    print("\n========== ACCOUNT DETAILS ==========")
    print("🏦 Bank:", "Geek Bank")
    print("👤 Name:", account["name"])
    print("💳 Account Number:", account_number)
    print(f"💰 Balance: ₦{account['balance']:,.2f}")


# ------------------------------------------------------------
# CHECK BALANCE
# ------------------------------------------------------------
def check_balance(account_number):

    balance = accounts[account_number]["balance"]

    print("\n========== ACCOUNT BALANCE ==========")
    print(f"💰 Available Balance: ₦{balance:,.2f}")


# ------------------------------------------------------------
# DEPOSIT MONEY
# ------------------------------------------------------------
def deposit(account_number):

    print("\n========== DEPOSIT MONEY ==========")

    try:
        amount = float(input("Enter amount to deposit: ₦"))

        if amount <= 0:
            print("❌ Amount must be greater than ₦0.")
            return

        accounts[account_number]["balance"] += amount

        accounts[account_number]["transactions"].append(
            f"Deposited ₦{amount:,.2f}"
        )

        print(f"✅ ₦{amount:,.2f} deposited successfully.")

        check_balance(account_number)

    except ValueError:
        print("❌ Please enter a valid amount.")


# ------------------------------------------------------------
# WITHDRAW MONEY
# ------------------------------------------------------------
def withdraw(account_number):

    print("\n========== WITHDRAW MONEY ==========")

    try:
        amount = float(input("Enter amount to withdraw: ₦"))

        if amount <= 0:
            print("❌ Amount must be greater than ₦0.")
            return

        balance = accounts[account_number]["balance"]

        if amount > balance:
            print("❌ Insufficient balance.")
            print(f"Your balance is ₦{balance:,.2f}")
            return

        accounts[account_number]["balance"] -= amount

        accounts[account_number]["transactions"].append(
            f"Withdrew ₦{amount:,.2f}"
        )

        print(f"✅ ₦{amount:,.2f} withdrawn successfully.")

        check_balance(account_number)

    except ValueError:
        print("❌ Please enter a valid amount.")


# ------------------------------------------------------------
# TRANSFER MONEY
# ------------------------------------------------------------
def transfer(account_number):

    print("\n========== TRANSFER MONEY ==========")

    recipient = input("Enter recipient account number: ")

    # Check recipient
    if recipient not in accounts:
        print("❌ Recipient account does not exist.")
        return

    # Prevent transfer to yourself
    if recipient == account_number:
        print("❌ You cannot transfer money to yourself.")
        return

    try:

        amount = float(input("Enter amount to transfer: ₦"))

        if amount <= 0:
            print("❌ Amount must be greater than ₦0.")
            return

        sender_balance = accounts[account_number]["balance"]

        if amount > sender_balance:
            print("❌ Insufficient balance.")
            print(f"Your balance is ₦{sender_balance:,.2f}")
            return

        recipient_name = accounts[recipient]["name"]

        # Remove money from sender
        accounts[account_number]["balance"] -= amount

        # Add money to recipient
        accounts[recipient]["balance"] += amount

        # Sender transaction
        accounts[account_number]["transactions"].append(
            f"Transferred ₦{amount:,.2f} to "
            f"{recipient_name} ({recipient})"
        )

        # Recipient transaction
        accounts[recipient]["transactions"].append(
            f"Received ₦{amount:,.2f} from "
            f"{accounts[account_number]['name']} ({account_number})"
        )

        print("\n✅ Transfer successful!")
        print("Recipient:", recipient_name)
        print(f"Amount: ₦{amount:,.2f}")

        check_balance(account_number)

    except ValueError:
        print("❌ Please enter a valid amount.")


# ------------------------------------------------------------
# TRANSACTION HISTORY
# ------------------------------------------------------------
def transaction_history(account_number):

    print("\n========== TRANSACTION HISTORY ==========")

    transactions = accounts[account_number]["transactions"]

    if len(transactions) == 0:

        print("📭 No transactions yet.")

    else:

        for number, transaction in enumerate(transactions, 1):

            print(f"{number}. {transaction}")


# ------------------------------------------------------------
# CHANGE PIN
# ------------------------------------------------------------
def change_pin(account_number):

    print("\n========== CHANGE PIN ==========")

    old_pin = input("Enter your current PIN: ")

    if old_pin != accounts[account_number]["pin"]:

        print("❌ Incorrect current PIN.")
        return

    while True:

        new_pin = input("Enter your new 4-digit PIN: ")

        if new_pin.isdigit() and len(new_pin) == 4:
            break

        print("❌ PIN must contain exactly 4 digits.")

    accounts[account_number]["pin"] = new_pin

    print("✅ PIN changed successfully!")


# ------------------------------------------------------------
# BANK MENU
# ------------------------------------------------------------
def bank_menu(account_number):

    while True:

        print("\n")
        print("=" * 40)
        print("              🏦 GEEK BANK")
        print("=" * 40)

        print("1. 💰 Deposit Money")
        print("2. 💸 Withdraw Money")
        print("3. 🔄 Transfer Money")
        print("4. 💳 View Account Balance")
        print("5. 👤 Account Details")
        print("6. 📜 Transaction History")
        print("7. 🔐 Change PIN")
        print("8. 🚪 Logout")

        choice = input("\nChoose an option: ")

        if choice == "1":

            deposit(account_number)

        elif choice == "2":

            withdraw(account_number)

        elif choice == "3":

            transfer(account_number)

        elif choice == "4":

            check_balance(account_number)

        elif choice == "5":

            account_details(account_number)

        elif choice == "6":

            transaction_history(account_number)

        elif choice == "7":

            change_pin(account_number)

        elif choice == "8":

            print("\n👋 You have been logged out.")
            break

        else:

            print("❌ Invalid option. Please choose 1-8.")


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------
while True:

    print("\n")
    print("=" * 40)
    print("          🏦 WELCOME TO GEEK BANK")
    print("=" * 40)

    print("1. 🆕 Create Account")
    print("2. 🔐 Login")
    print("3. 🚪 Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        create_account()

    elif choice == "2":

        account_number = login()

        if account_number is not None:

            bank_menu(account_number)

    elif choice == "3":

        print("\nThank you for banking with GEEK BANK! 🏦")
        print("Goodbye! 👋")
        break

    else:

        print("❌ Invalid option. Please choose 1-3.")
