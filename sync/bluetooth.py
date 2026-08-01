"""워치 쪽 블루투스 동기화 클라이언트."""

import json

# 한 번에 보낼 최대 기록 수
BATCH_LIMIT = 20


class SyncClient:
    """폰 연동 모듈(pulsefit-sync)로 기록을 보낸다."""

    def __init__(self, transport):
        self.transport = transport
        self.pending = []

    def enqueue(self, record: dict):
        self.pending.append(record)

    def flush(self) -> int:
        """대기 중인 기록을 묶어서 보낸다. 연결이 없으면 다음에 보낸다."""
        if not self.transport.connected:
            return 0
        sent = 0
        while self.pending:
            batch = self.pending[:BATCH_LIMIT]
            self.transport.send(json.dumps(batch, ensure_ascii=False))
            del self.pending[:BATCH_LIMIT]
            sent += len(batch)
        return sent
