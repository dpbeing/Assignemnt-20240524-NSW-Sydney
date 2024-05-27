import pytest
import pandas as pd
from src.transform_data import transform_data

def test_transform_data():
    data = pd.DataFrame([{
        'FirstName': ' Deep ',
        'LastName': ' Mehta ',
        'Company': 'ABC Corp',
        'BirthDate': '1980-05-15',
        'Salary': 60000,
        'Address': '123 Main St',
        'Suburb': 'Pymble',
        'State': 'NSW',
        'Post': 2010,
        'Phone': 1234567890,
        'Mobile': 2345678901,
        'Email': 'deep.mehta@example.com'
    }])
    transformed_data = transform_data(data)
    assert transformed_data['FullName'][0] == 'Deep Mehta'
    assert transformed_data['BirthDate'][0] == '15/05/1980'
    assert transformed_data['Salary'][0] == '$60,000.00'
    assert transformed_data['Age'][0] == 43
    assert transformed_data['SalaryBucket'][0] == 'B'
    assert 'FirstName' not in transformed_data.columns
    assert 'LastName' not in transformed_data.columns
    assert 'Address' in transformed_data.columns
    assert isinstance(transformed_data['Address'][0], dict)
    assert transformed_data['Address'][0] == {
        'Street': '123 Main St',
        'Suburb': 'Pymble',
        'State': 'NSW',
        'Post': 2010
    }