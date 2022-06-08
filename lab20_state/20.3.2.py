from __future__ import annotations
from abc import ABC, abstractmethod


class Fan:
    _state: State = None

    def __init__(self):
        self.set_state(LowState())

    def set_state(self, state):
        self._state = state
        self._state.fan = self

    def get_state(self):
        return self._state

    def turn_up(self):
        self.get_state().turn_up()

    def turn_dowm(self):
        self.get_state().turn_down()


class State(ABC):

    @property
    def fan(self) -> Fan:
        return self._fan

    @fan.setter
    def fan(self, fan: Fan) -> None:
        self._fan = fan

    @abstractmethod
    def turn_up(self):
        pass

    @abstractmethod
    def turn_down(self):
        pass


class LowState(State):
    def turn_up(self):
        self.fan.set_state(MediumState())
        print("Fan is on medium")

    def turn_down(self):
        pass


class MediumState(State):
    def turn_up(self):
        self.fan.set_state(HighState())
        print("Fan is on high")

    def turn_down(self):
        self.fan.set_state(LowState())
        print("Fan is on low")


class HighState(State):
    def turn_up(self):
        pass

    def turn_down(self):
        self.fan.set_state(MediumState())
        print("Fan is on medium")


if __name__ == '__main__':
    fan = Fan()
    fan.turn_up()
    fan.turn_up()
    fan.turn_dowm()
    fan.turn_dowm()
    fan.turn_up()