from src.libs.my_lib import power_to, capitalize


def test_power_to_0_pow_any():
    assert power_to(0, 2) == 0


def test_power_to_any_pow_0():
    assert power_to(2, 0) == 1


def test_power_to_2_to_m2():
    assert power_to(2, -2) == 0.25


def test_power_to_none():
    assert power_to("2", -2) is None


def test_capitalize_ok():
    assert capitalize("test") == "Test"


def test_capitalize_numeric():
    assert capitalize("123test") == "123test"


def test_capitalize_none():
    assert capitalize(3) is None
