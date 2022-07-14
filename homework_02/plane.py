"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02 import base, exceptions


class Plane(base.Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if self.cargo + cargo > self.max_cargo:
            raise exceptions.CargoOverload()
        else:
            self.cargo += cargo

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
