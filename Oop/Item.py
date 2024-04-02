import csv
 
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
        self.__name  = name
        self.__price = price
        self.quantity  = quantity
        # to store
        Item.all_store.append(self)
    # read only
    @property
    def name(self):
        return self.__name
        
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value 

    @name.setter
    def name(self, value):
        self.__name = value
    #  method
    def calculate_total_price(self):
        return self.price * self.quantity
    
    # Class level method
    @classmethod
    def instantiate_from_csv(cls):
        '''
        this should also do something that has relationship with the class but usually, those are used to
        manifulate different structures of data to instantiate objects 
        '''
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )
    @staticmethod
    def is_interger(num):
        '''
        this should do something that has a relationhip with the class
        but not something that must be unique per instance(Object)
        '''
        # check decimal
        if isinstance(num, float):
            # Count out the . digit
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"