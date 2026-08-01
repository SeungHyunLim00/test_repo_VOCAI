"""가속도 기반 걸음 수 계산 (만보기)."""

from datetime import datetime

# 걸음으로 인정하는 가속도 크기 (g) — 낮을수록 작은 흔들림도 걸음으로 센다
STEP_ACCEL_THRESHOLD_G = 1.1
# 걸음 사이 최소 간격 (ms) — 이보다 짧으면 같은 걸음으로 본다
MIN_STEP_GAP_MS = 250
# 팔 흔들림이 없을 때(유모차·카트) 보조 판정 사용 여부
USE_CADENCE_FALLBACK = False


class Pedometer:
    """가속도 피크를 세어 하루 걸음 수를 만든다."""

    def __init__(self):
        self.steps_today = 0
        self._last_peak_ms = None
        self._day = datetime.utcnow().date()

    def on_accel(self, magnitude_g: float, t_ms: int):
        """가속도 크기 하나를 받는다. 피크면 걸음으로 센다."""
        self._roll_day()
        if magnitude_g < STEP_ACCEL_THRESHOLD_G:
            return
        if self._last_peak_ms is not None and t_ms - self._last_peak_ms < MIN_STEP_GAP_MS:
            return
        self._last_peak_ms = t_ms
        self.steps_today += 1

    def _roll_day(self):
        """날짜가 바뀌면 걸음 수를 0으로 되돌린다."""
        today = datetime.utcnow().date()
        if today != self._day:
            self._day = today
            self.steps_today = 0

    def summary(self) -> dict:
        return {"date": self._day.isoformat(), "steps": self.steps_today}
