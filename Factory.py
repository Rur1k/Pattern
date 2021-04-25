class Delivery:
    def __init__(self, Cargo, TypeDelivery):
        self.__Cargo = Cargo
        self.__TypeDelivery = TypeDelivery

    def AirDelivery(self):
        print('Air Delivery')

    def SeaDelivery(self):
        print('Sea Delivery')

    def LandDelivery(self):
        print('Land Delivery')

    def Road(self):
        if self.__Cargo == "Air cargo":
            Delivery.AirDelivery()
        elif self.__Cargo == 'Sea cargo':
            Delivery.SeaDelivery()
        elif self.__Cargo == 'Land cargo':
            Delivery.LandDelivery()
        else:
            raise Warning('No delivery!!!')


Delivery = Delivery('Land cargo')

Delivery.Road()