from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    def needs_service(self):
        return (3 <= (self.tire_wear[0] + self.tire_wear[1] + self.tire_wear[2] + self.tire_wear[3]))
