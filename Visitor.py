class Visitor:
    def buy(self, car):
        methods = {
            Toyota: self.buy_toyota,
            BMW: self.buy_bmw,
        }
        buy = methods.get(type(car), self.buy_unknown)
        buy(car)

    def buy_toyota(self, car):
        print('Куплена Toyota')

    def buy_bmw(self, car):
        print('Куплена BMW')

    def buy_unknown(self, car):
        print('Данная марка авто отсутвует')

class Car:
    def buy(self, visitor):
        visitor.buy(self)

class Toyota(Car):
    pass

class BMW(Car):
    pass

class Lada(Car):
    pass

visitor = Visitor()

toyota = Toyota()
toyota.buy(visitor)

bmw = BMW()
bmw.buy(visitor)

lada = Lada()
lada.buy(visitor)
