class Calculator:
    def __init__(self, a=0,b=0):
        self.a = a
        self.b = b

    def addition(self):
            return self.a + self.b 

    def subtraction(self):
            return self.a - self.b 

    def multiplication(self):
            return self.a * self.b 

    def division(self):
        return self.a / self.b 

c = Calculator(2,2)
print(c.addition())
print(c.subtraction())
print(c.multiplication())
print(c.division())

