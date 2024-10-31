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

    def save_as_csv(self, dbns):
        """
        Save SAT data to CSV file.
        """
        dbns = sorted(dbns)

        headers = ["DBN", "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean",
                   "Writing Mean"]

        with open('output.csv', 'w') as file:
            file.write(",".join(headers) + "\n")
            for dbn in dbns:
                school_data = next((school for school in self._data if school["DBN"] == dbn), None)
                if school_data:
                    row = [
                        school_data.get["DBN", ""],
                        f'"{school_data.get("School Name", "")}"' if "," in school_data.get("School Name", "") else school_data.get("School Name", ""),
                        school_data.get("Number of Test Takers", ""),
                        school_data.get("Critical Reading Mean", ""),
                        school_data.get("Mathematics Mean", "")
                    ]
                    file.write(','.join(str(value) if value != "" else "" for value in row) + '\n')
