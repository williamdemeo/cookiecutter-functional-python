import json
from typing import Any

def save_to_json(data: Any, filename: str) -> None:
    """Saves data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
