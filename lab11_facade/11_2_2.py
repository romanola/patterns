class Accelerator:

    @staticmethod
    def press():
        print("Pressing accelerator down")

    @staticmethod
    def lift():
        print("Lifting accelerator up")


class Clutch:

    @staticmethod
    def press():
        print("Pressing clutch down")

    @staticmethod
    def lift():
        print("Lifting clutch up")


class GearStick:

    def __init__(self):
        self.gear = 0
        self.range = 0, 1, 2, 3, 4, 5  # 0 == R

    def change_gear(self, gear: int):
        print(f"Changing gear to {gear}")
        self.gear = gear


class HandBrake:

    def __init__(self):
        self.is_up = True

    def push_down(self):
        print("Pushing down handbrake")
        self.is_up = False

    def lift_up(self):
        print("Lifting up handbrake")
        self.is_up = True


class Ignition:

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        print("Turning ignition on")
        self.is_on = True

    def turn_off(self):
        print("Turning ignition off")
        self.is_on = False


class Car:

    def __init__(self):
        self._accelerator = Accelerator()
        self._clutch = Clutch()
        self._gear_stick = GearStick()
        self._hand_brake = HandBrake()
        self._ignition = Ignition()

    def _gear_up(self):
        if self._gear_stick.gear + 1 in self._gear_stick.range:
            self._accelerator.lift()
            self._clutch.lift()
            self._gear_stick.change_gear(self._gear_stick.gear + 1)
            self._clutch.press()

    def _gear_down(self):
        if self._gear_stick.gear - 1 in self._gear_stick.range:
            self._accelerator.lift()
            self._clutch.lift()
            self._gear_stick.change_gear(self._gear_stick.gear - 1)
            self._clutch.press()

    def automatic_change_gear(self, gear):
        self._gear_up() if self._gear_stick.gear < gear else self._gear_down()


def main():
    car = Car()
    car.automatic_change_gear(1)
    car.automatic_change_gear(2)
    car.automatic_change_gear(1)


if __name__ == '__main__':
    main()
