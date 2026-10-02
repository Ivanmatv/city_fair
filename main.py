from seller import Seller
from retail_outlet import RetailOutlet

seller1 = Seller("Ваня")
seller2 = Seller("Игорь")

retail_outlet_cross = RetailOutlet("Перекрёсток")
retail_outlet_fifth = RetailOutlet("Пятёрочка")

retail_outlet_cross.add_seller(seller1)
retail_outlet_cross.add_seller(seller2)
retail_outlet_cross.show_retail_outlet_sellers()
print()
retail_outlet_cross.add_product(product="Яблоки", quantity=10)
retail_outlet_cross.add_product(product="Апельсины", quantity=10)
retail_outlet_cross.show_product()
retail_outlet_cross.sale(seller=seller1, product="Яблоки", quantity=5)
retail_outlet_cross.sale(seller=seller1, product="Арбуз", quantity=5)
retail_outlet_cross.show_product()
print()
retail_outlet_cross.delete_seller(seller1)
retail_outlet_cross.show_retail_outlet_sellers()
print()
retail_outlet_fifth.add_seller(seller1)
retail_outlet_fifth.show_retail_outlet_sellers()
