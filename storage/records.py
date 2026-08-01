"""워치 내부 기록 저장."""

import json
from pathlib import Path

MAX_RECORDS = 500


class RecordStore:
    """운동·심박 기록을 JSON 파일로 저장한다."""

    def __init__(self, path: str = "records.json"):
        self.path = Path(path)
        self.records = []

    def load(self):
        if self.path.exists():
            self.records = json.loads(self.path.read_text(encoding="utf-8"))
        return self.records

    def add(self, record: dict):
        """기록을 추가하고 오래된 기록은 지운다."""
        self.records.append(record)
        if len(self.records) > MAX_RECORDS:
            self.records = self.records[-MAX_RECORDS:]

    def save(self):
        self.path.write_text(json.dumps(self.records, ensure_ascii=False), encoding="utf-8")
