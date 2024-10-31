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
                self._data = json.load(file)

    def save_as_csv(self, dbns, output_filename="output.csv"):
        """
        Save SAT data to CSV file named 'output.csv'.
        """
        dbns.sort()
        with open(output_filename, "w", newline='') as csv_file:
            csv_file.write("DBN, School Name, Number of Test Takers, Critical Reading Mean, Mathematics Mean, Writing Mean\n")
            for row in self._data['school_data']:
                if row['DBN'] in dbns:
                    school_name = row['school_name'].replace(",", r'\"')
                    csv_file.write(f"{row['DBN']}, {school_name}, {row['num_tested']}, {row['critical_reading_mean']}, {row['mathematics_mean']}, {row['writing_mean']}\n")
