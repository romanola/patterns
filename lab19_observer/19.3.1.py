from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    """
    Subject interface
    Declares methods to manage observers
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach observer to subject
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach observer from subject
        """
        pass

    def notify(self) -> None:
        """
        Notify all observers of an event
        """
        pass


class LineReaderSubject(Subject):
    """
    Subject reads and has a state of the current line of the file
    and notifies observers of state changes
    """
    _line: str = None  # current line of the file
    _line_number: int = None    # current line index
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def read_lines(self) -> None:
        """
        Read lines of the file and notify observers when updating current line
        """

        with open('input01.txt', 'r') as file:
            self._line_number = 0

            while True:
                line = file.readline()
                if not line:
                    break

                self._line = line
                self._line_number += 1
                self.notify()


class Observer(ABC):
    """
    Observer interface
    Declares update method that is used by the subject to notify observers
    """

    @abstractmethod
    def update(self, subject: Subject):
        """
        Get updates from subject
        """
        pass


class LongestFileLineObserver(Observer):
    """
    Observes increasing length of a line
    """
    _longest_line: str = None

    def update(self, subject: Subject) -> None:
        if not self._longest_line:
            self._longest_line = subject._line
            print('\nLongestFileLineObserver: Initial event')
            print(f"{self._longest_line=}")
        else:
            if len(self._longest_line) < len(subject._line):
                print('\nLongestFileLineObserver: Reacted to the event')
                self._longest_line = subject._line
                print(f"{self._longest_line=}")


class LongestFileWordObserver(Observer):
    """
    Observes increasing length of a word
    """
    _longest_word: str = None

    @staticmethod
    def _get_longest_word_from_line(line: str) -> str:
        return max(line.split(), key=len)

    def update(self, subject: Subject) -> None:
        line_longest_word = self._get_longest_word_from_line(subject._line)

        if not self._longest_word:
            print('\nLongestFileWordObserver: Initial event')
            self._longest_word = line_longest_word
            print(f"{self._longest_word=}")
        else:
            if len(self._longest_word) < len(line_longest_word):
                print('\nLongestFileWordObserver: Reacted to the event')
                self._longest_word = line_longest_word
                print(f"{self._longest_word=}")


class WordsCountObserver(Observer):
    """
    Observes words count of a line
    """
    _words_count: int = None

    @staticmethod
    def _get_words_count_from_line(line: str) -> int:
        return len(line.split())

    def update(self, subject: Subject) -> None:
        line_words_count = self._get_words_count_from_line(subject._line)

        if not self._words_count:
            print('\nWordsCountObserver: Initial event')
            self._words_count = line_words_count
            print(f"{self._words_count=}")

        else:
            print('\nWordsCountObserver: Reacted to the event')
            self._words_count += line_words_count
            print(f"{self._words_count=}")


class LineLongestWordObserver(Observer):
    """
    Observes line with longest word
    """
    _longest_word: str = None
    _line_with_longest_word: str = None
    _line_number: int = None

    @staticmethod
    def _get_longest_word_from_line(line: str) -> str:
        return max(line.split(), key=len)

    def update(self, subject: Subject) -> None:
        line_longest_word = self._get_longest_word_from_line(subject._line)

        if not self._longest_word:
            print('\nLineLongestWordObserver: Initial event')
            self._longest_word = line_longest_word
            self._line_with_longest_word = subject._line
            self._line_number = subject._line_number
            print(f"{self._longest_word=}, {self._line_with_longest_word=}, {self._line_number=}")

        else:
            if len(self._longest_word) < len(line_longest_word):
                print('\nLineLongestWordObserver: Reacted to the event')
                self._longest_word = line_longest_word
                self._line_with_longest_word = subject._line
                self._line_number = subject._line_number
                print(f"{self._longest_word=}, {self._line_with_longest_word=}, {self._line_number=}")


if __name__ == '__main__':
    subject = LineReaderSubject()

    observer1 = LongestFileLineObserver()
    subject.attach(observer1)

    observer2 = LongestFileWordObserver()
    subject.attach(observer2)

    observer3 = WordsCountObserver()
    subject.attach(observer3)

    observer4 = LineLongestWordObserver()
    subject.attach(observer4)

    subject.read_lines()
