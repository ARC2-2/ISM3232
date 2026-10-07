# business_riles.py
# Author: Aaron Contente

APPROVAL_LIMIT = 1000  # module level constant


def calculate_total(price: float, quantity: int) -> float:
    """Return total cost including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Return True if amount exceeds approval limit."""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount: float) -> str:
    """Return approval tier based on routing tier"""
    if amount <= 1000:
        return "auto"
    elif amount <= 5000:
        return "manager"
    else:
        return "director"


def apply_discount(price: float, pct: float) -> float:
    """Return price after applying discount, pct is 0-100"""
    return price * (1 - pct / 100)
