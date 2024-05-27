import pandas as pd
import pytest
from src.read_data import read_csv

def test_read_csv(tmp_path):
    # Create a sample pipe-separated CSV file
    data = """Deep|Mehta|Company Inc.|1980-01-01|75000|123 Main St|Pymble|NSW|12345|1234567890|9876543210|deep.mehta@example.com"""
    
    # Write the sample data to a temporary file
    file_path = tmp_path / "test_data.csv"
    file_path.write_text(data)
    
    # Read the data using the read_data function
    df = read_csv(file_path)

    # Define the expected DataFrame
    expected_data = {
        'FirstName': ['Deep'],
        'LastName': ['Mehta'],
        'Company': ['Company Inc.'],
        'BirthDate': ['1980-01-01'],
        'Salary': [75000.0],
        'Address': ['123 Main St'],
        'Suburb': ['Pymble'],
        'State': ['NSW'],
        'Post': [12345],
        'Phone': [1234567890],
        'Mobile': [9876543210],
        'Email': ['deep.mehta@example.com']
    }
    expected_df = pd.DataFrame(expected_data)
    
    # Compare the resulting DataFrame with the expected DataFrame
    pd.testing.assert_frame_equal(df, expected_df)

if __name__ == "__main__":
    pytest.main()
