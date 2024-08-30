# Create a class bank using constructor with arguments account_holder_name, email, account_number, and balance set default balance=0
# deposit(amount) : balance + balance
    # amount_deposited
    # Final balance
# withdraw(amount): check balance is less than amount ("insufficient amount")
    # Amount_ withdrawed
    # # Final balance
# Display
#    account_holder_name
#    email, account_number, and balance


class bank:
    def __init__(self, account_holder_name, email, account_number, balance =0):
        self.name = account_holder_name
        self.email = email
        self.account_no = account_number
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Amount Deposited = ", amount)
        print("Final balance = ", self.balance)
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn = {amount}")
            print(f"Final Balance = {self.balance}")
    def display(self):
        print(f"Account Holder Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Account Number: {self.account_no}")
        print(f"Balance: {self.balance}")
account = bank("Manu Mathew", "manu@123.com", "1234")
account.deposit(1000)
account.withdraw(500)
account.withdraw(600)
account.display()
