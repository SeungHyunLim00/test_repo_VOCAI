"""잠든 동안 혈중 산소(SpO2)를 주기적으로 재서 수면 기록에 남긴다."""

import time

from sensor.spo2 import SPO2_MEASURE_SECONDS, Spo2Meter

# 잠든 동안 SpO2 측정 간격 (초) — 잴 때마다 PPG 적색·적외선 LED를 SPO2_MEASURE_SECONDS 동안 켠다
NIGHT_SPO2_INTERVAL_S = 30


class NightSpo2Recorder:
    """수면 추적기가 '잠듦'으로 본 동안만 SpO2를 잰다."""

    def __init__(self, tracker, meter: Spo2Meter | None = None):
        self.tracker = tracker
        self.meter = meter or Spo2Meter()
        self.readings = []

    def record_while_asleep(self, read_window):
        """수면 중 측정 루프 — 잠들어 있는 동안 재고, 다음 측정까지 쉰다."""
        while self.tracker.asleep_at is not None:
            samples, quality = read_window(SPO2_MEASURE_SECONDS)
            value = self.meter.measure(samples, quality)
            if value is not None:
                self.readings.append(value)
            time.sleep(NIGHT_SPO2_INTERVAL_S)
