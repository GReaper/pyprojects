from utils import get_valid_input
from operations import Purchase,  Rental
    
class Property:
    def __init__(self,  square_feet='',  beds='',  baths='',  **kwargs):
        super().__init__(**kwargs)
        self._square_feet = square_feet
        self._num_bedrooms = beds
        self._num_baths = baths
        
    def display(self):
        print()
        print("================")
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self._square_feet))
        print("bedrooms: {}".format(self._num_bedrooms))
        print("bathrooms: {}".format(self._num_baths))
        print()
        
    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "), 
        beds=input("Enter the number of bedrooms: "), 
        baths=input("Enter the number of baths: "))
        
    prompt_init = staticmethod(prompt_init)
        
class Apartment(Property):
    valid_laundries =("coin",  "ensuite",  "none")
    valid_balconies = ("yes",  "no",  "solarium")
    
    def __init__(self,  balcony='',  laundry='',  **kwargs):
        super().__init__(**kwargs)
        self._balcony = balcony
        self._laundry = laundry
        
    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self._laundry)
        print("balcony: %s" % self._balcony)
        
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have?",  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?",  Apartment.valid_balconies)
        parent_init.update({'laundry': laundry, 
                                    'balcony': balcony})
        return parent_init
        
    prompt_init = staticmethod(prompt_init)
        
class House(Property):
    valid_garage = ("attached",  "detached",  "none")
    valid_fenced = ("yes",  "no")
    
    def __init__(self,   num_stories='',  garage='',  fenced='',  **kwargs):
        super().__init__(**kwargs)
        self._garage = garage
        self._fenced = fenced
        self._num_stories = num_stories
        
    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self._num_stories))
        print("garage: {}".format(self._garage))
        print("fenced yard: {}".format(self._fenced))
        
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced?",  House.valid_fenced)
        garage = get_valid_input("Is there a garage?",  House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({'fenced': fenced, 
                                    'garage': garage, 
                                    'num_stories':  num_stories})
        return parent_init
        
    prompt_init = staticmethod(prompt_init)
    
class HouseRental(Rental,  House):
    '''Rental and House inheritance order is important because, if we had put House, Rental, when calling the display() method,
    the Rental.display() method would not be called. With the current order, display() refers to the Rental version, which calls
    super.display() to get the House version, which again calls super.display() to get the Property version. If we reverse it, display()
    would refer to the House class display(). When super is called, it calls the method on the  Property parent class. But Property does
    not have a call to super in its display method. This means Rental class display() method would not be called. It is also important
    to notice that we cannot put a super().display() call in Property, because the superclass of Property is object, which does not
    have a display() method.'''
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
        
    prompt_init = staticmethod(prompt_init)
    
class ApartmentRental(Rental,  Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
        
    prompt_init = staticmethod(prompt_init)
    
class HousePurchase(Purchase,  House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
        
    prompt_init = staticmethod(prompt_init)
    
class ApartmentPurchase(Purchase,  Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
        
    prompt_init = staticmethod(prompt_init)
    
