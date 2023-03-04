from simple_salesforce import Salesforce, SalesforceMalformedRequest

# Donation
class Donation:

    # Constructor
    def __init__(self, sf_instance: Salesforce, donation_name, donation_amount, stage_name, close_date, donation_type, aesr_DonationCategory__c) -> None:
        self.sf = sf_instance
        self.donation_name = donation_name
        self.donation_amount = donation_amount
        self.stage_name = stage_name
        self.close_date = close_date
        self.donation_type = donation_type
        self.aesr_DonationCategory__c = aesr_DonationCategory__c
        self.donation_id = None

    # Constructor
    def __init__(self, sf_instance: Salesforce) -> None:
        self.sf = sf_instance
        self.donation_name = None
        self.donation_amount = None
        self.stage_name = None
        self.close_date = None
        self.donation_type = None
        self.aesr_DonationCategory__c = None
        self.donation_id = None

    def get_sf(self):
        return self.sf

    def get_donation_id(self):
        return self.donation_id

    def get_donation_amount(self):
        return self.donation_amount

    def get_stage_name(self):
        return self.stage_name

    def get_close_date(self):
        return self.close_date

    def get_donation_type(self):
        return self.donation_type
    
    def get_aesr_DonationCategory__c(self):
        return self.aesr_DonationCategory__c

    # Create Donation
    def create_donation (self, contact_id):
        try:
            opportunity = self.sf.Opportunity.create({'npsp__Primary_Contact__c': contact_id, 'Name': self.donation_name, 'Amount': self.donation_amount, 'StageName': self.stage_name, 'CloseDate': self.close_date, 'Type':self.donation_type, 'aesr_DonationCategory__c': self.aesr_DonationCategory__c})
            self.donation_id = opportunity['id']
            self.sf.OpportunityContactRole.create({'OpportunityId': self.donation_id, 'ContactId': contact_id})
        except SalesforceMalformedRequest as e:
            print(e)

    # Update Donation amount
    def update_donation_amount (self, donation_id, new_donation_amount):
        try:
            opportunity = self.sf.Opportunity.update(donation_id, {'Amount': new_donation_amount})
        except SalesforceMalformedRequest as e:
            print(e)

    # Update Donation name
    def update_donation_name (self, donation_id, new_donation_name):
        try:
            opportunity = self.sf.Opportunity.update(donation_id, {'Name': new_donation_name})
        except SalesforceMalformedRequest as e:
            print(e)

    # Update Donation type
    def update_donation_type (self, donation_id, new_donation_type):
        try:
            opportunity = self.sf.Opportunity.update(donation_id, {'Type': new_donation_type})
        except SalesforceMalformedRequest as e:
            print(e)

    # Update Donation category
    def update_donation_category (self, donation_id, new_donation_category):            
        try:
            opportunity = self.sf.Opportunity.update(donation_id, {'aesr_DonationCategory__c': new_donation_category})
        except SalesforceMalformedRequest as e:
            print(e)

    # Delete Donation
    def delete_donation (self, donation_id):
        try:
            if donation_id is not None:
                opportunity = self.sf.Opportunity.delete(donation_id)
        except SalesforceMalformedRequest as e:
            print(e)

    # Get Donation by ID
    def get_donation_byid (self, donation_id):
        try:
            opportunity = self.sf.Opportunity.get(donation_id)
            self.donation_id = opportunity['Id']
            self.donation_name = opportunity['Name']
            self.donation_amount = opportunity['Amount']
            self.stage_name = opportunity['StageName']
            self.close_date = opportunity['CloseDate']
            self.donation_type = opportunity['Type']
            self.aesr_DonationCategory__c = opportunity['aesr_DonationCategory__c']
        except SalesforceMalformedRequest as e:
            print(e)

    # Get Donation by contact ID and date
    def get_donation_bycontactid_date (self, contact_id, close_date):
        try:
            query = "SELECT Id, Name, Amount, StageName, CloseDate, Type, aesr_DonationCategory__c FROM Opportunity WHERE npsp__Primary_Contact__c = '{}' AND CloseDate = {}".format(contact_id, close_date)
            result = self.sf.query(query)

            # Check if any Donation records were returned
            if result['totalSize'] > 0:
                # Extract the first Donation record from the result set
                self.donation_id = result['records'][0]['Id']
                self.donation_name = result['records'][0]['Name']
                self.donation_amount = result['records'][0]['Amount']
                self.stage_name = result['records'][0]['StageName']
                self.close_date = result['records'][0]['CloseDate']
                self.donation_type = result['records'][0]['Type']
                self.aesr_DonationCategory__c = result['records'][0]['aesr_DonationCategory__c']
        except SalesforceMalformedRequest as e:
            print(e)