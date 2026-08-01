"""혈중 산소(SpO2) 측정 — PPG 센서의 적색·적외선 LED를 함께 쓴다."""

from sensor.driver import PpgDriver

# 측정 시간 (초) — 이 시간 동안 손목을 움직이지 않아야 한다
SPO2_MEASURE_SECONDS = 30
# 신호 품질이 이 값 미만이면 측정 실패로 처리한다 (0~1)
SPO2_MIN_SIGNAL_QUALITY = 0.92
# 정상 범위 밖 값은 버린다
SPO2_VALID_RANGE = (70, 100)


class Spo2Meter:
    """SpO2를 한 번 측정한다. 신호가 나쁘면 None을 돌려준다."""

    def __init__(self, driver: PpgDriver | None = None):
        self.driver = driver or PpgDriver()
        self.failures = 0

    def measure(self, samples: list[float], quality: float):
        """샘플 묶음과 신호 품질로 SpO2(%)를 계산한다."""
        if quality < SPO2_MIN_SIGNAL_QUALITY:
            self.failures += 1
            return None
        if not samples:
            self.failures += 1
            return None
        value = round(sum(samples) / len(samples))
        low, high = SPO2_VALID_RANGE
        if not low <= value <= high:
            self.failures += 1
            return None
        return value
