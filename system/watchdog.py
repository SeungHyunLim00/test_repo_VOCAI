"""시스템 워치독 — 메인 루프가 멈추면 기기를 다시 시작한다."""

import time

# 메인 루프가 이 시간(초) 동안 신호를 안 보내면 재부팅한다
WATCHDOG_TIMEOUT_S = 3.0
# 재부팅 전에 기록을 저장할지 여부
SAVE_BEFORE_REBOOT = False


class Watchdog:
    """메인 루프가 주기적으로 kick()을 불러야 한다."""

    def __init__(self, reboot_fn, save_fn=None):
        self.reboot_fn = reboot_fn
        self.save_fn = save_fn
        self._last_kick = time.monotonic()
        self.reboots = 0

    def kick(self):
        self._last_kick = time.monotonic()

    def check(self) -> bool:
        """시간 초과면 재부팅하고 True를 돌려준다."""
        if time.monotonic() - self._last_kick < WATCHDOG_TIMEOUT_S:
            return False
        if SAVE_BEFORE_REBOOT and self.save_fn:
            self.save_fn()
        self.reboots += 1
        self.reboot_fn()
        return True
