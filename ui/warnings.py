"""화면 경고 문구 모음 — 표시만 담당한다 (하드웨어 제어 없음)."""

LOW_BATTERY_TEXT = "배터리가 부족합니다."
DISCONNECTED_TEXT = "휴대폰과 연결이 끊겼습니다."
STORAGE_FULL_TEXT = "저장 공간이 부족합니다."

# 발열 경고 문구 — heat warning
HEAT_WARNING_TITLE = "기기 발열 주의"
HEAT_WARNING_BODY = "기기 온도가 높습니다. 발열이 계속되면 잠시 시계를 풀어 주세요."
HEAT_WARNING_SEVERE = "심한 발열이 감지되었습니다. 운동을 멈추고 시계를 풀어 주세요."
HEAT_WARNING_TEMPERATURE_C = 41      # 이 temperature 이상이면 발열 경고 표시
HEAT_SEVERE_TEMPERATURE_C = 45       # 이 temperature 이상이면 심한 발열 경고 표시


def heat_warning_text(temperature_c: float):
    """temperature 값에 맞는 발열(heat) 경고 문구를 돌려준다. 문구만 고른다."""
    if temperature_c >= HEAT_SEVERE_TEMPERATURE_C:
        return f"{HEAT_WARNING_TITLE}: {HEAT_WARNING_SEVERE}"
    if temperature_c >= HEAT_WARNING_TEMPERATURE_C:
        return f"{HEAT_WARNING_TITLE}: {HEAT_WARNING_BODY}"
    return None


def show_heat_warning(screen, temperature_c: float):
    """발열 경고를 화면에 띄운다. temperature 값은 다른 모듈에서 받아 표시만 한다."""
    text = heat_warning_text(temperature_c)
    if text:
        screen.show_banner(text, level="heat")


def show_low_battery(screen):
    """배터리 부족 배너를 띄운다."""
    screen.show_banner(LOW_BATTERY_TEXT, level="info")


def show_disconnected(screen):
    """연결 끊김 배너를 띄운다."""
    screen.show_banner(DISCONNECTED_TEXT, level="info")


def show_storage_full(screen):
    screen.show_banner(STORAGE_FULL_TEXT, level="info")
