from city_fair.seller import Seller


class RetailOutlet:
    def __init__(self, retail_outlet: str):
        self.__retail_outlet: str = retail_outlet
        self.__sellers: list = []
        self.__products = {}

    def get_name(self) -> str:
        return self.__retail_outlet

    def add_seller(self, seller: Seller) -> None:
        seller_name = seller.get_name()
        self.__sellers.append(seller_name)

    def delete_seller(self, seller: Seller) -> None:
        seller_name = seller.get_name()
        self.__sellers.remove(seller_name)

    def show_retail_outlet_sellers(self) -> None:
        formatted_sellers_list = ", ".join(self.__sellers)
        print(
            f"Торговая точка - '{self.__retail_outlet}', "
            f"продавцы: {formatted_sellers_list}"
        )

    def add_product(self, product: str, quantity: int):
        if product not in self.__products:
            if quantity > 0 and isinstance(quantity, int):
                self.__products[product] = quantity
            else:
                print("Количество должно быть целым и положительным!")
        else:
            print("Такой товар уже есть!")

    def show_product(self) -> None:
        for product, quantity in self.__products.items():
            print(f"Товар {product} - {quantity} шт")

    def remove_product(self, product: str) -> None:
        if product in self.__products:
            del self.__products[product]
        else:
            print("Такого товара нет!")

    def sale(self, seller: Seller, product: str, quantity: int) -> None:
        products = seller.sale(
            products=self.__products,
            product=product,
            quantity=quantity
        )

        if isinstance(products, str):
            print(products)
        else:
            self.__products = products
            print(f"Продавец отдаёт - {product} в количестве {quantity} шт")
