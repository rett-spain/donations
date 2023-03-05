from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceAuthenticationFailed, SalesforceMalformedRequest

class SalesForceAPI:
    def __init__(self, username, password, security_token):
        self.username = username
        self.password = password
        self.security_token = security_token
        self.sf = None

    # Authenticate to Salesforce
    def authenticate(self):
        try:
            self.sf = Salesforce (username=self.username, password=self.password, security_token=self.security_token)
            return True
        except Exception as e:
            print(e)
            return False

    # Upload a list of donations to Salesforce
    def upload_donations(self, donations):
        for donation in donations:
            # check if contact exists in Salesforce
            if self.contact_exists(donation.contact_id):
                # upload Donation to Salesforce
                self.upload_donation(donation)
                print (f"Uploaded donation of {donation.donation_amount} for contact with ID {donation.contact_id}")
            else:
                print(f"Contact with ID {donation.contact_id} does not exist in Salesforce")


    # Upload a single donation to Salesforce
    def upload_donation(self, donation):
        try:
            opportunity = self.sf.Opportunity.create({'npsp__Primary_Contact__c': donation.contact_id, 'Name': donation.donation_name, 'Amount': donation.donation_amount, 'StageName': donation.stage_name, 'CloseDate': donation.close_date, 'Type':donation.donation_type, 'aesr_DonationCategory__c': donation.donation_category})
            donation.donation_id = opportunity['id']
            self.sf.OpportunityContactRole.create({'OpportunityId': donation.donation_id, 'ContactId': donation.contact_id})
        except SalesforceMalformedRequest as e:
            print(e)

        return True

    # Check if the contact exists in Salesforce and retrieve the Contact ID and other information related with the contact
    def contact_exists(self, contact_id):
        query = "SELECT Id, FirstName, MiddleName, LastName, Email FROM Contact WHERE Id = '{}'".format(contact_id)
        result = self.sf.query(query)

        # Check if only 1 contact records is returned, otherwise return False
        if result['totalSize'] == 1:
            # Extract the first Contact record from the result set
            return True
        else:
            return False

    # Retrieve contact information from Salesforce based on the contact ID
    def get_contact_byid(self, contact):
        query = "SELECT Id, FirstName, MiddleName, LastName, Email FROM Contact WHERE Id = '{}'".format(contact.contact_id)
        result = self.sf.query(query)

        # Check if only 1 contact records is returned, otherwise return False
        if result['totalSize'] == 1:
            # Extract the first Contact record from the result set
            contact.contact_id = result['records'][0]['Id']
            contact.first_name = result['records'][0]['FirstName']
            contact.middle_name = result['records'][0]['MiddleName']
            contact.last_name = result['records'][0]['LastName']
            contact.email = result['records'][0]['Email']

            return True
        else:
            return False

    # Retrieve contact information from Salesforce based on the contact email address
    def get_contact_byemail(self, contact):
        query = "SELECT Id, FirstName, MiddleName, LastName, Email FROM Contact WHERE Email = '{}'".format(contact.email_address)
        result = self.sf.query(query)

        # Check if only 1 contact records is returned, otherwise return False
        if result['totalSize'] == 1:
            # Extract the first Contact record from the result set
            contact.contact_id = result['records'][0]['Id']
            contact.first_name = result['records'][0]['FirstName']
            contact.middle_name = result['records'][0]['MiddleName']
            contact.last_name = result['records'][0]['LastName']
            contact.email_address = result['records'][0]['Email']

            return True
        else:
            return False