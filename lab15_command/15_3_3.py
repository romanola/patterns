from abc import ABC, abstractmethod
from typing import Iterable


class Device(ABC):

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def next_chanel(self):
        pass

    @abstractmethod
    def prev_chanel(self):
        pass


class Television(Device):

    def __init__(self):
        self._is_on = False
        self._volume = 50
        self._chanel = 5

    def on(self):
        if not self._is_on:
            print("Television is on")
            self._is_on = True

    def off(self):
        if self._is_on:
            print("Television is off")
            self._is_on = False

    def volume_up(self):
        if self._is_on:
            self._volume += 1
            print(f'Volume = {self._volume}')

    def volume_down(self):
        if self._is_on:
            self._volume -= 1
            print(f'Volume = {self._volume}')

    def next_chanel(self):
        if self._is_on:
            self._chanel += 1
            print(f'Chanel = {self._chanel}')

    def prev_chanel(self):
        if self._is_on:
            self._chanel -= 1
            print(f'Chanel = {self._chanel}')


class Radio(Device):

    def __init__(self):
        self._is_on = False
        self._volume = 50
        self._station = 85.0

    def on(self):
        if not self._is_on:
            print("Radio is on")
            self._is_on = True

    def off(self):
        if self._is_on:
            print("Radio is off")
            self._is_on = False

    def volume_up(self):
        if self._is_on:
            self._volume += 1
            print(f'Volume = {self._volume}')

    def volume_down(self):
        if self._is_on:
            self._volume -= 1
            print(f'Volume = {self._volume}')

    def next_chanel(self):
        if self._is_on:
            self._station += .1
            print(f'Station = {self._station}')

    def prev_chanel(self):
        if self._is_on:
            self._station -= .1
            print(f'Station = {self._station}')


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class TurnOn(Command):

    def __init__(self, device: Television | Radio):
        self._payload: callable = device.on

    def execute(self) -> None:
        self._payload()


class TurnOff(Command):

    def __init__(self, device: Television | Radio):
        self._payload: callable = device.off

    def execute(self) -> None:
        self._payload()


class VolumeUp(Command):

    def __init__(self, device: Television | Radio):
        self._payload: callable = device.volume_up

    def execute(self) -> None:
        self._payload()


class VolumeDown(Command):

    def __init__(self, device: Television | Radio):
        self._payload: callable = device.volume_down

    def execute(self) -> None:
        self._payload()


class Next(Command):

    def __init__(self, device: Television | Radio):
        self._payload: callable = device.next_chanel

    def execute(self) -> None:
        self._payload()


class Prev(Command):

    def __init__(self, device: Television | Radio):
        self._payload: callable = device.prev_chanel

    def execute(self) -> None:
        self._payload()


class UniversalController:

    def __init__(self, device: Iterable[Television | Radio]):
        self._offs = []
        for device in device:
            self._offs.append(TurnOff(device))

    def off(self):
        for controller in self._offs:
            controller.execute()


def main():
    tv1 = Television()
    tv2 = Television()
    radio = Radio()

    tv1.on()
    tv2.volume_up()
    tv2.on()
    radio.on()
    radio.next_chanel()

    u_controller = UniversalController((tv1, tv2, radio))
    u_controller.off()


if __name__ == '__main__':
    main()
