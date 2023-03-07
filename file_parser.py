import pandas as pd

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

    # Get all donation from the Excel file
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
