# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/30/2024
# Description: Write a class named Satdata that read JSON file and a data to a text file in CSv format.
import json

class SatData:
    """
    A class to handle SAT data, reading SAT data for NYC from JSON file and saving specific school data to a CSV file.
    """
    def __init__(self):
        """
        Initialize SATData class by loading SAT data from 'sat.json'.
        """
        with open('sat.json', 'r') as file:
            self._data = json.load(file)

    def save_as_csv(self, dbns: list):
        """
        Save SAT data to CSV file named 'output.csv'.
        """
        headers = ["DBN", "School Name", "Number of Test Takers",
                   "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]
        rows = []
        for entry in self._data:
            if entry['DBN'] in dbns:
                row = [entry['DBN'],
                       f'"{entry["School Name"]}"' if ',' in entry["School Name"] else entry["School Name"],
                       entry['Number of Test Takers'],
                       entry['Critical Reading Mean'],
                       entry['Mathematics Mean'],
                       entry['Writing Mean']]
                rows.append(row)

        rows.sort(key=lambda x: x[0])

        with open('output.csv', 'w') as file:
            file.write(','.join(headers) + '\n')
            for row in rows:
                file.write(','.join(row) + '\n')
