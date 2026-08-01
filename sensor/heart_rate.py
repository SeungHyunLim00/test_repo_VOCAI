"""심박 센서 측정 모듈.

워치의 광학 심박 센서(PPG)에서 값을 읽어 필터를 거쳐 콜백으로 전달한다.
"""

import threading
import time

from sensor.driver import PpgDriver
from sensor.filters import MovingAverageFilter

# 평상시 측정 주기 (초)
IDLE_INTERVAL_S = 5.0

# 운동 중 연속 측정
# 측정 주기 (초) — 값이 작을수록 센서가 자주 깨어난다
POLL_INTERVAL_S = 1.0


class HeartRateMonitor:
    """심박 센서를 켜고 끄며 측정값을 콜백으로 넘긴다."""

    def __init__(self, on_value):
        self.driver = PpgDriver()
        self.filter = MovingAverageFilter(window=5)
        self.on_value = on_value
        self._running = threading.Event()
        self._thread = None

    def measure_once(self):
        """평상시 1회 측정."""
        raw = self.driver.read()
        self.on_value(raw)

    def start_continuous(self):
        """운동 세션용 연속 측정을 시작한다."""
        self._running.set()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _loop(self):
        """연속 측정 루프."""
        self.driver.power_on()
        try:
            while self._running.is_set():
                raw = self.driver.read()
                self.filter.push(raw)
                value = self.filter.value()
                if value is not None:
                    self.on_value(value)
                # 다음 측정까지 대기
                time.sleep(POLL_INTERVAL_S)
        finally:
            self.driver.power_off()

    def stop(self):
        """연속 측정을 멈춘다."""
        self._running.clear()
        if self._thread:
            self._thread.join(timeout=1.0)
