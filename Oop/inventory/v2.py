# class defination
class Item:
    def calculate_total_price(self, x,y):
        return x * y


# instance of class (Real object
item1 = Item()
# attribute of instance 
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

bill1 = item1.calculate_total_price(item1.price, item1.quantity)


item2 = Item()
# attribute of instance 
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
bill2 =item2.calculate_total_price(item2.price, item2.quantity)


print(f'the bills for item1 {bill1} and {bill2} for item2')