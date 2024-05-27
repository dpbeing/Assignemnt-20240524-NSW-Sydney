import pytest
import pandas as pd
from src.transform_data import transform_data
from src.entity import Employee, Address

def test_transform_data():
    # Define a sample DataFrame
    data = {
        'FirstName': ['Deep' ,'Dan'],
        'LastName': ['Mehta', 'Smith'],
        'Company': ['Company Inc.', 'Another Co.'],
        'BirthDate': ['1980-01-01', '1990-02-02'],
        'Salary': [75000, 85000],
        'Address': ['123 Main St', '456 Another Rd'],
        'Suburb': ['Pymble', 'Other Suburb'],
        'State': ['NSW', 'VIC'],
        'Post': [12345, 67890],
        'Phone': [1234567890, 2345678901],
        'Mobile': [9876543210, 1987654320],
        'Email': ['deep_mehta@example.com', 'dan.smith@example.com']
    }
    
    df = pd.DataFrame(data)

    # Transform the data
    employees = transform_data(df)
    
    # Verify the data structure and content
    assert isinstance(employees, list)
    assert len(employees) == 2
    assert isinstance(employees[0], Employee)
    assert employees[0].full_name == 'Deep Mehta'
    assert employees[1].full_name == 'Dan Smith'
    assert employees[0].age == 44  # Assuming test is run in 2024
    assert employees[1].age == 34
    assert employees[0].salary == '$75,000.00'
    assert employees[1].salary == '$85,000.00'
    assert employees[0].salary_bucket == 'B'
    assert employees[1].salary_bucket == 'B'
    assert isinstance(employees[0].address, Address)
    assert employees[0].address.street == '123 Main St'
    assert employees[1].address.post_code == 67890

if __name__ == '__main__':
    pytest.main()
