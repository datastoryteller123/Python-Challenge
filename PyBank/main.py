# Python Challenge

# Import module that will enable file paths across the operating systems
import os

#Import module for reading csv file
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# CSV Module - Reading
with open(csvpath) as csvfile:

    # CSV delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # CSV Header
    csv_header = next(csvreader)

   
    total_month = 0
    total_pandl = 0
    num = 0
    change = 0
    date = []
    profit = []
    
    header = next(csvreader)
    total_month += 1
    total_pandl = total_pandl + int(header[1])
    value = int(header[1])
     
    for row in csvreader:
        
        date.append(row[0])
        
        change = int(row[1])-value
        profit.append(change)
        value = int(row[1])
        
        #Total number of months/Total P&L Change
        total_month += 1
        total_pandl = total_pandl + int(row[1])

    # The greatest increase in profits
    greatest_increase = max(profit)
    greatest_index = profit.index(greatest_increase)
    greatest_date = date[greatest_index]

    # The greatest decrease in losses
    greatest_decrease = min(profit)
    worst_index = profit.index(greatest_decrease)
    worst_date = date[worst_index]

    # The average of the changes in "Profit/Losses"
    Average_Change = sum(profit)/len(profit)
    

# Print Output

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_month)}")
print(f"Total: ${str(total_pandl)}")
print(f"Average Change: ${str(round(Average_Change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

pathout = os.path.join("Analysis", "budget_analysis.txt")

with open(pathout, "w") as txt_file:
    txt_file.write(
        "Financial Analysis"
        "---------------------"
        f"Total Months: {str(total_month)}"
        f"Total: ${str(total_pandl)}"
        f"Average Change: ${str(round(Average_Change,2))}"  
        f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})"
        f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})"
    )
