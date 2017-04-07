class BankAccount:
    def __init__(self, bal, name): #<--- have to put
        self.balance = bal
        self.name = name
    def greet_balance(self):
        print('Hello {}, your balance is {}.'.format(self.name, self.balance))

    def withdrawal(self, amount):
        if self.balance - amount - self.padding >= 0:
            self.balance -= amount
            print('You have withdrawn ${}, your balance is now ${}.'.format(amount, self.balance))
        else:
            print('You don\'t have enough money dude')
    def deposit(self, amount):
        self.balance += amount
        print('You deposit ${}'.format(amount))

class BankAccountRestricted(BankAccount):
    def __init__(self, bal, name, padding):
        BankAccount.__init__(self, bal, name)
        self.padding = padding


chris = BankAccount(150, 'Chris')
katie = BankAccount(2000, 'Katie')



#self refers to the self being created. have to start with dunder init dunder
#dunder = double underscore"""

chris.greet_balance()
#katie.greet_balance()
chris.withdrawal(30)


#inheritance is easier than it seems.
