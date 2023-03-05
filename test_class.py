from mysecrets import username, password, security_token, email_address_1
from salesforce_api import SalesForceAPI
from donation import Donation
from contact import Contact

# Obtain the access token from Salesforce
my_sf = SalesForceAPI(username, password, security_token)
my_sf.authenticate()
print (my_sf.sf)

# Let's use 3 contact ids as example
contact_id1 = "0033X00002rGwc3"
contact_id2 = "0033X00002rGwc6"
contact_id3 = "0033X00002rGwc7"

# Retrieve info from contact based on contact ID
my_contact = Contact()
my_contact.contact_id = contact_id1
my_sf.get_contact_byid(my_contact)

# Retrieve info from contact based on email
my_other_contact = Contact()
my_other_contact.email_address = email_address_1
my_sf.get_contact_byemail(my_other_contact)

# Create donation information
donation_name = "Donation 1 test"
donation_amount = 1.23
stage_name = "Closed Won"
close_date = "2023-03-04"
donation_type = "Donación"
donation_category = "Bing"

# Create a list of donations
donations = []
my_donation1 = Donation(donation_name, donation_amount, stage_name, close_date, donation_type, donation_category, contact_id1)
donations.append(my_donation1)
my_donation2 = Donation(donation_name, donation_amount, stage_name, close_date, donation_type, donation_category, contact_id2)
donations.append(my_donation2)
my_donation3 = Donation(donation_name, donation_amount, stage_name, close_date, donation_type, donation_category, contact_id3)
donations.append(my_donation3)

# Upload the donations to Salesforce
my_sf.upload_donations(donations)