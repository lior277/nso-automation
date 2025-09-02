import random
import string

def random_string(length: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

def random_email(domain: str = "example.com") -> str:
    prefix = random_string(6).lower()
    return f"{prefix}@{domain}"

def random_int(low: int = 1, high: int = 1000) -> int:
    return random.randint(low, high)
