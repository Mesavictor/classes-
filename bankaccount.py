class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
    def deposit(self):
        print("Amount deposited=KSH",deposited)
    def withdraw(self):
        print("Amount withdrawn=KSH",withdrawn)
    def check_balance(self):
        
        print("Balance=KSH",balance)
    def customer_details(self):
        print("name:",customer_name)
        print("account number:",account_number)
        print("date of opening:",date_of_opening)
account_number='67889990453'
deposited=100000
withdrawn=20000
balance=deposited-withdrawn
date_of_opening='12/4/2012'
customer_name='John Macharia'
dt=BankAccount(account_number,balance,date_of_opening,customer_name)
dt.customer_details()
dt.deposit()
dt.withdraw()
dt.check_balance()
