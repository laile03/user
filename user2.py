class User: 

    def __init__ (self, name): 
        self.name = name 
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount 

    def make_withdrawl(self, amount):
        self.amount -= amount 

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount += amount 
        user.amount -= amount 
        self.display_user_balance()
        user.display_user_balance()



lai = User('Lai')
quynh = User('Quynh')
lam = User('Lam')


lai.make_deposit(200)
lai.make_deposit(200)
lai.make_deposit(200)
lai.make_withdrawl(200)
lai.display_user_balance()

quynh.make_deposit(1000)
quynh.make_deposit(1000)
quynh.make_withdrawl(500)
quynh.make_withdrawl(500)
quynh.display_user_balance()

lam.make_deposit(100)
lam.make_withdrawl(30)
lam.make_withdrawl(30)
lam.make_withdrawl(50)
lam.display_user_balance()

lai.transfer_money(300, lam)