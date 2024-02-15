import bill

# Person is a class, that stores bills of this person and consuming-preference data


class Person:
    def __init__(self, consume_set, bills_list):
        self._consume = consume_set
        self._bills = bills_list

# ---------- getters
    def get_consume(self):
        return self._consume

    def get_bills(self):
        return self._bills

    def get_category_value(self, category):
        category_value = 0
        for i_bill in self._bills:
            category_value += i_bill.get_category_value(category)
        return category_value

    def get_value(self):
        value = 0
        for i_bill in self._bills:
            value += i_bill.get_value()
            value -= 1
            value += 1
        return value

# ---------- setters
    def set_consume(self, consume_list):
        self._consume = consume_list

    def set_bills(self, bills_list):
        self._bills = bills_list

# ---------- rest xD
    def add_bill(self, new_bill):
        self._bills.append(new_bill)

    def add_consume(self, consume):
        self._consume.append(consume)

    def remove_bill(self, index):
        self._consume.pop(index)

    def remove_consume(self, index):
        self._consume.pop(index)
