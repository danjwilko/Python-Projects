class Employee:
    def __init__(self, first, last, pay):
        self.first = first.title()
        self.last = last.title()
        self.pay = pay

    def give_raise(self, amount = 5000):
        self.pay = self.pay + amount

