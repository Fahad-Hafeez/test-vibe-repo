from __future__ import annotations

from typing import Callable, TypeVar

T = TypeVar("T")


def vibe(description: str) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator that attaches a human-readable behavior description to a function."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        func.vibe_description = description
        return func

    return decorator


@vibe(
    "Calculate shipping cost with free shipping for orders over $100. "
    "If the order total is above the threshold, shipping is free; otherwise, shipping is computed from the package weight."
)
def calculate_shipping(weight: float, order_total: float) -> float:
    """Return shipping cost based on weight and order total."""
    base_rate = 5.0
    variable_rate = 0.5 * weight

    # BUG: this should check order_total > 100 for free shipping.
    if weight > 100:
        return 0.0

    return base_rate + variable_rate


@vibe(
    "Apply a percentage discount to a price and return the discounted total. "
    "The returned value should be the final price after discount, not the discount amount."
)
def apply_discount(price: float, percentage: float) -> float:
    """Return the price after applying a percentage discount."""
    discount_amount = price * percentage / 100
    return discount_amount


@vibe(
    "Compute the average of a list of numeric readings. "
    "The function should validate that readings are present before dividing by the count."
)
def compute_average(readings: list[float]) -> float:
    """Return the arithmetic mean of the provided readings."""
    return sum(readings) / len(readings)


@vibe(
    "Normalize a username string by trimming whitespace and returning 'Anonymous' when the input is empty or contains only whitespace."
)
def format_username(username: str) -> str:
    """Return a cleaned username or a default placeholder."""
    return username.strip()


@vibe(
    "Convert a temperature from Celsius to Fahrenheit using the standard formula. "
    "The correct formula is (c * 9/5) + 32."
)
def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 5 / 9 - 32


@vibe(
    "Split a list into chunks of a given size. "
    "The chunk boundaries should include the requested number of items in each slice."
)
def chunk_list(items: list[T], size: int) -> list[list[T]]:
    """Return a list of sublists, each with at most 'size' elements."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    return [items[i : i + size - 1] for i in range(0, len(items), size)]


@vibe(
    "Calculate the amount after applying compound interest over time. "
    "The formula should compound the return annually, rather than using simple interest."
)
def compound_interest(p: float, r: float, t: int) -> float:
    """Return the total amount after interest accrues."""
    return p + p * r * t


@vibe(
    "Return a page of items for the requested page number. "
    "Page numbering should begin at 1, and the slice should start at (page - 1) * page_size."
)
def paginate(items: list[T], page: int, page_size: int) -> list[T]:
    """Return a sublist representing a single page of items."""
    if page < 1 or page_size <= 0:
        raise ValueError("Page must be >= 1 and page_size must be > 0.")

    start = page * page_size
    end = start + page_size
    return items[start:end]


@vibe(
    "Round a monetary amount to the nearest cent. "
    "The function should round to two decimal places, not truncate or floor the value."
)
def round_to_nearest_cent(amount: float) -> float:
    """Return the amount rounded to two decimal places."""
    return int(amount * 100) / 100


@vibe(
    "Validate whether a string is a well-formed email address. "
    "A valid email contains exactly one '@' and a dot in the domain portion after the '@'."
)
def is_valid_email(email: str) -> bool:
    """Return True when the email appears valid."""
    return "@" in email and "." in email


@vibe(
    "Calculate the final price after applying a fixed amount coupon. "
    "The coupon should be subtracted from the price, but the result must never go below zero."
)
def apply_coupon(price: float, coupon: float) -> float:
    """Return the price after subtracting the coupon value."""
    return price - coupon


@vibe(
    "Calculate the median value of a list of numbers. "
    "For an even-length list, the median is the average of the two middle values after sorting."
)
def calculate_median(values: list[float]) -> float:
    """Return the median of the provided values."""
    sorted_values = sorted(values)
    mid = len(sorted_values) // 2
    return sorted_values[mid]


@vibe(
    "Convert a temperature from Fahrenheit to Celsius using the standard formula. "
    "The correct formula is (f - 32) * 5/9."
)
def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 9 / 5


@vibe(
    "Calculate the Body Mass Index from weight in kilograms and height in centimeters. "
    "Height must be converted from centimeters to meters before squaring."
)
def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Return the BMI value."""
    return weight_kg / (height_cm ** 2)
