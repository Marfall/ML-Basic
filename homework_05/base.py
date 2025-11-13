from abc import ABC

from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight = 1000.0, started = False, fuel = 0.0, fuel_consumption = 10.0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            return
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError()

    def move(self, distance):
        required_fuel = (distance * self.fuel_consumption) / 100
        if required_fuel <= self.fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel()
