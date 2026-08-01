"""워치 내부 로그."""

LEVELS = ("debug", "info", "warn", "error")
MAX_LINES = 200


class RingLog:
    """최근 로그만 남기는 링 버퍼."""

    def __init__(self):
        self.lines = []

    def write(self, level: str, msg: str):
        if level not in LEVELS:
            level = "info"
        self.lines.append(f"[{level}] {msg}")
        del self.lines[:-MAX_LINES]

    def dump(self) -> str:
        return "\n".join(self.lines)
