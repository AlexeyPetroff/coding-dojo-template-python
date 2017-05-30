books_prices = {"Part1": 8, "Part2": 8, "Part3": 8, "Part4": 8, "Part5": 8}


def get_price(name):
    return books_prices[name]


class Cart:
    cart = {}

    def __init__(self):
        self.cart = {}

    def add_to_cart(self, name, count):
        self.cart[name] = count

    def count_all_items(self):
        return sum(self.cart.values())

    def count_price(self):
        cart_temp = self.cart
        names_of_books = self.cart.keys()
        price = 0
        sets = []
        for piece in names_of_books:
            while cart_temp[piece] > 0:
                create_new = True
                for one_set in sets:
                    if piece not in one_set:
                        one_set.append(piece)
                        create_new = False
                        break
                if create_new:
                    new_set = [piece]
                    sets.append(new_set)
                cart_temp[piece] -= 1
        for one_set in sets:
            set_price = 0
            for book in one_set:
                set_price += books_prices[book]
            if len(one_set) == 2:
                set_price = set_price * 0.95
            elif len(one_set) == 3:
                set_price = set_price * 0.9
            elif len(one_set) == 4:
                set_price = set_price * 0.8
            elif len(one_set) == 5:
                set_price = set_price * 0.75
            price += set_price
        return price
