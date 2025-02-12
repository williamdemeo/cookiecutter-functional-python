from dataclasses import dataclass

@dataclass(frozen=True)
class NumberData:
    """Immutable data class for representing number processing results."""
    original: int
    transformed: int
