class Transport:
    def CreateTransport(self):
        pass

class AirTransport(Transport):
    def CreateTransport(self):
        pass

class SeaTransport(Transport):
    def CreateTransport(self):
        pass

class LandTransport(Transport):
    def CreateTransport(self):
        pass

Transport = Transport()

Car = Transport.CreateTransport()