from enum import Enum
from random import randint, choice
from typing import Dict


class Material(Enum):
    Steel = "Steel"
    Alloy = "Alloy"


class Fuel(Enum):
    Petrol = "Petrol"
    Diesel = "Diesel"
    Electric = "Electric"


class CarColor(Enum):
    White = "white"
    Black = "Black"
    Red = "Red"
    Grey = "Grey"


class CarType(Enum):
    Sedan = "Sedan"
    Hatchback = "Hatchback"
    SUV = "SUV"


class Wheel:

    def __init__(self, diameter):
        self.material = Material.Steel
        self.diameter = diameter

    def __str__(self):
        return f'Wheel(material={self.material}, diameter={self.diameter})'


class WheelFactory:

    def __init__(self):
        self._wheels: Dict[int, Wheel] = {}

    @staticmethod
    def _get_key(diameter, material: Material = Material.Steel) -> int:
        return hash(f'{material}_{diameter}')

    def get_wheel(self, diameter: int, material: Material = Material.Steel) -> Wheel:
        key = self._get_key(diameter)
        if key in self._wheels.keys():
            return self._wheels.get(key)
        wheel = Wheel(diameter)
        self._wheels[key] = wheel
        return wheel


class Engine:

    def __init__(self, power: int, fuel: Fuel):
        self.power = power
        self.fuel = fuel

    def __str__(self):
        return f'Engine(power={self.power}, fuel={self.fuel})'


class EngineFactory:

    def __init__(self):
        self._engines: Dict[int, Engine] = {}

    @staticmethod
    def _get_key(power, fuel: Fuel) -> int:
        return hash(f'{power}_{fuel}')

    def get_engine(self, power: int, fuel: Fuel) -> Engine:
        key = self._get_key(power, fuel)
        if key in self._engines.keys():
            return self._engines.get(key)
        engine = Engine(power, fuel)
        self._engines[key] = engine
        return engine


class Car:

    def __init__(self, car_type: CarType, car_color: CarColor, engine: Engine, wheel: Wheel):
        self.car_type = car_type
        self.car_color = car_color
        self.engine = engine
        self.wheel = wheel

    def show_info(self):
        print(f"Car:\ntype={self.car_type},\ncolor={self.car_color},\nengine={self.engine},\nwheel={self.wheel}")


class CarBuilder:

    def __init__(self):
        self._car_type: CarType | None = None
        self._car_color: CarColor | None = None
        self._engine: Engine | None = None
        self._wheel: Wheel | None = None
        self._wheel_factory = WheelFactory()
        self._engine_factory = EngineFactory()
        self.reset()

    def reset(self):
        self._car_type = CarType.Sedan
        self._car_color = CarColor.White
        self._engine = self._engine_factory.get_engine(105, Fuel.Petrol)
        self._wheel = self._wheel_factory.get_wheel(17)
        return self

    def set_type(self, car_type: CarType):
        self._car_type = car_type
        return self

    def set_color(self, color: CarColor):
        self._car_color = color
        return self

    def set_wheel(self, wheel: Wheel):
        self._wheel = wheel
        return self

    def set_engine(self, engine: Engine):
        self._engine = engine
        return self

    def build(self) -> Car:
        assert all((self._car_type, self._car_color, self._engine, self._wheel)), "Invalid args"
        return Car(self._car_type, self._car_color, self._engine, self._wheel)


class CarSimulator:

    def __init__(self):
        self._vehicles = []
        self._car_builder = CarBuilder()
        self._wheel_factory = WheelFactory()
        self._engine_factory = EngineFactory()

    def create_rand_car(self):
        car_type = choice(list(CarType))
        fuel = choice(list(Fuel))
        color = choice(list(CarColor))
        diameter = randint(17, 20)
        power = randint(11, 15) * 10

        car = self._car_builder\
            .reset()\
            .set_type(car_type)\
            .set_color(color)\
            .set_engine(self._engine_factory.get_engine(power, fuel))\
            .set_wheel(self._wheel_factory.get_wheel(diameter))\
            .build()
        print(f"Creating {car}")
        car.show_info()
        self._vehicles.append(car)

    @property
    def vehicles(self):
        return self._vehicles


def main():
    cs = CarSimulator()
    for _ in range(15):
        cs.create_rand_car()

    # security breached (for view only)
    print(F'Results:\ntotal car number: {len(cs.vehicles)}\n'
          F'total wheel number: {len(cs._wheel_factory._wheels.keys())}\n'
          F'total engine number: {len(cs._engine_factory._engines.keys())}')


if __name__ == '__main__':
    main()
