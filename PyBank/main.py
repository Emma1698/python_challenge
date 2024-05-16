import os
import csv

csv_path =os.path.join("Resources" , "budget_data.csv")

with open(csv_path)as csv_file:
    csvreader= csv.reader (csv_file, delimiter= ',')
    csvheader=next(csvreader)
    print('Financial Analysis')
    print("__________________")
    

# The total number of months included in the dataset
    total_months = []
# The net total amount of "Profit/Losses" over the entire period
    total_profit_losses = []
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    changes_profit_losses = []
 # The greatest increase in profits (date and amount) over the entire period
    greatest_increase_profit= 0
# The greatest decrease in profits (date and amount) over the entire period   
    greatest_decrease_profit= 0

    for row in csvreader:
        total_months += 1
        total_profit_losses += int(row[1])
        total_months.append(row[0])
        total_profit_losses.append
        changes_profit_losses.append



    # print(current_profit)
    print(total_months)
    print(total_profit_losses)
    
    