from mysecrets import username, password, security_token
from salesforce_api import SalesForceAPI


def print_results(results):
    for result in results['searchRecords']:
        print(f"Name: {result['FirstName']} {result['LastName']}")
        print(f"Phone: {result['Phone']}")
        print(f"Email: {result['Email']}")
        print(f"Id: {result['Id']}")
        print()

# Obtain the access token from Salesforce
my_sf = SalesForceAPI(username, password, security_token)
my_sf.authenticate()

# Get the contact information by generic search
generic_info = input("Enter the generic info:")
result = my_sf.get_contactid_bygeneric (generic_info)

# Print the results
print_results (result)