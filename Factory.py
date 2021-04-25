class Delivery:

    def Road(self, Cargo, typeDelivery):
        return self._get_type_delivery(typeDelivery)

    def _get_type_delivery(self, typeDelivery):
        if typeDelivery == 'Air':
            return self._AirDelivery()
        elif typeDelivery == 'Sea':
            return self._SeaDelivery()
        elif typeDelivery == 'Land':
            return self._LandDelivery()
        else:
            ValueError(typeDelivery)

    def _AirDelivery(self):
        return 'Air Delivery'

    def _SeaDelivery(self):
        return 'Sea Delivery'

    def _LandDelivery(self):
        return 'Land Delivery'

Delivery = Delivery()

print(Delivery.Road('Cargo', 'Sea'))