"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def get_item():
    Item.pay_rate = 0.7
    return [Item("Смартфон", 10000, 20), Item("Бритва", "", "1")]


def test_calculate_total_price(get_item):
    assert get_item[0].calculate_total_price() == 200000
    with pytest.raises(Exception):
        get_item[1].calculate_total_price()


def test_apply_discount(get_item):
    get_item[0].apply_discount()
    assert get_item[0].price == 7000


def test__init__(get_item):
    assert get_item[0].name == "Смартфон"
    assert get_item[1].name == "Бритва"
    assert get_item[0].price == 10000
    assert get_item[0].quantity == 20
    assert len(get_item[0].all) == 6
