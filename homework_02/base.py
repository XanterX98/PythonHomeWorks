from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True

        if not self.started and self.fuel <= 0:
            raise exceptions.LowFuelError()

    def move(self, distance):
        if self.fuel_consumption * distance > self.fuel:
            raise exceptions.NotEnoughFuel()
        else:
            self.fuel -= self.fuel_consumption * distance
