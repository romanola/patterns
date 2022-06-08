from collections.abc import Iterable, Iterator


class Employee:

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class StaffListIterator(Iterator):

    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class StaffList(Iterable):

    def __init__(self, collection):
        self._collection = collection

    def __iter__(self) -> StaffListIterator:
        return StaffListIterator(self._collection)

    def get_reverse_iterator(self) -> StaffListIterator:
        return StaffListIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


def main():
    zak = Employee('Zak')
    sarah = Employee('Sarah')
    anna = Employee('Anna')

    staff_list = StaffList((zak, sarah, anna))
    staff_iter = iter(staff_list)

    print(list(staff_iter))


if __name__ == '__main__':
    main()
