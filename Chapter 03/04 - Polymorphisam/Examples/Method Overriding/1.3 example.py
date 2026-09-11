class Payment:
    def pay(self):
        print("Processing Payment")


class CreditCard(Payment):
    def pay(self):
        print("Payment using Credit Card")


class JazzCash(Payment):
    def pay(self):
        print("Payment using JazzCash")


class EasyPaisa(Payment):
    def pay(self):
        print("Payment using EasyPaisa")


card = CreditCard()
jazz = JazzCash()
easy = EasyPaisa()

card.pay()
jazz.pay()
easy.pay()