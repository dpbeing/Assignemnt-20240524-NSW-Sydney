import pytest
from src.read_data import read_csv

def test_read_data(self):
    data = read_csv('data/members-data.csv')
    self.assertIsInstance(data, list)
    self.assertGreater(len(data), 0)
    self.assertIn('FirstName', data[0])
    self.assertIn('LastName', data[0])
