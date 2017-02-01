from utils import get_valid_input

class Purchase:
    def __init__(self,  price='',  taxes='',  **kwargs):
        super().__init__(**kwargs)
        self._price = price
        self._taxes = taxes
        
    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self._price))
        print("estimated taxes: {}".format(self._taxes))
        
    def prompt_init():
        return dict(price=input("What is the selling price? "), 
        taxes=input("What are the estimated taxes? "))
    
    prompt_init = staticmethod(prompt_init)
    
class Rental:
    def __init__(self,  furnished='',  utilities='', rent='',  **kwargs):
        super().__init__(**kwargs)
        self._furnished = furnished
        self._utilities = utilities
        self._rent = rent
        
    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self._rent))
        print("estimated utilities: {}".format(self._utilities))
        print("furnished: {}".format(self._furnished))
        
    def prompt_init():
        return dict(rent=input("What is the monthly rent? "), 
        utilities=input("What are the estimated utilities? "), 
        furnished=get_valid_input("Is the property furnished?",  ("yes",  "no")))
        
    prompt_init = staticmethod(prompt_init)
