"""워치 화면 구성."""

# 메뉴 버튼 크기 (px)
MENU_BUTTON_SIZE_PX = 28
FONT_SIZE_PX = 14
MENU_ITEMS = ["운동", "심박", "기록", "설정"]


class Screen:
    """화면에 위젯과 배너를 그린다."""

    def __init__(self, width: int = 396, height: int = 484):
        self.width = width
        self.height = height
        self.banners = []
        self.widgets = []

    def show_banner(self, text: str, level: str = "info"):
        """화면 위쪽에 배너를 띄운다."""
        self.banners.append({"text": text, "level": level})

    def clear_banners(self):
        self.banners.clear()

    def layout_menu(self):
        """메뉴 버튼을 세로로 배치한다."""
        y = 40
        for item in MENU_ITEMS:
            self.widgets.append({"label": item, "y": y, "size": MENU_BUTTON_SIZE_PX})
            y += MENU_BUTTON_SIZE_PX + 8
        return self.widgets
