class Shopping:
    def shop(self):
        print("Welcome to my shop")

class Buying:
    def buy(self):
        print("I am buying this product")

class Checkout:
    def checkout(self):
        print("Would you like to pay using VISA or Cash?")


class Final_Checkpoint():
    def __init__(self) :
        self.shop = Shopping()
        self.buy = Buying()
        self.checkout=Checkout()

    def startPaying(self):
        self.shop.shop()
        self.buy.buy()
        self.checkout.checkout()

if __name__ == "__main__": 
    obj = Final_Checkpoint()
    obj.startPaying()






    