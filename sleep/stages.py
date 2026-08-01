"""수면 단계(얕은 잠·깊은 잠·렘) 분류와 수면 점수."""

# 깊은 잠 판정: 심박이 평소 안정 심박의 이 비율 이하일 때
DEEP_SLEEP_HR_RATIO = 0.72
# 렘 판정: 심박 변동이 이 값(bpm) 이상일 때
REM_HR_VARIATION_BPM = 8
# 수면 점수 가중치
SCORE_WEIGHTS = {"duration": 0.5, "deep": 0.3, "wake": 0.2}
TARGET_SLEEP_MIN = 420


def classify(epochs: list[dict], resting_bpm: float) -> list[str]:
    """30초 단위 구간마다 단계를 붙인다. epoch = {"bpm": .., "var": ..}."""
    stages = []
    for e in epochs:
        if e["bpm"] <= resting_bpm * DEEP_SLEEP_HR_RATIO:
            stages.append("deep")
        elif e["var"] >= REM_HR_VARIATION_BPM:
            stages.append("rem")
        else:
            stages.append("light")
    return stages


def sleep_score(stages: list[str], wake_count: int) -> int:
    """0~100 수면 점수."""
    if not stages:
        return 0
    minutes = len(stages) / 2
    deep_ratio = stages.count("deep") / len(stages)
    duration = min(minutes / TARGET_SLEEP_MIN, 1.0)
    wake = max(0.0, 1 - wake_count / 10)
    total = (SCORE_WEIGHTS["duration"] * duration + SCORE_WEIGHTS["deep"] * min(deep_ratio / 0.2, 1.0)
             + SCORE_WEIGHTS["wake"] * wake)
    return round(total * 100)
