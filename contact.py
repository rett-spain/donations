# Contact
class Contact:

    # Constructor
    def __init__(self) -> None:
        self.contact_id = None
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.email_address = None

    def get_contact_id(self):
        return self.contact_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email_address(self):
        return self.email_address

    def set_contact_id(self, contact_id):
        self.contact_id = contact_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email_address(self, email_address):
        self.email_address = email_address