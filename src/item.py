from csv import DictReader


class InstantiateCSVError(Exception):

    def __init__(self, message):
        self.message = message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> str:
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]
            raise Exception("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, csv='items.csv'):
        """
        Метод, инициализирующий экземпляры класса Item данными из файла.
        """
        try:
            with open(csv, newline='') as csvfile:
                csv_reader = DictReader(csvfile)
                if len(csv_reader.fieldnames) < 3:
                    raise InstantiateCSVError("Файл item.csv поврежден")
                for row in csv_reader:
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(some_line) -> int:
        """
        Метод, возвращающий число из числа-строки.
        """
        try:
            return int(float(some_line))
        except (ValueError, TypeError):
            return None

    def __add__(self, other) -> int:
        """Метод реализующий сложение экземпляров класса.
        Осуществляет проверку принадлежности экземпляра к классу Item.
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить экземпляр класса Item(или его наследников) с экземпляром иного класса.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"
