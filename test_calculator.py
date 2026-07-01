import pytest

from calculator import (
    apply_coupon,
    apply_discount,
    calculate_bmi,
    calculate_median,
    calculate_shipping,
    celsius_to_fahrenheit,
    chunk_list,
    compute_average,
    compound_interest,
    fahrenheit_to_celsius,
    format_username,
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
