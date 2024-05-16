import os
import csv

csv_path= "Resources\election_data.csv"

with open(csv_path)as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for line in csvreader:
        print(line)
        
