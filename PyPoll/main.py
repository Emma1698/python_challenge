# Creating the file/cvs file
import os
import csv

# Creating path for file
csvpath= os.path.join('Resources','election_data.csv')

# Opening the csv file
with open(csvpath)as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',') 
    csv_header= next(csvreader)

# Listing variables
candidates= []
number_votes= []
votes_receive= []
total = 0
Raymond= 0
Charles=0
Diana=0

# Counting the total number of votes
for row in csvreader:
    total += 1
    
    

    
  