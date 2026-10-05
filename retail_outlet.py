from city_fair.seller import Seller


class RetailOutlet:
    def __init__(self, retail_outlet: str):
        self.__retail_outlet: str = retail_outlet
        self.__sellers: list = []

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

    def show_products(self, seller: Seller) -> None:
        seller.show_products()

    def sale(self, seller: Seller, product: str, quantity: int) -> None:
        products = seller.sale(
            product=product,
            quantity=quantity
        )
        result_text = products
        print(f"{result_text}")