from car_factory import CarFactory
from datetime import datetime
from utils import add_years_to_date
from random import randint as rand

def test_all():
    test_calliope()
    test_glissade()
    test_palindrome()
    test_rorschach()
    test_thovex()

def test_calliope():
    print("----------------------------------------------")
    print("Testing Calliope expecting not to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -1)
    current_mileage = rand(100000, 1000000)
    last_service_mileage = current_mileage - 100

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast service date:\t", last_service_date,
            "\nCurrent mileage:\t", current_mileage,
            "\nLast service mileage:\t", last_service_mileage)

    car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    print("Needs service:\t\t", car.needs_service())

    print("----------------------------------------------")
    print("Testing Calliope expecting to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -10)
    current_mileage = rand(100000, 1000000)
    last_service_mileage = current_mileage - 100000

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast service date:\t", last_service_date,
            "\nCurrent mileage:\t", current_mileage,
            "\nLast service mileage:\t", last_service_mileage)

    car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    print("Needs service:\t\t", car.needs_service())

def test_glissade():
    print("----------------------------------------------")
    print("Testing Glissade expecting not to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -1)
    current_mileage = rand(100000, 1000000)
    last_service_mileage = current_mileage - 100

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast service date:\t", last_service_date,
            "\nCurrent mileage:\t", current_mileage,
            "\nLast service mileage:\t", last_service_mileage)

    car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    print("Needs service:\t\t", car.needs_service())

    print("----------------------------------------------")
    print("Testing Glissade expecting to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -10)
    current_mileage = rand(100000, 1000000)
    last_service_mileage = current_mileage - 100000

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast service date:\t", last_service_date,
            "\nCurrent mileage:\t", current_mileage,
            "\nLast service mileage:\t", last_service_mileage)

    car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    print("Needs service:\t\t", car.needs_service())

def test_palindrome():
    print("----------------------------------------------")
    print("Testing Palindrome expecting not to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -1)
    warning_light_is_on = False

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast servcice date:\t", last_service_date,
            "\nWarning light is on:\t", warning_light_is_on)

    car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
    print("Needs service:\t\t", car.needs_service())

    print("----------------------------------------------")
    print("Testing Palindrome expecting to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -10)
    warning_light_is_on = True

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast servcice date:\t", last_service_date,
            "\nWarning light is on:\t", warning_light_is_on)

    car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
    print("Needs service:\t\t", car.needs_service())

def test_rorschach():
    print("----------------------------------------------")
    print("Testing Rorschach expecting not to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -1)
    current_mileage = rand(100000, 1000000)
    last_service_mileage = current_mileage - 100

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast service date:\t", last_service_date,
            "\nCurrent mileage:\t", current_mileage,
            "\nLast service mileage:\t", last_service_mileage)

    car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    print("Needs service:\t\t", car.needs_service())

    print("----------------------------------------------")
    print("Testing Rorschach expecting to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -10)
    current_mileage = rand(100000, 1000000)
    last_service_mileage = current_mileage - 100000

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast service date:\t", last_service_date,
            "\nCurrent mileage:\t", current_mileage,
            "\nLast service mileage:\t", last_service_mileage)

    car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    print("Needs service:\t\t", car.needs_service())

def test_thovex():
    print("----------------------------------------------")
    print("Testing Thovex expecting not to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -1)
    current_mileage = rand(100000, 1000000)
    last_service_mileage = current_mileage - 100

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast service date:\t", last_service_date,
            "\nCurrent mileage:\t", current_mileage,
            "\nLast service mileage:\t", last_service_mileage)

    car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
    print("Needs service:\t\t", car.needs_service())

    print("----------------------------------------------")
    print("Testing Thovex expecting to need service")
    current_date = datetime.now()
    last_service_date = add_years_to_date(current_date, -10)
    current_mileage = rand(100000, 1000000)
    last_service_mileage = current_mileage - 50000

    print("Creating with values:\nCurrent date:\t\t", current_date,
            "\nLast service date:\t", last_service_date,
            "\nCurrent mileage:\t", current_mileage,
            "\nLast service mileage:\t", last_service_mileage)

    car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
    print("Needs service:\t\t", car.needs_service())
