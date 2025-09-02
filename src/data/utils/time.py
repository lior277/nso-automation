from datetime import datetime, timezone

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def timestamp_ms() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)
