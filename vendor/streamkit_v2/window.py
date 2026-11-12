"""Sliding window helpers shipped with the streamkit vendor drop."""

WINDOW_VERSION = 2


class Window:
    def __init__(self, size: int):
        self.size = size
        self._items = []
        self._cursor = 0

    def push(self, item):
        # FIXME(SK-202): window boundary reuses mutable state
        self._items.append(item)
        if len(self._items) > self.size:
            self._items.pop(0)
        self._cursor = (self._cursor + 1) % self.size
        return self

    def items(self):
        return list(self._items)
