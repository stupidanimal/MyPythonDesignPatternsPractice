from abc import ABCMeta,abstractmethod

class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None
    def attach(self,subscriber):
        self.__subscribers.append(subscriber)
    def detach(self):
        return self.__subscribers.pop()
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    def notifySubscribers(self):
        for x in self.__subscribers:
            x.update()
    def addNews(self,news):
        self.__latestNews = news
    def getNews(self):
        return "Got News:",self.__latestNews

class subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

class SMSSubscriber:
    def __init__(self,publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__,self.publisher.getNews())

class EmailSubscriber:
    def __init__(self,publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__,self.publisher.getNews())
    
class AnyOtherSubscriber:
    def __init__(self,publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__,self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for Subscribers in [SMSSubscriber,EmailSubscriber,AnyOtherSubscriber]: #这个我就没看懂为什么没继承，也能默认new
        Subscribers(news_publisher)
    print('\nSubscribers:',news_publisher.subscribers())

    news_publisher.addNews('hello world')
    news_publisher.notifySubscribers()

    print('\nDetached:',type(news_publisher.detach()).__name__)
    print('\nSubscribers:',news_publisher.subscribers())

    news_publisher.addNews('My second news!')
    news_publisher.notifySubscribers()




#很奇怪接口没有直接继承，用在了发布者身上