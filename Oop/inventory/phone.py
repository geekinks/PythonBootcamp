from Item import Item

class Phone(Item): 
    # constructor
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
    # validate
        assert broken_phones >=0, f"Broken phones {broken_phones} is must not be nagetive" 
        self.broken_phone = broken_phones
    
    def increment_price(self, increase):
        assert increase >= 0, f"Increase {increase} must not be negative"
        self.price += increase
    
    @classmethod
    def calculate_total_broken_phones(cls):
        total_broken_phones = 0
        for phone in cls.all_store:
            total_broken_phones += phone.broken_phone
        return total_broken_phones