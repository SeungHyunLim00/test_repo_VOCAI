"""센서 신호 필터."""

from collections import deque


class MovingAverageFilter:
    """최근 N개 값의 이동 평균을 낸다."""

    def __init__(self, window: int = 5):
        self.window = window
        self._values = deque(maxlen=window)

    def push(self, raw: float):
        """새 원시 값을 넣는다. 비정상 값은 버린다."""
        if raw <= 0 or raw > 250:
            return
        self._values.append(raw)

    def value(self):
        """창이 다 차면 평균을, 아니면 None을 돌려준다."""
        if len(self._values) < self.window:
            return None
        return sum(self._values) / len(self._values)

    def reset(self):
        self._values.clear()
