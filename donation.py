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
