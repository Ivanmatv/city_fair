from city_fair.seller import Seller


class RetailOutlet:
    def __init__(self, retail_outlet_name: str):
        self.__retail_outlet_name = retail_outlet_name
        self.__sellers = []

    def add_seller(self, seller: Seller) -> None:
        seller_name = seller.get_name()
        self.__sellers.append(seller_name)

    def show_retail_outlet_sellers(self):
        formatted_sellers_list = ", ".join(self.__sellers)
        print(
            f"Торговая точка - '{self.__retail_outlet_name}', "
            f"продавцы: {formatted_sellers_list}"
        )

    def delete_seller(self, seller: Seller) -> None:
        seller_name = seller.get_name()
        self.__sellers.remove(seller_name)
