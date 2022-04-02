import bill

# Person is a class, that stores bills of this person and consuming-preference data


class Person:
    # TODO: consume set - determinate type
    def __init__(self, ps_categories_set, bills_list: list):
        self._ps_categories = ps_categories_set
        self._bills = bills_list

# ---------- getters
    # TODO: check type (if ps_categories format was changed)
    def get_ps_categories(self) -> list:
        return self._ps_categories

    def get_bills(self) -> list:
        return self._bills

    # TODO: determinate type
    def get_category_value(self, category) -> float:
        category_value = 0.0
        for i_bill in self._bills:
            category_value += i_bill.get_category_value(category)
        return category_value

    def get_value(self) -> float:
        value = 0.0
        for i_bill in self._bills:
            value += i_bill.get_value()
        return value

# ---------- setters
    # TODO: check type (if ps_categories format was changed)
    def set_ps_categories(self, ps_categories_set: list):
        self._ps_categories = ps_categories_set

    def set_bills(self, bills_list: list):
        self._bills = bills_list

# ---------- Add/Remove
    def add_bill(self, new_bill: bill.Bill):
        self._bills.append(new_bill)

    # TODO: Determinate type
    def add_ps_categories(self, category):
        self._ps_categories.append(category)

    def remove_bill(self, index: int):
        self._ps_categories.pop(index)

    def remove_ps_categories(self, index: int):
        self._ps_categories.pop(index)
