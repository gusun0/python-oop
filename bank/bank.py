class User:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("Personal details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance has been updated: ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds, Balance Available: $", self.balance)
        else:
            self.balance = self.balance - amount
            print("Account balance has been updated: $", self.balance)

    def view_balance(self):
        self.show_user_details()
        print("Account balance has been updated: $", self.balance)









Johan = Bank('Johan', 20,'male')
Johan.show_user_details()
Johan.deposit(400)
Johan.withdraw(100)
Johan.withdraw(300)
Johan.view_balance()


