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
        try:
            with open('sat.json', 'r') as json_file:
                self._data = json.load(json_file)
            except FileNotFoundError:
                print('file not found')

    def save_as_csv(self, dbn_list):
        """
        Save SAT data to CSV file.
        """
        csv_list = []
        headers = ["DBN", "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean",
                   "Writing Mean"]
        for item in self._data['data']:
            if item[8] in dbn_list:
                csv_list.append(item[8:14])
        sorted(csv_list)
        with open('output.csv', 'w') as new_file:
            new_file.write(','.join(headers))
            new_file.write('\n')
            pos = 0
            while pos < len(csv_list):
                new_file.write(csv_list[pos])
                new_file.write('\n')
                pos += 1
            return csv_list
