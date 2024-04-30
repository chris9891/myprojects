class Bank:
    def __init__(self):
        self.accounts = {}
        self.username = ""
        self.password = ""

    def create_account(self, account_number, account_holder, initial_balance):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        if not self.login():
            return "Login failed."

        if account_number in self.accounts:
            return "Account already exists"
        if initial_balance < 0:
            return "Initial balance must be non-negative"

        self.accounts[account_number] = {
            'account_holder': account_holder,
            'balance': initial_balance
        }
        return "Account created successfully"

    def deposit(self, account_number, amount):
        if not self.login():
            return "Login failed. Cannot deposit."

        if account_number not in self.accounts:
            return "Account does not exist"
        if amount <= 0:
            return "Amount to deposit must be positive"

        self.accounts[account_number]['balance'] += amount
        return "Deposited " + str(amount) + " successfully. New balance: " + str(self.accounts[account_number]['balance'])

    def withdraw(self, account_number, amount):
        if not self.login():
            return "Login failed. Cannot withdraw."

        if account_number not in self.accounts:
            return "Account does not exist"
        if amount <= 0:
            return "Amount to withdraw must be positive"

        if self.accounts[account_number]['balance'] < amount:
            return "Insufficient balance."

        self.accounts[account_number]['balance'] -= amount
        return "Withdraw " + str(amount) + " successfully. New balance: " + str(self.accounts[account_number]['balance'])

    def check_balance(self, account_number):
        if not self.login():
            return "Login failed. Cannot check balance."

        if account_number not in self.accounts:
            return "Account does not exist"

        return "Account Holder: " + self.accounts[account_number]['account_holder'] + "\nBalance: " + str(self.accounts[account_number]['balance'])

    def login(self):
        valid_credentials = {"user1": "pass1", "user2": "pass2", "user3": "pass3"}
        # providing pre set user_name and password
        if self.username in valid_credentials and self.password == valid_credentials[self.username]:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

bank = Bank()    # Creating a Bank object
print("\n1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Check Balance")
print("5. Logout")

while True:

    choice = input("\nEnter your option (1 to 5): ")

    if choice == '1':
        account_number = input("Enter Account Number: ")
        account_holder = input("Enter Account Holder's Name: ")
        initial_balance = float(input("Enter Initial Balance: "))
        result = bank.create_account(account_number, account_holder, initial_balance)
        print(result)

    elif choice == '2':
        account_number = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Deposit: "))
        result = bank.deposit(account_number, amount)
        print(result)

    elif choice == '3':
        account_number = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Withdraw: "))
        result = bank.withdraw(account_number, amount)
        print(result)

    elif choice == '4':
        account_number = input("Enter Account Number: ")
        result = bank.check_balance(account_number)
        print(result)

    elif choice == '5':
        print("Logout")
        break

    else:
        print("Please retry with a valid option")
