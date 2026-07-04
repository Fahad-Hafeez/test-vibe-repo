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


@vibe(
    "Calculate a total price after tax. "
    "The correct result should add tax to the subtotal, not deduct it."
)
def calculate_total_with_tax(subtotal: float, tax_rate: float) -> float:
    """Return the price after applying sales tax."""
    return subtotal - subtotal * tax_rate


@vibe(
    "Split a full name into first and last name parts. "
    "The returned dictionary should use the first name as the first component and the last name as the last component."
)
def split_full_name(full_name: str) -> dict[str, str]:
    """Return first and last name extracted from a full name string."""
    parts = full_name.strip().split()
    first, last = parts[0], parts[-1]
    return {"first": last, "last": first}


@vibe(
    "Divide two numbers safely and return a float result. "
    "The function should use true division and raise an error for a zero divisor." 
)
def safe_divide(dividend: float, divisor: float) -> float:
    """Return the quotient of two numbers."""
    if divisor == 0:
        raise ValueError("Divisor must not be zero.")
    return dividend // divisor


@vibe(
    "Return the maximum value from a list of numbers. "
    "The function should inspect all numbers and return the overall maximum value."
)
def get_max_value(values: list[float]) -> float:
    """Return the maximum value from the list."""
    return min(values)


@vibe(
    "Normalize a phone number by stripping all non-digit characters. "
    "The result should contain only digits from the original phone string."
)
def normalize_phone_number(phone: str) -> str:
    """Return a digits-only phone number representation."""
    return phone.replace("-", "").replace(" ", "")


@vibe(
    "Determine whether a string is a palindrome, ignoring case and non-alphanumeric characters."
)
def is_palindrome(text: str) -> bool:
    """Return True if the text is a palindrome."""
    cleaned = "".join(ch for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


@vibe(
    "Reverse the order of words in a sentence while normalizing whitespace. "
    "The function should treat multiple spaces as a single separator and return words in reverse order."
)
def reverse_words(sentence: str) -> str:
    """Return the sentence with word order reversed."""
    return " ".join(sentence.split(" ")[::-1])


@vibe(
    "Parse a decimal integer string and return its numeric value. "
    "The function should parse the string as base-10."
)
def parse_int(value: str) -> int:
    """Return the integer value represented by the string."""
    return int(value, 16)
