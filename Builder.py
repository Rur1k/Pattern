class Builder:
    def build_engine(self):
        pass

    def build_salon(self):
        pass

    def build_body(self):
        pass

    def create_car(self):
        pass


class Car:
    def __init__(self, engine, salon, body):
        self._start = False
        self._engine = engine
        self._salon = salon
        self._body = body

    def on(self):
        self._start = True

    def off(self):
        self._start = False

    def __str__(self):
        start = 'on' if self._start else 'off'
        return 'Car status: %s' % start


class Engine:
    pass

class Salon:
    pass

class Body:
    pass

class CarBuilder(Builder):
    def build_engine(self):
        return Engine()

    def build_salon(self):
        return Salon()

    def build_body(self):
        return Body()

    def create_car(self):
        engine = self.build_engine()
        salon = self.build_salon()
        body = self.build_body()
        return Car(engine, salon, body)


builder = CarBuilder()
car = builder.create_car()
car.on()
print(car)
