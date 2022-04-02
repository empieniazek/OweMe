import product

# Class bill contains all products of the bill


class Bill:
    def __init__(self, products_list: list):
        self._products = products_list

    def set_products(self, products_list: list):
        self._products = products_list

    def get_category_value(self, category) -> float:
        category_value = 0.0
        for i_product in self._products:
            if i_product.get_category() == category:
                category_value += i_product.get_cost
        return category_value

    def get_value(self) -> float:
        bill_value = 0.0
        for i_product in self._products:
            bill_value += i_product.get_cost()
        return bill_value

    def get_products(self) -> list:
        return self._products

    def add_product(self, new_product: product.Product):
        self._products.append(new_product)

    def pop_product(self, index: int):
        self._products.pop(index)

    def remove_product(self, name: str):
        for index, i_product in enumerate(self._products):
            if i_product.get_name() == name:
                self._products.pop(index)
                break
