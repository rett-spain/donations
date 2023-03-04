from mysecrets import username, password, security_token, email_address_1
from npsp_connection import npsp_connection
from donation import Donation
from contact import Contact

# Obtain the access token from Salesforce
my_connection = npsp_connection(username, password, security_token)
my_connection.connect()
print (my_connection.sf)

# Query for the Contact record based on the Email field
my_contact = Contact(my_connection.sf)
my_contact.get_contact_byemail (email_address_1)
print(my_contact.contact_id)
print(my_contact.email_address)
print(my_contact.first_name)
print(my_contact.last_name)

# Query for the Donation record based on the Contact ID and Close Date
my_donation = Donation (my_connection.sf)
my_donation.get_donation_bycontactid_date (my_contact.contact_id, "2023-03-04")
my_donation.delete_donation (my_donation.donation_id)

# Create a new Donation record
donation_name = "Donation 1 test"
donation_amount = 1.23
stage_name = "Closed Won"
close_date = "2023-03-04"
type = "Donación"
aesr_DonationCategory__c = "Bing"
donation = Donation (my_connection.sf, donation_name, donation_amount, stage_name, close_date, type, aesr_DonationCategory__c)
donation.create_donation (my_contact.contact_id)

# Update the Donation record
my_donation_id = '006MI000006ziGpYAI'
donation.update_donation_amount (my_donation_id, 2.45)
donation.update_donation_category (my_donation_id, "Eventos")
donation.update_donation_name (my_donation_id, "Donation 2 test")
donation.update_donation_type (my_donation_id, "Subvención")
print (my_donation_id)

# Delete the Donation record
donation.delete_donation (my_donation_id)