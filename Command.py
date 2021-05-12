class Car:
    def runCar(self):
        print('Ехать')

    def stopCar(self):
        print('Стоять')

class Command:
    def act(self):
        pass

class CarCommand(Command):
    def __init__(self, CarAct):
        self.CarAct = CarAct

class RunCar(CarCommand):
    def act(self):
        self.CarAct.runCar()

class StopCar(CarCommand):
    def act(self):
        self.CarAct.stopCar()

class Switch:
    def __init__(self, run_base, stop_base):
        self.__run_base = run_base
        self.__stop_base = stop_base

    def run(self):
        self.__run_base.act()

    def stop(self):
        self.__stop_base.act()

car = Car()
switch = Switch(RunCar(car), StopCar(car))

switch.run()
switch.stop()