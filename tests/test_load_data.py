import pytest
import os
import json
from src.load_data import load_data

def test_load_data(tmpdir):
    file_path = os.path.join(tmpdir, 'output.json')
    transformed_data = pd.DataFrame([{
        'FullName': 'Deep Mehta',
        'Company': 'ABC Corp',
        'BirthDate': '15/05/1980',
        'Salary': '$60,000.00',
        'Age': 43,
        'SalaryBucket': 'B',
        'Address': {
            'Street': '123 Main St',
            'Suburb': 'Pymble',
            'State': 'NSW',
            'Post': 2010
        },
        'Phone': 1234567890,
        'Mobile': 2345678901,
        'Email': 'deep.mehta@example.com'
    }])
    load_data(transformed_data, file_path)
    with open(file_path, 'r') as file:
        output = json.load(file)
    assert isinstance(output, list)
    assert isinstance(output[0], dict)
    assert output[0]['FullName'] == 'Deep Mehta'
