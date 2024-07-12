from seek_music.resources.kkbox._client import KKBox

__all__ = ["SeekMusic"]


class SeekMusic:
    kkbox: "KKBox"

    def __init__(self):
        self.kkbox = KKBox()
