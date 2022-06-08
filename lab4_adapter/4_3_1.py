from __future__ import annotations

from abc import ABCMeta, abstractmethod


class Vehicle:

    def __init__(self, age=0, model='default', damage=.0, mileage=0):
        self._age = age
        self._model = model
        self._damage = damage  # [0, 1]: 0 - min, 1 - max
        self._mileage = mileage

    def get_age(self):
        return self._age

    def get_model(self):
        return self._model

    def get_damage(self):
        return self._damage

    def get_mileage(self):
        return self._mileage


class Car(Vehicle):

    def __init__(self, age, model, damage):
        super().__init__(age=age, model=model, damage=damage, mileage=0)


class Truck(Vehicle):

    def __init__(self, age, mileage):
        super().__init__(age=age, model='truck', damage=0, mileage=mileage)


class VehicleCalculator(metaclass=ABCMeta):

    @abstractmethod
    def set_vehicle(self, vehicle):
        pass

    @abstractmethod
    def calculate_price(self):
        pass


class CarCalculator(VehicleCalculator):
    _average_car_price = 6000
    marks_to_price = {'Ford': 3000, 'Audi': 5000, 'Bmw': 7000, "Tesla": 10000}

    def __init__(self):
        self._vehicle: Vehicle | None = None

    def get_retail_price(self) -> int:
        assert self._vehicle is not None, "You forgot to set a vehicle"

        if self._vehicle.get_model() in CarCalculator.marks_to_price.keys():
            return CarCalculator.marks_to_price.get(self._vehicle.get_model())
        return CarCalculator._average_car_price

    def set_vehicle(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def calculate_price(self):
        assert self._vehicle is not None, "You forgot to set a vehicle"
        price = self._vehicle.get_damage() * max([self.get_retail_price() - self._vehicle.get_age() * 100, 0])
        return f'{price} USD'


class TruckCalculator(VehicleCalculator):
    _average_price = 10000

    def __init__(self):
        self._vehicle: Vehicle | None = None

    def set_vehicle(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def calculate_price(self):
        assert self._vehicle is not None, "You forgot to set a vehicle"
        price = max(
            [TruckCalculator._average_price - self._vehicle.get_age() * 100 - self._vehicle.get_mileage() / 100, 0]
        )
        return f'{price} USD'


class Auto:

    def __init__(self, age: int, model: str, damaged: bool):
        self._age = age
        self._model = model
        self._damaged = damaged

    def get_age(self):
        return self._age

    def get_model(self):
        return self._model

    def get_damaged(self):
        return self._damaged


class Custom:

    _ex_rate = 29.5
    _tax_per = 0.2

    def __init__(self):
        self._auto: Auto | None = None
        self._vehicle_calc: CarCalculator | TruckCalculator | None = None

    def set_auto(self, auto: Auto):
        self._auto = auto
        if auto.get_model() == 'truck':
            self._vehicle_calc = TruckCalculator()
            self._vehicle_calc.set_vehicle(Truck(auto.get_age(), 1000))
        else:
            self._vehicle_calc = CarCalculator()
            damage = 0 if not auto.get_damaged() else 0.5
            self._vehicle_calc.set_vehicle(Car(auto.get_age(), auto.get_model(), damage))

    def _get_us_price(self) -> float:
        price_us = float(self._vehicle_calc.calculate_price().split()[0])
        return price_us

    def vehicle_price(self):
        price = Custom._usd_to_uah(self._get_us_price())
        tax = self.tax()
        return f'{price + tax} UAH'

    def tax(self):
        price_us = self._get_us_price()
        return Custom._usd_to_uah(price_us * Custom._tax_per)

    @staticmethod
    def _usd_to_uah(usd):
        return usd * Custom._ex_rate


def main():
    my_auto = Auto(5, 'Audi', True)
    calc = Custom()
    calc.set_auto(my_auto)
    print(calc.vehicle_price())

    my_truck = Auto(10, 'truck', False)
    calc.set_auto(my_truck)
    print(calc.vehicle_price())


if __name__ == '__main__':
    main()
