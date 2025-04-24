class Bankaccount(object):
    interest_rate=3  #class variable- will execute in instance method
    def __init__(self,acc_holder,balance=0):
        self.acc_holder=acc_holder
        self.balance=balance
    def deposit(self,amount):  #object specific method 
        self.balance+=amount
        print(f"Deposited INR {amount} \ncurrent BALANCE: {self.balance}")
    def withdraw(self,amount):  #object specific method
        if amount>self.balance:
            print("Insuffiecient balance")
        else:
            self.balance-=amount
            print(f"Debited  INR {amount} \ncurrent BALANCE:{self.balance}")
    def set_interest_rate(cls,newrate): # classmethod- run class variable using cls. 
        cls.interest_rate= newrate  #cls access the class variable
        print(f"updated new interest rate:{cls.interest_rate}")
    set_interest_rate=classmethod(set_interest_rate)
    def validate_account(account_number):
        valid = False
        if len(str(account_number)) ==  12:
            if str(account_number).isdigit():
                valid = True
        return valid
    
    validate_account_number = staticmethod(validate_account)
if __name__ == "__main__":

    acc1 = Bankaccount("Anil", 1000)

    if(Bankaccount.validate_account('234501010098')):
        acc1.deposit(500)
        acc1.withdraw(200)
        Bankaccount.set_interest_rate(6)