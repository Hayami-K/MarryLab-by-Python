import csv

class Reader:
    def __init__(self, path):
        self.path = path

    def csv_to_list(self):
        with open(self.path, "r") as f:
            reader = csv.reader(f)
            return list(reader)