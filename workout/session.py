"""운동 세션 관리."""

from datetime import datetime

from sensor.heart_rate import HeartRateMonitor
from workout.distance import DistanceTracker


class WorkoutSession:
    """운동 시작부터 종료까지 심박·거리를 기록한다."""

    def __init__(self, kind: str):
        self.kind = kind
        self.samples = []
        self.hr = HeartRateMonitor(on_value=self._on_heart_rate)
        self.distance = DistanceTracker()
        self.started_at = None

    def start(self):
        """운동을 시작한다."""
        self.started_at = datetime.now()
        self.distance.start()
        self.hr.start_continuous()

    def _on_heart_rate(self, value):
        self.samples.append(value)

    def finish(self):
        self.hr.stop()
        self.distance.stop()
        return {"kind": self.kind, "samples": len(self.samples)}
