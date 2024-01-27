import unittest
from unittest.mock import patch, mock_open
from invoice_gen.pull_csv_data import CSVData


class TestCSVData(unittest.TestCase):
    def setUp(self):
        self.test_file = "tests/data/test.csv"

    def test_init_sets_input_file(self):
        csv_data = CSVData(self.test_file)
        self.assertEqual(csv_data.input_file, self.test_file)

    @patch("pandas.read_csv")
    def test_read_csv_reads_data(self, mock_read_csv):
        with patch("pandas.read_csv", return_value=mock_read_csv):
            mock_read_csv.to_dict.return_value = [{"a": 1, "b": 2}]
            csv_data = CSVData(self.test_file)
            csv_data.read_csv()
            self.assertEqual(csv_data.data, [{"a": 1, "b": 2}])

    def test_iter_returns_data_iterator(self):
        csv_data = CSVData(self.test_file)
        csv_data.data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
        self.assertEqual(list(iter(csv_data)), [{"a": 1, "b": 2}, {"a": 3, "b": 4}])


if __name__ == "__main__":
    unittest.main()
