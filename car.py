from serviceable import Serviceable
from capulet import CapuletEngine
from sternman import SternmanEngine
from willoughby import WilloughbyEngine
from nubbin import NubbinBattery
from spindler import SpindlerBattery

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    def needs_service():
        return self.engine.needs_service() or self.battery.needs_service()

def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

def create_palindrome(current_date, last_service_date, warning_light_on):
    return Car(SternmanEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))

def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))
