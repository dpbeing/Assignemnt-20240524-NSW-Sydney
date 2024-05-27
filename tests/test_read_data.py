import pytest
from src.read_data import read_csv

def test_read_data(self):
    data = read_csv('/Users/deep/Assignemnt-20240524-NSW-Sydney/data/data/members-data.csv')
    self.assertIsInstance(data, list)
    self.assertGreater(len(data), 0)
    self.assertIn('FirstName', data[0])
    self.assertIn('LastName', data[0])
