import pandas as pd
from typing import List, Dict, Any, Iterator
import os


class CSVData:
    """
    Class to pull data from a csv file and returns a list of dictionaries
    """

    def __init__(self, input_file: str) -> None:
        """
        Initialize CSVData with the input file path.

        Args:
            input_file (str): Path to the input CSV file.
        """
        if not os.path.isfile(input_file):
            raise ValueError(f"{input_file} does not exist.")
        if not input_file.endswith(".csv"):
            raise ValueError(f"{input_file} is not a valid CSV file.")
        self.data: List[Dict[str, Any]] = []
        self.input_file = input_file
        self.read_csv()

    def read_csv(self) -> None:
        """
        Read the CSV data from the input file and store it in self.data.
        """
        try:
            self.data = pd.read_csv(self.input_file).to_dict("records")
        except:
            raise ValueError(f"{self.input_file} is not a valid CSV file.")

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        """
        Returns the iterator object (self.data list)

        Returns:
            Iterator[Dict[str, Any]]: An iterator over self.data
        """
        return iter(self.data)
