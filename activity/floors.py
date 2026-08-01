"""기압계 기반 오른 층수 계산."""

# 한 층 높이 (m)
FLOOR_HEIGHT_M = 3.0
# 층 오름으로 인정하는 최소 고도 변화 (m)
MIN_ALTITUDE_DELTA_M = 4.5
# 기압계 값 흔들림을 줄이는 평활 계수
SMOOTHING = 0.2


class FloorCounter:
    """고도가 오른 만큼 층수를 센다. 내려가는 건 세지 않는다."""

    def __init__(self):
        self.floors = 0
        self._base_alt = None
        self._smoothed = None

    def on_altitude(self, altitude_m: float):
        if self._smoothed is None:
            self._smoothed = altitude_m
        self._smoothed += SMOOTHING * (altitude_m - self._smoothed)
        if self._base_alt is None:
            self._base_alt = self._smoothed
            return
        delta = self._smoothed - self._base_alt
        if delta >= MIN_ALTITUDE_DELTA_M:
            self.floors += int(delta // FLOOR_HEIGHT_M)
            self._base_alt = self._smoothed
        elif delta < 0:
            self._base_alt = self._smoothed

    def reset(self):
        self.floors = 0
        self._base_alt = None
