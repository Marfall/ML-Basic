from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    def __init__(self, weight=1000.0, started=False, fuel=0.0, fuel_consumption=10.0, engine=None):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine
