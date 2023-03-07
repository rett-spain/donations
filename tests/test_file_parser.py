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
