# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

# class definition
class Item: 
    #  constructor for Dynamic attribute

    def __init__(self, name: str, price: float,quantity=0):
        # validation
        assert price >= 0, f"price {price} most not be nagetive"
        assert quantity >= 0, f"quantity {quantity} most not be nagetive"
        #  action
        self.name  = name
        self.price = price
        self.quantity  = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

# object creation

item1 = Item("Phone", 100, 5)
item1.calculate_total_price()

item2 = Item("Laptop", 1000, 3)
item2.calculate_total_price()



#  access
print(f"we have {item1.name} that costs {item1.price} in order {item1.quantity}")

print(f"the total bill for item1 is {item1.calculate_total_price()}")


