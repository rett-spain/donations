from mysecrets import username, password, security_token
from salesforce_api import SalesForceAPI
from file_parser import FileParser


# Obtain the access token from Salesforce
my_sf = SalesForceAPI(username, password, security_token)
my_sf.authenticate()
print(my_sf.sf)

# Define the input and output file names
filename = 'example_with_contact_ids.xlsx'

# Open and parse the input Excel file
file_parser = FileParser(filename)
file_parser.read_excel_file()

# For each row in the output Excel file, create a donation object
donations = file_parser.get_donations()

# Upload the donations to Salesforce
my_sf.upload_donations(donations)
