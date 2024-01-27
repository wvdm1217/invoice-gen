"""
Tests for pull_csv_data.py
"""

import unittest
from invoice_gen import pull_csv_data

class TestPullData(unittest.TestCase):
    def test_pull_data(self):
        """
        Tests that pull_data returns a list of dictionaries
        """
        self.assertIsInstance(pull_csv_data.pull_data(), list)
        self.assertIsInstance(pull_csv_data.pull_data()[0], dict)
        self.assertEqual(pull_csv_data.pull_data()[0], {'name': 'John Doe', 'address': '123 Main St', 'city': 'Anytown', 'state': 'FL', 'zip_code': '12345', 'phone': '555-555-5555', 'email': 'johndoe@email.com'})

if __name__ == '__main__':
    unittest.main()