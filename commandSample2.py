from abc import ABCMeta,abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self,stock):
        self.stock = stock
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self,stock):
        self.stock = stock
    def execute(self):
        self.stock.sell()

class StockTrade:
    def buy(self):
        print('You will buy stocks')
    def sell(self):
        print('You will sell stocks')

class Agent:
    def __init__(self):
        self.__orderQueue = []
    def placeOrder(self,order):
        self.__orderQueue.append(order)
        order.execute()

if __name__=='__main__':
    stock = StockTrade()
    buyStockOrder = BuyStockOrder(stock)
    sellStockOrder = SellStockOrder(stock)

    agent = Agent()
    agent.placeOrder(buyStockOrder)
    agent.placeOrder(sellStockOrder)


#莫名感觉这个有点用
#我理解Agent是事物组织器，平时我自己写都用函数封装，这样就不太灵活，如果新添加内容就得写新函数,
#这个直接组织成一个单独的事物类，最后统一调用，比较方便