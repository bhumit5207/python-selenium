from pathlib import Path
from typing import Any


def get_file_path(relative_path: str) -> str:
    return str(Path(__file__).resolve().parents[1] / relative_path)


def get_timestamp() -> str:
    from datetime import datetime
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def safe_cast(value: Any, to_type: type, default: Any = None) -> Any:
    try:
        return to_type(value)
    except (TypeError, ValueError):
        return default
