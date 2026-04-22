# vibe/utils.py

def vibe(func):
    """Marker decorator for vibe functions."""
    return func

@vibe
def calculate_sum(a: int, b: int) -> int:
    """Calculate sum of two numbers."""
    return a + b

@vibe
def process_data(items: list[int]) -> dict[str, int]:
    """Process list of numbers."""
    return {"count": len(items), "sum": sum(items)}
