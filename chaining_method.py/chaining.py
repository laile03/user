class User: 

    def __init__ (self, name): 
        self.name = name 
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount 
        return self

    def make_withdrawl(self, amount):
        self.amount -= amount 
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount += amount 
        user.amount -= amount 
        self.display_user_balance()
        user.display_user_balance()
        return self 


lai = User('Lai')
quynh = User('Quynh')
lam = User('Lam')


lai.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawl(200).display_user_balance()

quynh.make_deposit(1000).make_deposit(1000).make_withdrawl(500).make_withdrawl(500).display_user_balance()

lam.make_deposit(100).make_withdrawl(30).make_withdrawl(30).make_withdrawl(50).display_user_balance()

lai.transfer_money(300, lam)