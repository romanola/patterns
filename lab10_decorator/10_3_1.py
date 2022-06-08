from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):

    @abstractmethod
    def operation(self) -> str:
        pass


class PrintableString(Component):

    def __init__(self, base):
        self.base = base

    def operation(self) -> str:
        return self.base


class Decorator(Component):

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class PostComaDecorator(Decorator):
    def operation(self) -> str:
        return self.component.operation() + ','


class PostEndlDecorator(Decorator):
    def operation(self) -> str:
        return self.component.operation() + '.'


class PostExclaimDecorator(Decorator):
    def operation(self) -> str:
        return self.component.operation() + '!'


class PostWordDecorator(Decorator):

    def __init__(self, component: Component, word):
        super().__init__(component)
        self.word = word

    def operation(self) -> str:
        return self.component.operation() + self.word


class PreWordDecorator(Decorator):

    def __init__(self, component: Component, word):
        super().__init__(component)
        self.word = word

    def operation(self) -> str:
        return self.word + self.component.operation()


if __name__ == "__main__":
    res = PrintableString('')
    res = PostComaDecorator(res)
    res = PostWordDecorator(res, ' Wold')
    res = PreWordDecorator(res, 'Hello')
    print(res.operation())
