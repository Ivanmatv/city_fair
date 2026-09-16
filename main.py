from seller import Seller
from retail_outlet import RetailOutlet

seller1 = Seller("Ваня")
seller2 = Seller("Игорь")

retail_outlet_apple = RetailOutlet("Яблоки")
retail_outlet_orange = RetailOutlet("Апельсины")

retail_outlet_apple.add_seller(seller1)
retail_outlet_apple.add_seller(seller2)
retail_outlet_apple.show_retail_outlet_sellers()

retail_outlet_apple.delete_seller(seller1)
retail_outlet_apple.show_retail_outlet_sellers()

retail_outlet_orange.add_seller(seller1)
retail_outlet_orange.show_retail_outlet_sellers()
