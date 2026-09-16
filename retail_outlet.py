class RetailOutlet:
    def __init__(self, retail_outlet_name: str):
        self.__retail_outlet_name = retail_outlet_name
        self.__sellers = []

    def add_seller(self, seller_name: Seller) -> None:
        self.__sellers.append(seller_name)

    def show_retail_outlet_sellers(self):
        print(
            f"Торговая точка - '{self.__retail_outlet_name}', "
            f"продавцы: {self.__sellers}"
        )

    def delete_seller(self, seller_name: Seller) -> None:
        self.__sellers.remove(seller_name)
