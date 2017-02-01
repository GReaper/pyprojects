class Contact1:
    _all_contacts = []
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact1._all_contacts.append(self)
        
class Suplier(Contact1):
    def order(self,  order):
        print("If this were a real system we sould send {} order to {}".format(order,  self.name))
        
class ContactList(list):
    def search(self,  name):
        '''Return all contacts that contain the search value in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
        
class Contact2:
    _all_contacts = ContactList()
    
    def __init__(self, name='', email='',  **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self._all_contacts.append(self)
        
class Friend(Contact2):
    def __init__(self,  name,  email,  phone):
        super.__init__(name,  email)
        self.phone = phone
        
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
        
class MailSender:
    '''Mixin example'''
    def send_mail(self,  message):
        print("Sending mail to "+ self.email)
        # Add the email logic here
        
class EmailableContact(Contact2,  MailSender):
    pass
    
class AddressHolder:
    def __init__(self,  street='',  city='',  state='',  code=''):
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        
class MultipleInheritanceFriend(Contact2, AddressHolder):
    def __init__(self, phone='', **kwargs):
        '''**kwargs constructor is needed to avoid a Diamond Problem. This way, both constructors are called only once and with the right params (which must be differente keyword arguments).'''
        super().__init__(**kwargs)
        self.phone = phone
        
