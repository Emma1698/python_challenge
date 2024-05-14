import csv

csv_path= "Resources/budget_data.csv"

with open(csv_path, mode="r")as csv_file:
    reader = csv.reader(csv_file)
    header=next(reader)
    for row in reader:
        print(row)
                