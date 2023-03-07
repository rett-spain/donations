import sys
import os

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the modules that will be tested
from file_parser import FileParser

# Test the FileParser class
def test_file_parser_init():
    file_parser = FileParser("test_file.xlsx")
    assert file_parser.file_path == "test_file.xlsx"
    assert file_parser.rows == []
    assert file_parser.headers == []

def test_read_excel_file():
    file_parser = FileParser("tests/test_file.xlsx")
    file_parser.read_excel_file()
    assert len(file_parser.rows) > 0
    assert len(file_parser.headers) > 0

def test_get_column_values():
    file_parser = FileParser("tests/test_file.xlsx")
    file_parser.read_excel_file()
    column_values = file_parser.get_column_values("Column1")
    assert len(column_values) == len(file_parser.rows)

import unittest

class TestFileParser(unittest.TestCase):
    def setUp(self):
        self.file_path = 'tests/test_file.xlsx'
        self.file_parser = FileParser(self.file_path)
        self.file_parser.read_excel_file()

    def test_get_row_value(self):
        # Test getting a value from the first row
        row = self.file_parser.rows[0]
        column_name = self.file_parser.headers[0]
        expected_value = row[0]
        self.assertEqual(self.file_parser.get_row_value(row, column_name), expected_value)

        # Test getting a value from the last row
        row = self.file_parser.rows[-1]
        column_name = self.file_parser.headers[-1]
        expected_value = row[-1]
        self.assertEqual(self.file_parser.get_row_value(row, column_name), expected_value)

        # Test getting a value from a middle row
        row = self.file_parser.rows[len(self.file_parser.rows) // 2]
        column_name = self.file_parser.headers[len(self.file_parser.headers) // 2]
        expected_value = row[len(row) // 2]
        self.assertEqual(self.file_parser.get_row_value(row, column_name), expected_value)

    def tearDown(self):
        # Clean up any resources used by the tests
        pass

if __name__ == '__main__':
    unittest.main()
