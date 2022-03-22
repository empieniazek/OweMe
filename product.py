# Class product contains the name, cost and category of the product

class Product:
    def __init__(self, name, cost, category=0):
        self._name = name
        self._cost = cost
        self._category = category

    def set_name(self, new_name):
        self._name = new_name

    def set_cost(self, new_cost):
        self._cost = new_cost

    def set_category(self, new_category):
        self._category = new_category

    def get_name(self):
        return self._name

    def get_cost(self):
        return self._cost

    def get_category(self):
        return self._category
