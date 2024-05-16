import os
import csv

csv_path= "Resources/budget_data.csv"

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
