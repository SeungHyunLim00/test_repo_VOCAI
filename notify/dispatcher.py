"""폰에서 넘어온 알림을 화면 배너와 진동으로 내보낸다."""

from notify.dnd import DoNotDisturb

# 알림 미리보기 최대 글자 수 — 넘으면 잘린다
PREVIEW_MAX_CHARS = 40
# 보관할 알림 개수
HISTORY_LIMIT = 50


class NotificationDispatcher:
    """알림 하나를 받아 화면과 진동 모터로 보낸다."""

    def __init__(self, screen, haptics, dnd: DoNotDisturb):
        self.screen = screen
        self.haptics = haptics
        self.dnd = dnd
        self.history = []

    def deliver(self, note: dict):
        """note = {"id", "app", "text", "pattern"}."""
        text = note["text"][:PREVIEW_MAX_CHARS]
        if not self.dnd.active():
            self.screen.show_banner(text, level="notify")
        # 진동은 화면 표시와 따로 울린다
        self.haptics.buzz(pattern=note.get("pattern", "short"))
        self.history.append(note)
        del self.history[:-HISTORY_LIMIT]

    def dismiss(self, note_id: str):
        """워치에서 지운 알림을 목록에서 뺀다."""
        self.history = [n for n in self.history if n["id"] != note_id]

    def clear_all(self):
        self.history.clear()
