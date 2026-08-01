"""방해 금지 모드 일정."""

from datetime import datetime, time

DEFAULT_START = time(22, 0)
DEFAULT_END = time(7, 0)


class DoNotDisturb:
    """정해진 시간대 또는 수동으로 방해 금지를 켠다."""

    def __init__(self, start: time = DEFAULT_START, end: time = DEFAULT_END):
        self.start = start
        self.end = end
        self.manual = False
        self.scheduled = True

    def active(self, now: datetime | None = None) -> bool:
        if self.manual:
            return True
        if not self.scheduled:
            return False
        t = (now or datetime.now()).time()
        if self.start <= self.end:
            return self.start <= t < self.end
        return t >= self.start or t < self.end

    def toggle(self):
        self.manual = not self.manual
        return self.manual
