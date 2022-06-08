from typing import Iterable
from abc import ABC, abstractmethod


class Lamp:

    def __init__(self, name: str = 'default'):
        self._name = name
        self._is_light_on: bool = False

    @property
    def name(self):
        return self._name

    def light_on(self):
        if not self._is_light_on:
            print(f'{self.name}: Light is on')
            self._is_light_on = True

    def light_off(self):
        if self._is_light_on:
            print(f'{self.name}: Light is off')
            self._is_light_on = False


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class TurnOn(Command):

    def __init__(self, lamp: Lamp):
        self._payload: callable = lamp.light_on

    def execute(self) -> None:
        self._payload()


class TurnOff(Command):

    def __init__(self, lamp: Lamp):
        self._payload: callable = lamp.light_off

    def execute(self) -> None:
        self._payload()


class Controller:

    def __init__(self, lamp: Lamp):
        self._on = TurnOn(lamp)
        self._off = TurnOff(lamp)

    def on(self):
        self._on.execute()

    def off(self):
        self._off.execute()


class UniversalController:

    def __init__(self, lamps: Iterable[Lamp]):
        # self._lamps = lamps
        self._ons = []
        self._offs = []
        for lamp in lamps:
            self._ons.append(TurnOn(lamp))
            self._offs.append(TurnOff(lamp))

    def on(self):
        for controller in self._ons:
            controller.execute()

    def off(self):
        for controller in self._offs:
            controller.execute()


def main():
    lamp1 = Lamp('Lamp #1')
    lamp2 = Lamp('Lamp #2')
    lamp3 = Lamp('Lamp #3')

    universal_controller = UniversalController([lamp1, lamp2, lamp3])
    universal_controller.on()
    universal_controller.off()


if __name__ == '__main__':
    main()
