class Item:
    # class level atribute
    pay_rate = 0.8
    all_store = []
    # constrcutor  for Dynamic attribute
    def __init__(self, name: str, price: float,quantity=0):
        # validation
        assert price >= 0, f"price {price} most not be nagetive"
        assert quantity >= 0, f"quantity {quantity} most not be nagetive"
        #  action
        self.name  = name
        self.price = price
        self.quantity  = quantity
        # to store
        Item.all_store.append(self)
    #  method
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"
        
# instance of class (objects)
item1 = Item("Phone", 100, 1)
item2 = Item("Labtop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("keyboard", 75, 5)

print(Item.all_store)


 