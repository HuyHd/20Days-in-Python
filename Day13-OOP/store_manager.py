from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, manufacturer, stock) -> None:
        self._name = name
        self._price = price
        self._manufacturer = manufacturer
        self._stock = stock

    @abstractmethod
    def get_describe(self):
        return self._name, self._price, self._manufacturer, self._stock

    def set_info(self, new_name, new_price, new_manufacturer, new_stock):
        self._name = new_name
        self._price = new_price
        self._manufacturer = new_manufacturer
        self._stock = new_stock


class Phone(Product):
    def __init__(self, name, price, manufacturer, stock, screen_size) -> None:
        super().__init__(name, price, manufacturer, stock)
        self._screen_size = screen_size

    def get_describe(self):
        return super().get_describe(), self._screen_size


class Laptop(Product):
    def __init__(self, name, price, manufacturer, stock, weight) -> None:
        super().__init__(name, price, manufacturer, stock)
        self._weight = weight

    def get_describe(self):
        return super().get_describe(), self._weight


class TV(Product):
    def __init__(self, name, price, manufacturer, stock, screen_type) -> None:
        super().__init__(name, price, manufacturer, stock)
        self._screen_type = screen_type

    def get_describe(self):
        return super().get_describe(), self._screen_type


class Oder():
    def __init__(self, customer_name) -> None:
        self._customer_name = customer_name
        self._products = {}

    def add_products(self, product_name, quantity):
        if product_name in self._products:
            self._products[product_name] += quantity
        else:
            self._products[product_name] = quantity

    def get_total(self, price_dict):
        total = 0
        for product_name, quantity in self._products.items():
            if product_name in price_dict:
                total += price_dict[product_name]*quantity
        return total

    def generate_invoice(self, price_dict):
        for product_name, quantity in self._products.items():
            if product_name in price_dict:
                total_product_price = price_dict[product_name] * quantity
                print(f"- {product_name} x {quantity}: {total_product_price} USD")
        total_order_price = self.get_total(price_dict)
        print(f"Total amount: {total_order_price} USD")


# Testcases:
if __name__ == "__main__":
    phone1 = Phone("iPhone 12", 1000, "Apple", 30, "6.1 inch")
    laptop1 = Laptop("Dell XPS 13", 1200, "Dell", 50, "1.2 kg")
    tv1 = TV("Samsung QLED", 1500, "Samsung", 5, "QLED")
    print(phone1.get_describe())
    print(laptop1.get_describe())
    print(tv1.get_describe())
    print()
    price_list = {
        "Laptop": laptop1._price,
        "Phone": phone1._price,
        "TV": tv1._price}
    order1 = Oder("John")
    order1.add_products("Laptop", 2)
    order1.add_products("Phone", 3)
    print("Order of", order1._customer_name)
    order1.generate_invoice(price_list)
