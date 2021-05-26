class IteratorBase:

    def first(self):
        pass

    def last(self):
        pass

    def next(self):
        pass

    def prev(self):
        pass

    def current_item(self):
        pass

    def is_done(self, index):
        pass

    def get_item(self, index):
        pass


class Iterator(IteratorBase):
    def __init__(self, list_=None):
        self._list = list_ or []
        self._current = 0

    def first(self):
        return self._list[0]

    def last(self):
        return self._list[-1]

    def current_item(self):
        return self._list[self._current]

    def is_done(self, index):
        last_index = len(self._list) - 1
        return 0 <= index <= last_index

    def next(self):
        self._current += 1
        if not self.is_done(self._current):
            self._current = 0
        return self.current_item()

    def prev(self):
        self._current -= 1
        if not self.is_done(self._current):
            self._current = len(self._list) - 1
        return self.current_item()

    def get_item(self, index):
        if not self.is_done(index):
            raise IndexError('Нет элемента с индексом: %d' % index)
        return self._list[index]


it = Iterator(['один', 'два', 'три', 'четыри', 'пять'])

for i in range(5):
    print(it.prev())

for i in range(5):
    print(it.next())