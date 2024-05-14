import csv

csv_path= "Resources\election_data.csv"

with open(csv_path, mode="r")as csv_file:
    reader = csv.reader(csv_file)
    header=next(reader)
    for low in reader:
        print(low)
        
    