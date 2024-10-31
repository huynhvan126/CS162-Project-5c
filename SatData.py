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
        with open("sat.json", "r") as file:
            try:
                self._data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON file: {e}")
                exit(1)

    def save_as_csv(self, dbns):
        """
        Save SAT data to CSV file named 'output.csv'.
        """
        headers = ["DBN", "School Name", "Number of Test Takers",
                   "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]
        dbns.sort()
        csv_data = ",".join(headers) + "\n"
        for school in self._data:
            if school["DBN"] in dbns:
                school_name = f'"{school["School Name"]}"' if "," in school["School Name"] else school["School Name"]
                row_data = [school["DBN"],
                            school_name,
                            str(school["Number of Test Takers"]),
                            str(school["Critical Reading Mean"]),
                            str(school["Mathematics Mean"]),]
                csv_data += ",".join(row_data) + "\n"

        with open("output.csv", "w") as file:
            file.write(csv_data)
