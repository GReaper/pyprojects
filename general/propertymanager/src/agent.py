from properties import HousePurchase,  HouseRental,  ApartmentPurchase,  ApartmentRental
from utils import get_valid_input

class Agent:
    type_map = {("house",  "rental"): HouseRental, 
    ("house",  "purchase"): HousePurchase, 
    ("apartment",  "rental"): ApartmentRental, 
    ("apartment",  "purchase"): ApartmentPurchase}
    
    def __init__(self):
        self._property_list = []
        
    def display(self):
        for property in self._property_list:
            property.display()
            
    def add_property(self):
        property_type = get_valid_input("What type of property?",  ("house",  "apartment")).lower()
        payment_type = get_valid_input("What payment type?",  ("rental",  "purchase")).lower()
        PropertyClass = self.type_map[(property_type,  payment_type)]
        init_args = PropertyClass.prompt_init()
        self._property_list.append(PropertyClass(**init_args))
