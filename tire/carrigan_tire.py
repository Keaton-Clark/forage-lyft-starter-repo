from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    def needs_service(self):
        return (.9 <= self.tire_wear[0] or .9 <= self.tire_wear[1] or .9 <= self.tire_wear[2] or .9 <= self.tire_wear[3])

