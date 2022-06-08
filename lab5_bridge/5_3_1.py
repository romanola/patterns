class AbstractBeverage:
    def __init__(self, sugar: int):
        self.sugar = sugar

    def prepare(self) -> None:
        pass

    def drink(self) -> None:
        pass

    def cost(self) -> int:
        pass


class Coffee(AbstractBeverage):

    def prepare(self):

        print('Put some coffee...')

    def cost(self):
        return 10


class BlackCoffee(Coffee):

    def __init__(self, sugar: int, water_volume: int, extra_coffee: bool):
        super().__init__(sugar)
        self.water_volume = water_volume
        self.extra_coffee = extra_coffee

    def drink(self) -> None:
        print('Drink black coffee!')

    def prepare(self):
        super(BlackCoffee, self).prepare()
        if self.extra_coffee:
            print('Put extra coffee...')
        if self.sugar:
            print(f'Put some sugar:\tpieces ...{self.sugar}')


class CoffeeWithMilk(Coffee):

    def __init__(self, sugar: int, milk_volume: int, ):
        super().__init__(sugar)
        self.milk_volume = milk_volume

    def drink(self) -> None:
        print('Drink coffee with milk!')

    def prepare(self):
        super(CoffeeWithMilk, self).prepare()
        print(f'Put some milk :\nml...%{self.milk_volume}')
        if self.sugar:
            print(f'Put some sugar:\tpieces ...{self.sugar}')


class Tea(AbstractBeverage):

    def prepare(self):
        print('Put some tea...')

    def cost(self):
        return 7


class Chocolate(AbstractBeverage):

    def prepare(self):
        print('Put some cacao...')

    def cost(self):
        return 15


class Beverage:
    def bill(self):
        pass


class Cafe:

    def __init__(self, beverage):
        self._beverage = beverage

    def order(self):
        print(f'You ordered {type(self._beverage).__name__} {type(self).__name__}')

    def bill(self):
        self.order()
        self._beverage.prepare()
        self._beverage.drink()
        self._beverage.cost()


class Togo(Cafe):
    pass


class Here(Cafe):
    pass


if __name__ == "__main__":
    my_bev = BlackCoffee(5, 100, True)
    my_bev2 = CoffeeWithMilk(0, 20)
    togo = Togo(my_bev)
    togo.bill()
    here = Here(my_bev2)
    here.bill()
