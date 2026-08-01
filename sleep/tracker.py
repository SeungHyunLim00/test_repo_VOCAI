"""수면 시작·종료 감지."""

from datetime import datetime, timedelta

# 움직임이 이 시간(분) 이상 없으면 잠든 것으로 본다
SLEEP_ONSET_STILL_MIN = 10
# 움직임 크기 기준 (g) — 이보다 작으면 '가만히 있음'
STILL_MOTION_G = 0.05
# 이 시간(분)보다 짧은 수면은 기록하지 않는다
MIN_SLEEP_DURATION_MIN = 180
# 깸으로 인정하는 연속 움직임 시간 (분)
WAKE_MOTION_MIN = 15


class SleepTracker:
    """손목 움직임만으로 잠든 시각과 깬 시각을 정한다."""

    def __init__(self):
        self.still_since = None
        self.asleep_at = None
        self.sessions = []
        self._moving_since = None

    def on_motion(self, now: datetime, motion_g: float):
        if motion_g < STILL_MOTION_G:
            self._moving_since = None
            if self.still_since is None:
                self.still_since = now
            onset = timedelta(minutes=SLEEP_ONSET_STILL_MIN)
            if self.asleep_at is None and now - self.still_since >= onset:
                self.asleep_at = self.still_since
            return
        self.still_since = None
        if self.asleep_at is None:
            return
        if self._moving_since is None:
            self._moving_since = now
        if now - self._moving_since >= timedelta(minutes=WAKE_MOTION_MIN):
            self._close(self._moving_since)

    def _close(self, woke_at: datetime):
        minutes = (woke_at - self.asleep_at).total_seconds() / 60
        if minutes >= MIN_SLEEP_DURATION_MIN:
            self.sessions.append({"start": self.asleep_at, "end": woke_at, "minutes": round(minutes)})
        self.asleep_at = None
        self._moving_since = None
