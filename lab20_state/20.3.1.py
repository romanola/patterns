from __future__ import annotations
from abc import ABC, abstractmethod


class MediaPlayer:
    _tracks: list = []
    _state: State = None
    _current_track_num = 0

    def __init__(self) -> None:
        self.set_state(StopState())

    def get_current_track(self) -> str:
        return self._tracks[self._current_track_num]

    def set_track_num(self, track_num: int) -> None:
        if track_num < 0 or track_num > len(self._tracks):
            return
        self._current_track_num = track_num

    def get_current_track_num(self) -> int:
        return self._current_track_num

    def get_tracks(self) -> list:
        return self._tracks

    def add_track(self, track) -> None:
        self._tracks.append(track)

    def set_state(self, state: State) -> None:
        print(f'MediaPlayer: set state to {type(state).__name__}')
        self._state = state
        self._state.media_player = self

    def get_state(self) -> State:
        return self._state

    def play(self):
        self._state.play()

    def pause(self):
        self._state.pause()

    def next(self):
        self._state.next()

    def prev(self):
        self._state.prev()

    def stop(self):
        self._state.stop()


class State(ABC):

    @property
    def media_player(self) -> MediaPlayer:
        return self._media_player

    @media_player.setter
    def media_player(self, media_player: MediaPlayer) -> None:
        self._media_player = media_player

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def prev(self):
        pass


class PlayingState(State):

    def play(self):
        pass

    def pause(self):
        self.media_player.set_state(PauseState())
        print(f'Track {self.media_player.get_current_track()} paused')

    def stop(self):
        self.media_player.set_state(StopState())
        print(f'Track {self.media_player.get_current_track()} stopped')

    def next(self):
        track_num = self.media_player.get_current_track_num()
        size = len(self.media_player.get_tracks())

        if track_num >= size:
            return

        self.media_player.set_state(PlayingState())
        self.media_player.set_track_num(track_num + 1)
        print(f'Next track {self.media_player.get_current_track()} playing')

    def prev(self):
        track_num = self.media_player.get_current_track_num()
        if track_num == 0:
            return
        self.media_player.set_state(PlayingState())
        self.media_player.set_track_num(track_num - 1)
        print(f'Previous track {self.media_player.get_current_track()} playing')


class PauseState(State):

    def play(self):
        self.media_player.set_state(PlayingState())
        print(f'Track {self.media_player.get_current_track()} playing')

    def pause(self):
        pass

    def stop(self):
        self.media_player.set_state(StopState())
        print(f'Track {self.media_player.get_current_track()} stopped')

    def next(self):
        track_num = self.media_player.get_current_track_num()
        size = len(self.media_player.get_tracks())

        if track_num >= size:
            return

        self.media_player.set_state(PlayingState())
        self.media_player.set_track_num(track_num + 1)
        print(f'Next track {self.media_player.get_current_track()} playing')

    def prev(self):
        track_num = self.media_player.get_current_track_num()
        if track_num == 0:
            return
        self.media_player.set_state(PlayingState())
        self.media_player.set_track_num(track_num - 1)
        print(f'Previous track {self.media_player.get_current_track()} playing')


class StopState(State):

    def play(self):
        self.media_player.set_state(PlayingState())
        print(f'Track {self.media_player.get_current_track()} playing')

    def pause(self):
        pass

    def stop(self):
        pass

    def next(self):
        track_num = self.media_player.get_current_track_num()
        size = len(self.media_player.get_tracks())

        if track_num >= size:
            return

        self.media_player.set_state(PlayingState())
        self.media_player.set_track_num(track_num + 1)
        print(f'Next track {self.media_player.get_current_track()} playing')

    def prev(self):
        track_num = self.media_player.get_current_track_num()
        if track_num == 0:
            return
        self.media_player.set_state(PlayingState())
        self.media_player.set_track_num(track_num - 1)
        print(f'Previous track {self.media_player.get_current_track()} playing')


if __name__ == '__main__':
    media_player = MediaPlayer()

    media_player.add_track('track1')
    media_player.add_track('track2')
    media_player.add_track('track3')
    media_player.add_track('track4')
    media_player.add_track('track5')
    media_player.add_track('track6')

    media_player.play()
    media_player.pause()
    media_player.play()
    media_player.next()
    media_player.next()
    media_player.prev()
    media_player.stop()
    media_player.play()
    media_player.stop()
