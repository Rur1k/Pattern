class Subject:
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        #if self._observers.isdisjoint(observer):
        self._observers.remove(observer)
        #else:
        #    print('Данный подписчик не найден')

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class ObserverBase:
    def update(self, data):
        pass


class Observer(ObserverBase):
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print('%s: %s' % (self._name, data))


subject = Subject()
subject.attach(Observer('Подписчик 1'))
subject.attach(Observer('Подписчик 2'))
subject.attach(Observer('Подписчик 3'))
subject.set_data('данные для подписчика')

#subject.detach(Observer('Подписчик 3'))
subject.set_data('новые данные для подписчиков')
