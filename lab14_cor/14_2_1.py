from abc import ABCMeta, abstractmethod
from PIL import Image
from docx import Document
import textract


class Handler(metaclass=ABCMeta):

    @abstractmethod
    def open(self, path):
        pass

    @abstractmethod
    def set_next(self, handler):
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def open(self, path):
        # print(f'-- (LOG) Path: {path}. Handler: {type(self).__name__} --')
        if self._next_handler:
            return self._next_handler.open(path)


class JpgHandler(AbstractHandler):

    def open(self, path):
        ext = path.split('.')[-1]
        if ext == 'jpg':
            Image.open(path).show()
        else:
            super().open(path)


class PngHandler(AbstractHandler):

    def open(self, path):
        ext = path.split('.')[-1]
        if ext == 'png':
            Image.open(path).show()
        else:
            super().open(path)


class DocxHandler(AbstractHandler):

    def open(self, path):
        ext = path.split('.')[-1]
        if ext == 'docx':
            doc = Document(path)

            print('\n'.join([para.text for para in doc.paragraphs]))
        else:
            super().open(path)


class DocHandler(AbstractHandler):

    def open(self, path):
        ext = path.split('.')[-1]
        if ext == 'doc':
            text = textract.process(path)
            text = text.decode("utf-8")

            print(text)
        else:
            super().open(path)


# todo finish all handlers


def main():
    # building chain

    jpg_handler = JpgHandler()
    png_handler = PngHandler()
    docx_handler = DocxHandler()
    doc_handler = DocHandler()

    jpg_handler.set_next(png_handler).set_next(docx_handler).set_next(doc_handler)

    files = [
        "image.jpg",
        "image.png",
        "document.docx",
        # "document.doc",
        # "table.xls",
        # "table.xlsx",
        # "presentation.pptx",
        # "document.pdf",
    ]

    src = 'resources/'

    for file in files:
        path = f'{src}{file}'
        jpg_handler.open(path)


if __name__ == '__main__':
    main()
