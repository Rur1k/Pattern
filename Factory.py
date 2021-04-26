class Transport:
    def CreateTransport(self):
        raise NotImplementedError()

class AirTransport(Transport):
    def CreateTransport(self):
        return 'Create air transport'

class SeaTransport(Transport):
    def CreateTransport(self):
        return 'Create sea transport'

class LandTransport(Transport):
    def CreateTransport(self):
        return 'Create land transport'

class Creator:
    def create_transport(self, type_): #фабричный метод с парамметрами.
        raise NotImplementedError()

class MyCreator(Creator):
    def create_transport(self, type_):
        if type_ == 'Air':
            return AirTransport()
        elif type_ == 'Sea':
            return SeaTransport()
        elif type_ == 'Land':
            return LandTransport()
        else:
            raise ValueError()

CreatorTransport = MyCreator()

print(CreatorTransport.create_transport('Air').CreateTransport())
print(CreatorTransport.create_transport('Sea').CreateTransport())
print(CreatorTransport.create_transport('Land').CreateTransport())
