from city_fair.retail_outlet import RetailOutlet


class CityDistrict:
    def __init__(self, name: str):
        self.__name = name
        self.__retail_outlets: list = []

    def get_name_district(self) -> str:
        return self.__name

    def add_retail_outlet(self, retail_outlet: RetailOutlet):
        self.__retail_outlets.append(retail_outlet)

    def get_retail_outlets(self) -> list:
        return self.__retail_outlets

    def show_retail_outlets(self):
        for retail_outlet in self.__retail_outlets:
            print(f"- {retail_outlet.get_name()}")
