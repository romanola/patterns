class Runway:

    def __init__(self):
        self._is_available = True

    @property
    def is_available(self) -> bool:
        return self._is_available

    def set_is_available(self, is_available: bool):
        self._is_available = is_available


class Plane:

    def __init__(self, plane_id: int):
        self._id = plane_id
        self._is_in_the_air = False
        self._runway = Runway()
        self._mediator = Mediator()
        self._mediator.planes_on_ground.add(self)

    def take_off(self):
        self._mediator.take_off(self)

    @property
    def is_in_the_air(self):
        return self._is_in_the_air

    @property
    def id(self):
        return self._id

    def set_is_in_the_air(self, is_in_the_air: bool):
        self._is_in_the_air = is_in_the_air

    @property
    def runway(self):
        return self._runway


class PlanesInFlight:

    def __init__(self):
        self._planes = []

    def add(self, plane: Plane):
        self._planes.append(plane)

    def remove(self, plane: Plane):
        # assert plane in self._planes, f'Plane {plane} is not in flight'
        if plane in self._planes:
            self._planes.remove(plane)


class PlanesOnGround:

    def __init__(self):
        self._planes = []

    def add(self, plane: Plane):
        self._planes.append(plane)

    def remove(self, plane: Plane):
        # assert plane in self._planes, f'Plane {plane} is not on ground'
        if plane in self._planes:
            self._planes.remove(plane)


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Mediator(metaclass=SingletonMeta):

    def __init__(self):
        self._planes_in_flight = PlanesInFlight()
        self._planes_on_ground = PlanesOnGround()

    def take_off(self, plane: Plane):
        if not plane.is_in_the_air and plane.runway.is_available:
            print(F"Plane {plane.id} is taking off...")
            self._planes_on_ground.remove(plane)
            self._planes_in_flight.add(plane)
            plane.set_is_in_the_air(True)
            plane.runway.set_is_available(False)

    @property
    def planes_in_flight(self):
        return self._planes_in_flight

    @property
    def planes_on_ground(self):
        return self._planes_on_ground


def main():
    plane1 = Plane(1)
    plane2 = Plane(2)
    plane3 = Plane(3)
    plane1.take_off()
    plane2.take_off()

    # print(plane1._mediator.planes_in_flight._planes)


if __name__ == '__main__':
    main()
