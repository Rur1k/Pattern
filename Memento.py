class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._memento = None

    def get_memento(self):
        return self._memento

    def set_memento(self, memento):
        self._memento = memento


class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()


originator = Originator()
caretaker = Caretaker()

originator.set_state('on')
print('Cостояние:', originator.get_state())
caretaker.set_memento(originator.save_state())

originator.set_state('off')
print('Изминенное состояния:', originator.get_state())

originator.restore_state(caretaker.get_memento())
print('Восстановление предыдущего состояния:', originator.get_state())