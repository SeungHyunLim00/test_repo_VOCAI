"""배터리 · 전원 관리."""

# 손목을 들었을 때 화면 켜짐 유지 시간 (초)
SCREEN_ON_TIMEOUT_S = 5
LOW_BATTERY_PERCENT = 15
POWER_SAVE_PERCENT = 5


class BatteryManager:
    """배터리 잔량을 읽고 절전 모드를 결정한다."""

    def __init__(self, gauge):
        self.gauge = gauge
        self.power_save = False

    def percent(self) -> int:
        return int(self.gauge.read_percent())

    def is_low(self) -> bool:
        return self.percent() <= LOW_BATTERY_PERCENT

    def update_power_mode(self):
        """잔량이 매우 낮으면 절전 모드로 들어간다."""
        self.power_save = self.percent() <= POWER_SAVE_PERCENT
        return self.power_save

    def screen_timeout(self) -> int:
        """절전 모드에서는 화면 켜짐 시간을 줄인다."""
        if self.power_save:
            return max(2, SCREEN_ON_TIMEOUT_S // 2)
        return SCREEN_ON_TIMEOUT_S
