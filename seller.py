class Seller:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def sale(self, products: dict, product: str, quantity: int) -> dict | str:
        absence_product = 0
        negative_result_text = ""
        product_quantity = products.get(product)

        if product in products and product_quantity > absence_product:
            if quantity <= product_quantity:
                products[product] -= quantity
                return products
            else:
                negative_result_text = "Вы ввели недопустимое значение товара."
        else:
            negative_result_text = "Такого товара нет!"

        return negative_result_text
