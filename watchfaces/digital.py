"""디지털 워치 페이스."""

COMPLICATIONS = ["날짜", "걸음", "날씨"]
TIME_FONT_PX = 64


def format_time(h: int, m: int, use_24h: bool = True) -> str:
    if use_24h:
        return f"{h:02d}:{m:02d}"
    suffix = "오전" if h < 12 else "오후"
    return f"{suffix} {(h % 12) or 12}:{m:02d}"


def render(screen, h: int, m: int, data: dict):
    screen.widgets.append({"text": format_time(h, m), "size": TIME_FONT_PX})
    for i, name in enumerate(COMPLICATIONS):
        screen.widgets.append({"label": name, "value": data.get(name, "-"), "slot": i})
