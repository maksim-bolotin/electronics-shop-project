"""Здесь надо написать тесты с использованием pytest для модуля Phone."""
import pytest
from src.phone import Phone


@pytest.fixture()
def get_phone():
    return [Phone("Смартфон", 10000, 20, 3), Phone("Xiaomi", "", 1, 1)]


def test__init__(get_phone):
    assert get_phone[0].name == "Смартфон"
    assert get_phone[1].name == "Xiaomi"
    assert get_phone[0].price == 10000
    assert get_phone[0].quantity == 20
    assert get_phone[1].number_of_sim == 1


def test_number_of_sim(get_phone):
    assert get_phone[1].number_of_sim == 1
    phone1 = Phone("iPhone 14", 120_000, 5, 0)
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test__repr__(get_phone):
    assert repr(get_phone[0]) == "Phone('Смартфон', 10000, 20, 3)"
    assert repr(get_phone[1]) == "Phone('Xiaomi', , 1, 1)"


def test__str__(get_phone):
    assert str(get_phone[0]) == "Смартфон"
    assert str(get_phone[1]) == "Xiaomi"
