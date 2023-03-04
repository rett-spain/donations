from mysecrets import username, password, security_token

# Obtain the access token from Salesforce
from simple_salesforce import Salesforce
sf = Salesforce (username, password, security_token)

# Query for all Contact records and print the results
query = "SELECT Id, FirstName, LastName, Email FROM Contact"
contacts = sf.query_all(query)['records']
for contact in contacts:
    print(contact)

# Query for the Contact record based on the Email field
email_address = 'pedrojrocha@outlook.com'
query = "SELECT Id, FirstName, LastName, Email FROM Contact WHERE Email = '{}'".format(email_address)
result = sf.query(query)

# Check if any Contact records were returned
if result['totalSize'] == 0:
    print("No Contact found with email address: {}".format(email_address))
else:
    # Extract the first Contact record from the result set
    contact = result['records'][0]

    # Print the Contact record's information
    print("Contact found with email address: {}".format(email_address))
    print("First Name: {}".format(contact['FirstName']))
    print("Last Name: {}".format(contact['LastName']))
    print("Email: {}".format(contact['Email']))