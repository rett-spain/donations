from mysecrets import username, password, security_token
from salesforce_api import SalesForceAPI
from file_parser import FileParser


# Obtain the access token from Salesforce
my_sf = SalesForceAPI(username, password, security_token)
my_sf.authenticate()
print(my_sf.sf)

# Define the input and output file names
input_filename = 'example.xlsx'
output_filename = 'example_with_contact_ids.xlsx'

# Open and parse the input Excel file
file_parser = FileParser(input_filename)
file_parser.read_excel_file()

# Get all contact ids from Salesforce based on the emails in the Excel file
all_contact_ids = my_sf.get_contactids_byemail(file_parser.get_column_values('email'))

# Get all contacts ids from Salesforce based on the names in the Excel file
all_contact_ids = my_sf.get_contactids_byname(file_parser.get_column_values('name'))

# Add the contact ids to an output Excel file
file_parser.add_contact_ids(all_contact_ids)
file_parser.save_file(output_filename)
