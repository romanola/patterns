from __future__ import annotations

from abc import ABCMeta, abstractmethod
from PIL import Image


class DisplayObject(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass


class ImageFile:

    def __init__(self):
        self._image: Image = None

    @abstractmethod
    def display(self):
        print("Displaying image.")
        self._image.show()

    def load(self, path: str):
        print(F"Loading image {path} ...")
        self._image = Image.open(path)


class ImageProxy(DisplayObject):

    def __init__(self):
        self._image: Image = None
        self._path: str | None = None

    def display(self):
        print("Displaying image.")
        self._image = Image.open(self._path)
        self._image.show()

    def load(self, path: str):
        print(F"Loading image {path} ...")
        self._path = path


def main():
    images = [
        'resources/image.jpg',
        'resources/image.png',
        'resources/image3.jpeg',
        'resources/image4.jpeg',
        'resources/image5.jpeg',
        'resources/image6.jpeg',
        'resources/image7.jpeg',
        'resources/image8.jpeg',
        'resources/image9.jpeg',
        'resources/image10.jpeg',
    ]

    im_pr = ImageProxy()

    for path in images:
        im_pr.load(path)
        im_pr.display()


if __name__ == '__main__':
    main()
