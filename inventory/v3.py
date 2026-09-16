class Item:
    # class level atribute
    pay_rate = 0.8
    # constrcutor  for Dynamic attribute
    def __init__(self, name: str, price: float,quantity=0):
        # validation
        assert price >= 0, f"price {price} most not be nagetive"
        assert quantity >= 0, f"quantity {quantity} most not be nagetive"
        
        self.name  = name
        self.price = price
        self.quantity  = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
item1 = Item("Phone", 100, 5)
item2 = Item("Labtop", 1000, 3)
item2.has_numpad = False

# print(f'the total bill for item1 is {item1.calculate_total_price()}')
# print(f'the total bill for item2 is {item2.calculate_total_price()}')

# print(Item.__dict__) # all attribute at class level
# print(item1.__dict__) # all attribute at instance Level


 