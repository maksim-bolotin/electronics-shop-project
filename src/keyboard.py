from src.item import Item


class LanguageMixin:
    """
    Миксин для управления раскладкой клавиатуры.
    """
    def __init__(self):
        self.key_language = "EN"

    def change(self) -> str:
        """
        Метод для смены языка клавиатуры.
        """
        self.key_language = "RU" if self.key_language == "EN" else "EN"
        return self.key_language


class Keyboard(Item, LanguageMixin):
    """
    Класс для товара “клавиатура”.
    """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.key_language = "EN"

    @property
    def language(self) -> str:
        """
        Свойство для получения текущего языка клавиатуры.
        """
        return self.key_language

    @language.setter
    def language(self, value: str):
        """
        Метод сеттера для языка клавиатуры.
        """
        raise AttributeError("AttributeError: property 'language' of 'Keyboard' object has no setter")

    def change_lang(self) -> str:
        """
        Метод для смены языка клавиатуры.
        """
        super().change()
        return self.key_language
