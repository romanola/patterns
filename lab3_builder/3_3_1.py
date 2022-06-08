from abc import abstractmethod, ABCMeta


class Pizza:
    pass


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_dough(self, dough):
        pass

    @abstractmethod
    def set_dough_kind(self, kind):
        pass

    @abstractmethod
    def set_supp(self, kind, number):
        pass

    @abstractmethod
    def get_pizza(self):
        pass


class PizzaBuilder(Builder):

    def __init__(self):
        self._pizza = Pizza()

    def reset(self):
        self._pizza = Pizza()

    def set_dough(self, dough):
        pizza = self.get_pizza()
        pizza.dough = dough

    def set_dough_kind(self, kind):
        pizza = self.get_pizza()
        pizza.dough_kind = kind

    def set_supp(self, kind, number):
        pizza = self.get_pizza()
        if 'supplements' not in dir(pizza):
            pizza.supplements = {}
        if kind not in pizza.supplements.keys():
            pizza.supplements[kind] = number
        else:
            pizza.supplements[kind] += number

    def get_pizza(self):
        return self._pizza


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PizzaYolo(metaclass=SingletonMeta):

    def __init__(self):
        self._builder = PizzaBuilder()

    def margherita(self):
        self._builder.reset()
        self._builder.set_dough('тонке')
        self._builder.set_dough_kind('борошно')
        self._builder.set_supp('сир', 100)
        self._builder.set_supp('томат', 6)
        self._builder.set_supp('часник', 1)
        return self._builder.get_pizza()

    def peperoni(self):
        self._builder.reset()
        self._builder.set_dough('товсте')
        self._builder.set_dough_kind('борошно')
        self._builder.set_supp('сир', 300)
        self._builder.set_supp('пепероні', 250)
        self._builder.set_supp('томатне пюре', 200)
        return self._builder.get_pizza()


def main():
    py = PizzaYolo()
    py_check_st = PizzaYolo()
    print(py is py_check_st)  # check singleton

    peperoni = py.peperoni()
    margherita = py.margherita()
    print(f'Peperoni: {peperoni.dough=}, {peperoni.dough_kind=}, {peperoni.supplements=}')
    print(f'Margherita: {margherita.dough=}, {margherita.dough_kind=}, {margherita.supplements=}')


if __name__ == '__main__':
    main()
