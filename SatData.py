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
        headers = ["DBN", "School_Name", "Number_of_Test_Takers",
                   "Critical_Reading_Mean", "Mathematics_Mean", "Writing_Mean"]
        dbns.sort()
        csv_data = ",".join(headers) + "\n"
        for row in self._data:
            dbn = row[2]
            if dbn in dbns:
                school_name = f'"{row[3]}"' if "," in row[3] else row[3]
                row_data = [dbn, school_name, str(row[4]), str(row[5]), str(row[6]), str(row[7])]
                csv_data += ",".join(row_data) + "\n"

        with open("output.csv", "w") as file:
            file.write(csv_data)
