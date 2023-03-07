from file_parser import FileParser

# Test the FileParser class
def test_file_parser_init():
    file_parser = FileParser("test_file.xlsx")
    assert file_parser.file_path == "test_file.xlsx"
    assert file_parser.rows == []
    assert file_parser.headers == []