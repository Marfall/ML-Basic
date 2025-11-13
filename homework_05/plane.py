from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight = 1000.0, started = False, fuel = 0.0, fuel_consumption = 10.0, max_cargo = 0.0):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = 0.0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_weight):
        new_cargo = self.cargo + cargo_weight
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0.0
        return previous_cargo