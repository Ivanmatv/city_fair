class Seller:
    def __init__(self, name: str):
        self.__name = name
        self.__products = {}

    def get_name(self) -> str:
        return self.__name

    def add_product(self, product: str, quantity: int):
        if product not in self.__products:
            if quantity > 0 and isinstance(quantity, int):
                self.__products[product] = quantity
            else:
                print("Количество должно быть целым и положительным!")
        else:
            print("Такой товар уже есть!")

    def show_products(self) -> None:
        for product, quantity in self.__products.items():
            print(f"Товар {product} - {quantity} шт")

    def remove_product(self, product: str) -> None:
        if product in self.__products:
            del self.__products[product]
        else:
            print("Такого товара нет!")

    def sale(self, product: str, quantity: int) -> str:
        if product not in self.__products:
            return f"{product} товара нет!"

        product_quantity = self.__products[product]

        if product_quantity != 0:
            if 0 < quantity <= product_quantity:
                self.__products[product] -= quantity
                return f"Продано {product} - {quantity} шт."
            else:
                return "Вы ввели недопустимое значение товара."
        else:
            return "Такого товара нет!"

