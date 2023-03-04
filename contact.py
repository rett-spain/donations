from simple_salesforce import Salesforce

# Contact
class Contact:

    # Constructor
    def __init__(self, sf_instance: Salesforce) -> None:
        self.sf = sf_instance
        self.first_name = None
        self.last_name = None
        self.email_address = None
        self.contact_id = None

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

    # Get Contact by email
    def get_contact_byemail (self, email_address):
        query = "SELECT Id, FirstName, LastName, Email FROM Contact WHERE Email = '{}'".format(email_address)
        result = self.sf.query(query)

        # Check if any Contact records were returned
        if result['totalSize'] > 0:
            # Extract the first Contact record from the result set
            self.contact_id = result['records'][0]['Id']
            self.email_address = result['records'][0]['Email']
            self.first_name = result['records'][0]['FirstName']
            self.last_name = result['records'][0]['LastName']


