import product

# Class bill contains all products of the bill


class Bill:
    def __init__(self, products_list):
        self._products = products_list

    def set_products(self, products_list):
        self._products = products_list

    def get_category_value(self, category):
        category_value = 0
        for i_product in self._products:
            if i_product.get_category() == category:
                category_value += i_product.get_cost
        return category_value

    def get_value(self):
        bill_value = 0
        for i_product in self._products:
            bill_value += i_product.get_cost()

    def get_products(self):
        return self._products

    def add_product(self, new_product):
        self._products.append(new_product)

    def pop_product(self, index):
        self._products.pop(index)

    def remove_product(self, name):
        for index, i_product in enumerate(self._products):
            if i_product.get_name() == name:
                self._products.pop(index)
                break
