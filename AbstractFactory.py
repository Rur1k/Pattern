class AbstractFactory:
    def CreateCar(self):
        pass

    def ProducingCountry(self):
        pass

class Car:
    def __init__(self, brand):
        self._brand = brand

    def __str__(self):
        return self._brand

class Country:
    def __init__(self, country):
        self._country = country

    def __str__(self):
        return self._country

class FactoryOne(AbstractFactory):
    def CreateCar(self):
        return Car('Жигуль')

    def ProducingCountry(self):
        return Country('СССР')


class FactoryTwo(AbstractFactory):
    def CreateCar(self):
        return Car('Toyota')

    def ProducingCountry(self):
        return Country('Япония')

def GetFactory(choise):
    if choise == 1:
        return FactoryOne()
    elif choise == 2:
        return FactoryTwo()

factory = GetFactory(1)
print(factory.CreateCar())
print(factory.ProducingCountry())

factory = GetFactory(2)
print(factory.CreateCar())
print(factory.ProducingCountry())
