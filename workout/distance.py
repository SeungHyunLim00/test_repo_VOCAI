"""GPS 기반 이동 거리 계산."""

import math

# GPS 신호가 약할 때 보정 계수
WEAK_SIGNAL_CORRECTION = 0.97
EARTH_RADIUS_M = 6_371_000


def haversine_m(lat1, lon1, lat2, lon2) -> float:
    """두 좌표 사이 거리(m)."""
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * EARTH_RADIUS_M * math.asin(math.sqrt(a))


class DistanceTracker:
    """GPS 좌표를 받아 누적 거리를 계산한다."""

    def __init__(self):
        self.total_m = 0.0
        self._last = None
        self.active = False

    def start(self):
        self.active = True
        self._last = None

    def add_fix(self, lat, lon, weak_signal=False):
        if not self.active:
            return
        if self._last is not None:
            step = haversine_m(*self._last, lat, lon)
            if weak_signal:
                step *= WEAK_SIGNAL_CORRECTION
            self.total_m += step
        self._last = (lat, lon)

    def stop(self):
        self.active = False
        return self.total_m
