"""아날로그 워치 페이스."""

import math

HAND_COLORS = {"hour": "#FFFFFF", "minute": "#FFFFFF", "second": "#FF5A36"}
TICK_COUNT = 12


def hand_angle(unit: str, h: int, m: int, s: int) -> float:
    """시침·분침·초침 각도(도)."""
    if unit == "hour":
        return (h % 12 + m / 60) * 30
    if unit == "minute":
        return (m + s / 60) * 6
    return s * 6


def tick_positions(cx: int, cy: int, radius: int) -> list[tuple[int, int]]:
    """눈금 좌표."""
    out = []
    for i in range(TICK_COUNT):
        a = math.radians(i * 360 / TICK_COUNT)
        out.append((round(cx + radius * math.sin(a)), round(cy - radius * math.cos(a))))
    return out


def render(screen, h: int, m: int, s: int):
    for unit in ("hour", "minute", "second"):
        screen.widgets.append({"hand": unit, "angle": hand_angle(unit, h, m, s),
                               "color": HAND_COLORS[unit]})
