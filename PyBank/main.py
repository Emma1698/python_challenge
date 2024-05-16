# Creating the file/cvs file
import os
import csv

# All Variable

    total_months = 0
    total_profit_losses = 0
    changes_profit_losses = []
    profit_losses= []
    months=[]

# Set path for file
csv_path =os.path.join("Resources" , "budget_data.csv")

# Opening cvs file
with open(csv_path)as csv_file:
    csvreader= csv.reader (csv_file, delimiter= ',')
    csvheader=next(csvreader)
    print('Financial Analysis')
    print("__________________")

# Looping through the data store and calculating total amount
    for row in csvreader:
        total_months += 1
        total_profit_losses += int(row[1])
        months.append(row[0])
        profit_losses.append(int(row[1]))
        changes_profit_losses.append(profit_losses[total_months -1]-profit_losses[total_months -2])

 # Getting the greatest increase and greatest decreased from change
    total_changes =sum(changes_profit_losses)
    average_changes =round(total_changes/(len(changes_profit_losses) -1), 2)
    increase_profit = max()


    # print(current_profit)
    
    
    