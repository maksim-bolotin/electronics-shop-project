import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def get_keyboard():
    return [Keyboard('Dark Project KD87A', 9600, 5)]


def test__init__(get_keyboard):
    assert get_keyboard[0].name == "Dark Project KD87A"
    assert get_keyboard[0].price == 9600
    assert get_keyboard[0].quantity == 5
    assert str(get_keyboard[0].language) == "EN"


def test_change_lang(get_keyboard):
    get_keyboard[0].change_lang()
    assert str(get_keyboard[0].language) == "RU"
    get_keyboard[0].change_lang()
    assert str(get_keyboard[0].language) == "EN"
    with pytest.raises(AttributeError):
        get_keyboard[0].language = 'HE'
