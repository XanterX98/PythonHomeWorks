"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02 import base, engine


class Car(base.Vehicle):
    engine: engine.Engine

    def set_engine(self, new_engine):
        self.engine = new_engine
