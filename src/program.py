dbooks = {"Part1":8, "Part2":8, "Part3":8, "Part4":8, "Part5":8}


def get_price(name):
    return dbooks[name]


class Cart:

    cart = {}

    def __init__(self):
        self.cart = {}

    def add_to_cart(self, name, count):
        self.cart[name] = count

    def count_all_items(self):
        return sum(self.cart.values())

    def count_price(self):
        names_of_books = self.cart.keys()
        price = 0

        for name in names_of_books:
            price += dbooks[name]*self.cart[name]
        if len(names_of_books) > self.count_all_items():
            price = price * 0.95
        return price