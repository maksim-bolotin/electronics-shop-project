from src.item import Item


class Phone(Item):
    """
    Класс для представления конкретного вида товара (Phone).
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса.
        """
        super().__init__(name, price, quantity)
        self.sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        """
        Геттер возвращает значение self.sim.
        """
        return self.sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        """
        Сеттер для проверки количества физических SIM-карт.
        """
        if value > 0:
            self.sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
