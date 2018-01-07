from abc import ABCMeta,abstractmethod
class You:
    def __init__(self):
        print('You:: Lets buy the Denim shirt')
        self.debitCard = DebitCard()
        self.isPurchased = None
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
    def __del__(self):
        if self.isPurchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :(")

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def __getAccount(self):
        self.account = self.card
        return self.account
    def __hasFunds(self):
        print("Bank:: Checking if Account",self.__getAccount(),"has enough funds")
        return True
    def setCard(self,card):
        self.card = card
    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False

class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = input('Proxy:: Punch is Card Number:')
        self.bank.setCard(card)
        return self.bank.do_pay()


you = You()

you.make_payment()

#感觉这个例子，按我自己来说我要设计肯定是垂直的瀑布式设计，从银行一头或者从用户一头，payment不会单独独立出来
#很奇怪这些设计模式的是怎么想的，可能是是吧业务铺开选着设定接口的