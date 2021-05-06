class Whell:
    def CreateWell(self):
        print('Колеса установлены')

class BodyCar:
    def CreateBodyCar(self):
        print('Кузов автомобиля собран')

class Engine:
    def CreateEngine(self):
        print('Двигатель установлен')

class Salon:
    def CreateSalon(self):
        print('Салон установлен')

class Car:
    def NewCar(self):
        newBody = BodyCar()
        newWhell = Whell()
        newEngine = Engine()
        newSalon = Salon()

        newBody.CreateBodyCar()
        newWhell.CreateWell()
        newEngine.CreateEngine()
        newSalon.CreateSalon()

        return 'Новый автомобиль собран'

NewCar = Car()
print(NewCar.NewCar())