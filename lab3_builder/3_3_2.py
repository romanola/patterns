from abc import ABCMeta, abstractmethod


class String:
    pass


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def get_string(self):
        pass

    @abstractmethod
    def push_left(self, chars):
        pass

    @abstractmethod
    def push_right(self, chars):
        pass

    @abstractmethod
    def push(self, chars, index):
        pass


class StringBuilder(Builder):

    def __init__(self):
        self._string = String()

    def reset(self):
        self._string = String()

    def get_string(self):
        """
        :return: Повертає рядок якщо існує, створює порожній інакше
        """
        if 'item' not in dir(self._string):
            self._string.item = ''
        return self._string.item

    def push_left(self, chars):
        cur = self.get_string()
        self._string.item = chars + cur

    def push_right(self, chars):
        cur = self.get_string()
        self._string.item = cur + chars

    def push(self, chars, index):
        cur = self.get_string()
        assert 0 <= index <= len(cur), 'Invalid index'
        self._string.item = cur[:index] + chars + cur[index:]

    def __str__(self):
        return self.get_string()


if __name__ == '__main__':
    sb = StringBuilder()
    sb.push_left('left')
    print(sb)
    sb.push_right('right')
    print(sb)
    sb.push(' middle ', 4)
    print(sb)
