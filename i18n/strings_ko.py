"""화면 문구 (한국어) — 표시용 리소스만 둔다."""

STRINGS = {
    "workout.start": "운동 시작",
    "workout.finish": "운동 종료",
    "battery.low": "배터리가 부족합니다",
    "sync.done": "동기화 완료",
    "sleep.summary": "지난밤 수면",
    "steps.goal": "오늘 걸음 목표 달성!",
    "heat.title": "기기 발열 주의",
    "heat.body": "기기가 뜨거우면 잠시 풀어 두세요",
    "heat.workout": "운동 중 발열이 감지되었습니다",
}


def t(key: str) -> str:
    return STRINGS.get(key, key)
