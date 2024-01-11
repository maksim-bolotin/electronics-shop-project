"""Здесь надо написать тесты с использованием pytest для модуля Phone."""
import pytest
from src.item import Item


@pytest.fixture()
def get_item():
    Item.all.clear()
    Item.pay_rate = 0.7
    return [Item("Смартфон", 10000, 20), Item("Бритва", "", 1)]


def test_calculate_total_price(get_item):
    assert get_item[0].calculate_total_price() == 200000
    with pytest.raises(Exception):
        assert get_item[1].calculate_total_price() is Exception


def test_apply_discount(get_item):
    get_item[0].apply_discount()
    assert get_item[0].price == 7000


def test__init__(get_item):
    assert get_item[0].name == "Смартфон"
    assert get_item[1].name == "Бритва"
    assert get_item[0].price == 10000
    assert get_item[0].quantity == 20
    assert len(get_item[0].all) == 2


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('') is ValueError
    assert Item.string_to_number('5.5') == 5


def test__repr__(get_item):
    assert repr(get_item[0]) == "Item('Смартфон', 10000, 20)"
    assert repr(get_item[1]) == "Item('Бритва', , 1)"


def test__str__(get_item):
    assert str(get_item[0]) == "Смартфон"
    assert str(get_item[1]) == "Бритва"


def test__add__(get_item):
    assert get_item[0] + get_item[1] == 21
