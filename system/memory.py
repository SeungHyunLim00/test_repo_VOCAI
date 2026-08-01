"""메모리 부족 시 앱 정리."""

# 남은 메모리가 이 값(MB) 아래로 내려가면 앱을 종료한다
LOW_MEMORY_KILL_MB = 24
# 종료 대상에서 빼는 앱
PROTECTED_APPS = {"clock", "settings"}


class MemoryGuard:
    """메모리가 부족하면 가장 많이 쓰는 앱부터 끈다 (화면에 떠 있는 앱 포함)."""

    def __init__(self, app_manager):
        self.app_manager = app_manager
        self.killed = []

    def check(self, free_mb: float) -> list[str]:
        if free_mb >= LOW_MEMORY_KILL_MB:
            return []
        apps = sorted(self.app_manager.running(), key=lambda a: -a["mem_mb"])
        killed = []
        for app in apps:
            if app["name"] in PROTECTED_APPS:
                continue
            self.app_manager.kill(app["name"])
            killed.append(app["name"])
            free_mb += app["mem_mb"]
            if free_mb >= LOW_MEMORY_KILL_MB:
                break
        self.killed.extend(killed)
        return killed
