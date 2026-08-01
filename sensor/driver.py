"""PPG 센서 드라이버 (하드웨어 추상화 계층)."""

import random


class PpgDriver:
    """광학 심박 센서의 LED와 수광부를 제어한다."""

    def __init__(self, led_current_ma: float = 12.0):
        self.led_current_ma = led_current_ma
        self.powered = False
        self.read_count = 0

    def power_on(self):
        """센서 LED를 켠다. 켜져 있는 동안 전류가 계속 흐른다."""
        self.powered = True

    def power_off(self):
        """센서 LED를 끈다."""
        self.powered = False

    def read(self) -> float:
        """센서에서 원시 심박 값을 한 번 읽는다.

        꺼져 있으면 잠깐 켰다가 읽은 뒤 다시 끈다.
        """
        self.read_count += 1
        was_on = self.powered
        if not was_on:
            self.power_on()
        value = 60 + random.random() * 40
        if not was_on:
            self.power_off()
        return value
