"""화면 경고 문구 모음 — 표시만 담당한다 (하드웨어 제어 없음)."""

LOW_BATTERY_TEXT = "배터리가 부족합니다."
DISCONNECTED_TEXT = "휴대폰과 연결이 끊겼습니다."
STORAGE_FULL_TEXT = "저장 공간이 부족합니다."


def show_low_battery(screen):
    """배터리 부족 배너를 띄운다."""
    screen.show_banner(LOW_BATTERY_TEXT, level="info")


def show_disconnected(screen):
    """연결 끊김 배너를 띄운다."""
    screen.show_banner(DISCONNECTED_TEXT, level="info")


def show_storage_full(screen):
    screen.show_banner(STORAGE_FULL_TEXT, level="info")
