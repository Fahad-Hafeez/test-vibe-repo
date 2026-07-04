import pytest

from calculator import (
    apply_coupon,
    apply_discount,
    calculate_bmi,
    calculate_median,
    calculate_shipping,
    calculate_total_with_tax,
    celsius_to_fahrenheit,
    chunk_list,
    compute_average,
    compound_interest,
    fahrenheit_to_celsius,
    format_username,
    get_max_value,
    is_palindrome,
    is_valid_email,
    normalize_phone_number,
    paginate,
    parse_int,
    round_to_nearest_cent,
    reverse_words,
    safe_divide,
    split_full_name,
)


def test_calculate_shipping_free_on_large_orders():
    assert calculate_shipping(weight=10, order_total=150) == 0.0


def test_apply_discount_returns_discounted_price():
    assert apply_discount(price=200.0, percentage=25.0) == 150.0


def test_compute_average_handles_empty_list():
    with pytest.raises(ValueError):
        compute_average([])


def test_format_username_returns_anonymous_for_blank_input():
    assert format_username("   ") == "Anonymous"


def test_celsius_to_fahrenheit_uses_correct_formula():
    assert pytest.approx(celsius_to_fahrenheit(0), rel=1e-6) == 32.0
    assert pytest.approx(celsius_to_fahrenheit(100), rel=1e-6) == 212.0


def test_chunk_list_creates_chunks_of_correct_size():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_compound_interest_compounds_annually():
    assert pytest.approx(compound_interest(1000.0, 0.05, 2), rel=1e-6) == 1102.5


def test_apply_coupon_never_goes_below_zero():
    assert apply_coupon(price=10.0, coupon=25.0) == 0.0


def test_calculate_median_even_length_list():
    assert calculate_median([1, 3, 2, 4]) == 2.5


def test_fahrenheit_to_celsius_uses_correct_formula():
    assert pytest.approx(fahrenheit_to_celsius(32), rel=1e-6) == 0.0
    assert pytest.approx(fahrenheit_to_celsius(212), rel=1e-6) == 100.0


def test_calculate_bmi_converts_height_to_meters():
    assert pytest.approx(calculate_bmi(70.0, 170.0), rel=1e-4) == 24.22


def test_calculate_total_with_tax_adds_tax():
    assert pytest.approx(calculate_total_with_tax(100.0, 0.08), rel=1e-6) == 108.0


def test_get_max_value_returns_maximum():
    assert get_max_value([1.0, 5.0, 3.0]) == 5.0


def test_normalize_phone_number_removes_non_digits():
    assert normalize_phone_number("(123) 456-7890") == "1234567890"


def test_is_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal, Panama")


def test_reverse_words_normalizes_whitespace():
    assert reverse_words("  hello   world  ") == "world hello"


def test_parse_int_parses_decimal_strings():
    assert parse_int("10") == 10


def test_split_full_name_returns_correct_fields():
    assert split_full_name("Jane Doe") == {"first": "Jane", "last": "Doe"}


def test_safe_divide_uses_true_division():
    assert pytest.approx(safe_divide(3.0, 2.0), rel=1e-6) == 1.5
    with pytest.raises(ValueError):
        safe_divide(1.0, 0.0)


def test_paginate_uses_one_based_page_numbers():
    assert paginate([1, 2, 3, 4, 5], page=2, page_size=2) == [3, 4]


def test_round_to_nearest_cent_uses_rounding():
    assert pytest.approx(round_to_nearest_cent(1.235), rel=1e-6) == 1.24


def test_is_valid_email_requires_dot_after_at():
    assert is_valid_email("user@example.com")
    assert not is_valid_email("user@example")
