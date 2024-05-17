# Creating the file/cvs file
import os
import csv

# All Variable

total_months = 0
total_profit_losses = 0
changes_profit_losses = []
profit_losses= []
months=[]

# Setting a path for file
csv_path =os.path.join("Resources" , "budget_data.csv")

# Opening cvs file
with open(csv_path)as csv_file:
    csvreader= csv.reader (csv_file, delimiter= ',')
    csvheader=next(csvreader)
    
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

    increase_profit = max(changes_profit_losses)
    greatest_increase_profit = changes_profit_losses.index(increase_profit)

    decreased_profit = min(changes_profit_losses)
    greatest_decreased_profit = changes_profit_losses.index(decreased_profit)

# Printing the Final analysis
    print('Financial Analysis')
    print("----------------------------------")
    print(f'Total Months:{total_months}')
    print(f'Total: ${total_profit_losses}')
    print(f'Average Change: ${average_changes}')
    print(f'Greatest Increase in Profit: {months[greatest_increase_profit]} (${increase_profit})')
    print(f'Greatest Decrease in Profits: {months[greatest_decreased_profit]} (${decreased_profit})')

# Setting a path for file to print Final Analysis and export to a text file
dpath = "PyBank/Analysis"
os.makedirs(dpath, exist_ok=True)
with open("Analysis/budget_analysis.txt", "w")as file:

    file.write('Financial Analysis\n')
    file.write("----------------------------------\n")
    file.write(f'Total Months:{total_months}\n')
    file.write(f'Total: ${total_profit_losses}\n')
    file.write(f'Average Change: ${average_changes}\n')
    file.write(f'Greatest Increase in Profit: {months[greatest_increase_profit]} (${increase_profit})\n')
    file.write(f'Greatest Decrease in Profits: {months[greatest_decreased_profit]} (${decreased_profit})')








    
    
    