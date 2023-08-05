
def power_to(val, exp) -> int | float | None:
    if not isinstance(val, (int, float)):
        return None
    return val **exp

def capitalize(s: str) -> str | None:
    if not isinstance(s, str):
        return None
    return s.capitalize()
