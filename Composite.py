class Unit:
    def info_unit(self):
        pass

class Solder(Unit):
    def info_unit(self):
        return 'Солдат'

class Panzer(Unit):
    def info_unit(self):
        return 'Танк'

class Ship(Unit):
    def info_unit(self):
        return 'Судно'

class Plane(Unit):
    def info_unit(self):
        return 'Самолет'

class Army(Unit):
    def __init__(self):
        self._myarmy = []

    def info_unit(self):
        print("Моя армия: ")
        for unit in self._myarmy:
            print(unit.info_unit())

    def add_unit(self, unit: Unit):
        self._myarmy.append(unit)


army = Army()

army.add_unit(Solder())
army.add_unit(Panzer())
army.add_unit(Ship())
army.add_unit(Plane())
army.info_unit()



