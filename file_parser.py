import pandas as pd
from salesforce_api import SalesForceAPI
from mysecrets import username, password, security_token

class FileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.headers = None
        self.data = []

    def read_excel_file(self):
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(self.file_path, engine='openpyxl')

        # Get the headers and convert them to a list of strings
        headers = df.columns.tolist()

        # Loop through each row and extract the values for each header
        data = []
        for _, row in df.iterrows():
            values = []
            for header in headers:
                values.append(row[header])
            data.append(values)

        return headers, data

    def read_csv_file(self):
        # Read CSV file and extract headers and data
        # ...
        headers = []
        data = []
        self.headers = headers
        self.data = data
        return headers, data

    def parse_file(self):
        # Determine file type and call appropriate read function
        file_type = self.file_path.split(".")[-1]
        if file_type == "xlsx":
            self.headers, self.data = self.read_excel_file()
        elif file_type == "csv":
            self.read_csv_file()
        else:
            raise ValueError("Unsupported file type: {}".format(file_type))

    def get_column_values(self, header):
        # Find the index of the header
        header_index = self.headers.index(header)
        # Get all values for the header
        values = []
        for row in self.data:
            values.append(row[header_index])
        return values



'''
# Open the Excel file
workbook = openpyxl.load_workbook(filename='example.xlsx')

# Select the worksheet you want to work with
worksheet = workbook.active

# Find the header row
header_row = None
for row in worksheet.iter_rows(min_row=1, max_row=1):
    for cell in row:
        if cell.value == 'email':
            header_row = row
            break
    if header_row:
        break

if not header_row:
    print('Could not find header row')
    exit()

# Find the index of the Email column
email_column_index = None
for cell in header_row:
    if cell.value == 'email':
        email_column_index = cell.column
        break

if not email_column_index:
    print('Could not find Email column')
    exit()

# Obtain the access token from Salesforce
my_sf = SalesForceAPI(username, password, security_token)
my_sf.authenticate()

# Iterate all values under the Email header
for row in worksheet.iter_rows(min_row=2):
    email_cell = row[email_column_index - 1]
    email = email_cell.value
    print(email)

    # Retrieve info from contact based on email
    my_contact_id = my_sf.get_contactid_byemail(email)

    # Print contact id
    print (my_contact_id)

# Close the workbook
workbook.close()
'''