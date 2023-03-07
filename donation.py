# Donation
class Donation:

    # Constructor
    def __init__(self, donation_name, donation_amount, stage_name, close_date, donation_type, donation_category, contact_id) -> None:
        self.donation_name = donation_name
        self.donation_amount = donation_amount
        self.stage_name = stage_name
        self.close_date = close_date
        self.donation_type = donation_type
        self.donation_category = donation_category
        self.contact_id = contact_id
        self.donation_id = None

    def get_donation_name(self):
        return self.donation_name

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
    
    def get_donation_category(self):
        return self.donation_category

    def set_donation_name(self, donation_name):
        self.donation_name = donation_name

    def set_donation_amount(self, donation_amount):
        self.donation_amount = donation_amount

    def set_stage_name(self, stage_name):
        self.stage_name = stage_name

    def set_close_date(self, close_date):
        self.close_date = close_date

    def set_donation_type(self, donation_type):
        self.donation_type = donation_type

    def set_donation_category(self, donation_category):
        self.donation_category = donation_category