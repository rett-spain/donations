from mysecrets import username, password, security_token, email_address_1
from simple_salesforce import Salesforce, SalesforceMalformedRequest

# Query for the Contact record based on the Email field
def get_contact (sf, email_address):
    query = "SELECT Id, FirstName, LastName, Email FROM Contact WHERE Email = '{}'".format(email_address)
    result = sf.query(query)

    # Check if any Contact records were returned
    if result['totalSize'] > 0:
        # Extract the first Contact record from the result set
        contact = result['records'][0]

    # Return the Contact record
    return contact


# Query for all Opportunity records associated with the Contact record
def get_donations(sf, contact_id):
    # Query for all Opportunity records associated with the Contact record
    query = f"SELECT Opportunity.Id, Opportunity.Name, Opportunity.Amount FROM OpportunityContactRole WHERE ContactId = '{contact_id}'"

    # Execute the query and return the results
    results = sf.query_all(query)

    # Extract the Opportunity records from the results
    donations = []
    for record in results['records']:
        donations.append({'id': record['Opportunity']['Id'], 'name': record['Opportunity']['Name'], 'amount': record['Opportunity']['Amount']})
    
    return donations

# Add a new donation to the Contact record
def add_donation(sf, contact_id, donation_name, donation_amount, stage_name, close_date, type, aesr_DonationCategory__c):
    try:
        # Create a new Opportunity record
        opportunity = sf.Opportunity.create({'npsp__Primary_Contact__c': contact_id, 'Name': donation_name, 'Amount': donation_amount, 'StageName': stage_name, 'CloseDate': close_date, 'Type':type, 'aesr_DonationCategory__c': aesr_DonationCategory__c})
        opportunity_id = opportunity['id']
        sf.OpportunityContactRole.create({'OpportunityId': opportunity_id, 'ContactId': contact_id})
    except SalesforceMalformedRequest as e:
        print(e)


# Obtain the access token from Salesforce
sf = Salesforce (username, password, security_token)

# Query for the Contact record based on the Email field
# email_address = 'martinalamolla13@gmail.com'
#email_address = input("Enter email address: ")
my_contact = get_contact(sf, email_address_1)
print(my_contact)

# Query for all Opportunity records associated with the Contact record
donations = get_donations(sf, my_contact['Id'])
print (donations)

# Add a new donation to the Contact record
donation = {
    'donation_name': 'Donation 1 test',
    'donation_amount': 23.45,
    'stage_name': 'Closed Won',
    'close_date': '2023-03-04',
    'type': 'Donación',
    'aesr_DonationCategory__c': 'Bing'
}
donation_name = "Donation 1 test"
donation_amount = 23.45
stage_name = "Closed Won"
close_date = "2023-03-04"
type = "Donación"
aesr_DonationCategory__c = "Bing"
add_donation(sf, my_contact['Id'], donation_name, donation_amount, stage_name, close_date, type, aesr_DonationCategory__c)

# Query for all Opportunity records associated with the Contact record
donations = get_donations(sf, my_contact['Id'])
print (donations)

# Query for all Opportunity records associated with the Contact record
donations = get_donations(sf, my_contact['Id'])
print (donations)