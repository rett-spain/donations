import pandas as pd
from salesforce_api import SalesForceAPI
from mysecrets import username, password, security_token

class FileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.rows = []
        self.headers = []

    # Read the Excel file
    def read_excel_file(self):
        # Use Pandas to read the Excel file
        df = pd.read_excel(self.file_path)

        # Store the data and headers in self.rows and self.headers, respectively
        self.rows = df.values.tolist()
        self.headers = df.columns.tolist()

    # Get the values of a column given the name of the header
    def get_column_values(self, header):
        # Get all values for a given header
        header_index = self.headers.index(header)
        values = [row[header_index] for row in self.rows]
        return values

    # Get the value of a specific column in a row given the name of the column
    def get_row_value(self, row, column_name):
        # Get the index of the column
        column_index = self.headers.index(column_name)

        # Return the value in the specified column for the given row
        return row[column_index]

    # Get all donation amounts from the Excel file
    def get_donations(self):
        donations = []
        for row in self.rows:
            donation = {}
            for i, header in enumerate(self.headers):
                donation[header] = row[i]
            donations.append(donation)
        return donations

    # Add contact IDs to the file
    def add_contact_ids(self, sf_contacts):
        # Add the "Contact Id" header to the file
        self.headers.append("contact_id")

        # Loop through all the rows and add the contact ID
        for row in self.rows:
            email = row[self.headers.index("email")]
            for contact in sf_contacts:
                if contact == email:
                    row.append(sf_contacts[contact])
                    break
            else:
                row.append(None)

        # Update the data property with the new rows
        self.data = pd.DataFrame(self.rows, columns=self.headers)

    # Write to file
    def save_file(self, output_file_path):
        # Save the modified data to a new Excel file
        self.data.to_excel(output_file_path, index=False)


'''
    def __init__(self, file_path, header_row=0):
        self.data = pd.read_excel(file_path, header=header_row, engine='openpyxl')
        self.header = list(self.data.columns)
#        self.file_path = file_path
#        self.headers = None
#        self.data = []

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

    def parse_file(self, file_path):
        # Read the data from the file
        self.read_excel_file(file_path)

        # Get the index of the relevant columns
        email_index = self.get_column_index("Email")
        amount_index = self.get_column_index("Amount")
        contact_id_index = self.get_column_index("Contact Id")

        # Get the donations data and upload to Salesforce
        for row in self.data[1:]:
            email = row[email_index]
            amount = row[amount_index]
            contact_id = row[contact_id_index]
            donation = Donation(amount, Contact(email, contact_id))
            self.upload_donations([donation])

    def get_column_values(self, header):
        # Find the index of the header
        header_index = self.headers.index(header)
        # Get all values for the header
        values = []
        for row in self.data:
            values.append(row[header_index])
        return values

    def get_row_values_from_column_name (self, column_name, column_value):
        # Find the index of the column with the given column name
        print (column_name)
        print (column_value)
        print (self.data[0].index)
        column_index = self.data[0].index(column_name)

        # Loop through all the rows and find the row that matches the given column value
        for row in self.data:
            if row[column_index] == column_value:
                return row

        # If no matching row is found, return None
        return None
'''
        

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