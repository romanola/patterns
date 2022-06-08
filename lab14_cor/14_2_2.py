from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Request:
    def __init__(self, a: int, b: int, sym: str):
        """
        :param a: first digit
        :param b: second digit
        :param sym: + - / * (str type)
        """
        self._a = a
        self._b = b
        self._sym = sym

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def sym(self):
        return self._sym

    def __str__(self):
        return f'{self.a} {self.sym} {self.b}'

    def __repr__(self):
        return f'{self.a} {self.sym} {self.b}'


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Request):
        if self._next_handler:
            return self._next_handler.handle(request)


class AdditionHandler(AbstractHandler):
    def handle(self, request: Request) -> str:
        if request.sym == '+':
            return f'{request.a + request.b}'
        else:
            return super().handle(request)


class SubtractionHandler(AbstractHandler):
    def handle(self, request: Request) -> str:
        if request.sym == '-':
            return f'{request.a - request.b}'
        else:
            return super().handle(request)


class MultiplicationHandler(AbstractHandler):
    def handle(self, request: Request) -> str:
        if request.sym == '*':
            return f'{request.a * request.b}'
        else:
            return super().handle(request)


class DivisionHandler(AbstractHandler):
    def handle(self, request: Request) -> str:
        if request.sym == '/':
            assert request.b != 0, 'Division by zero!'
            return f'{request.a / request.b}'
        else:
            return super().handle(request)


def main():
    add_handler = AdditionHandler()
    sub_handler = SubtractionHandler()
    mul_handler = MultiplicationHandler()
    div_handler = DivisionHandler()

    add_handler.set_next(sub_handler).set_next(mul_handler).set_next(div_handler)

    requests = [
         Request(1, 3, '+'),
         Request(1, 3, '-'),
         Request(2, 5, "*"),
         Request(10, 5, '/'),

         # may raise an error
         # Request(2, 0, '/'),
    ]

    for request in requests:
        print(f'{request} = {add_handler.handle(request)}')


if __name__ == "__main__":
    main()
