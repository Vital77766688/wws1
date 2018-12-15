from abc import ABC, abstractmethod


class Engine:
    def __init__(self):
        self.subscribers = set()


class ObservableEngine(Engine):

    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self, name):
        self.__name = name
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self, name):
        self.__name = name
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)


if __name__ == '__main__':
    engine = ObservableEngine()
    subs1 = ShortNotificationPrinter("subs1")
    subs2 = FullNotificationPrinter("subs2")
    engine.subscribe(subs1)
    engine.subscribe(subs2)
    s = {"title": "qqq", "text": "dqe widjsi ow jwiqiw!"}
    engine.notify(s)
    engine.unsubscribe(subs1)
    s = {"title": "www", "text": "sk owkdnw ow qp wmekw w lwe?"}
    engine.notify(s)
    print("subs1", subs1.achievements)
    print("subs2", subs2.achievements)


