# Class product contains the name, cost and category of the product

class Product:
    # TODO: Determinate category type
    def __init__(self, name: str, cost: float, category):
        self._name = name
        self._cost = cost
        self._category = category

    def set_name(self, new_name: str):
        self._name = new_name

    def set_cost(self, new_cost: float):
        self._cost = new_cost

    # TODO: Determinate category type
    def set_category(self, new_category):
        self._category = new_category

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> float:
        return self._cost

    # TODO: Determinate category type
    def get_category(self):
        return self._category
