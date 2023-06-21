import os
import csv

#set lists and variables
date = []
profit_losses = 0
revenue= 0
pl_change = []
month_of_change =[]
total_months=0


with open('budget_data.csv', encoding='utf-8') as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter= ',') 
    #read header row
    csv_header = next(csvreader)
    total_months +=1
    
    #move down a line
    first_row= next(csvreader) 
    value=int(first_row[1])
    profit_losses += value
    

    #read each row of data after first_row 
    for row in csvreader:

        #Total months
        total_months +=1

        #net profit_losses
        profit_losses = profit_losses + int(row[1])

        #Change in revenue: 
        change= int(row[1]) - value
        pl_change.append(change)
        value=int(row[1])

    #Average change
    mean = sum(pl_change) / len(pl_change) 
    rounded_number=round(mean, 2) 
   

    #Display results in terminal
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total months: " + (str(total_months))) 
    print("Total:" + " $" + str(profit_losses))
    print("Average Change: $" + str(rounded_number))
    print("Greatest Increase in Profits: " + "$" + str(max(pl_change)))
    print("Greatest Decrease in Profits: " + "$" + str(min(pl_change)))

#Export text file with results 
with open('analysis.txt', 'w') as outfile:

    outfile.write(
        "Financial Analysis\n"
        "---------------------\n"
        "Total Months: " + str(total_months) + "\n"
        "Total:" + "$" + str(profit_losses) + "\n"
        "Average Change: $" + str(rounded_number) + "\n"
        "Greatest Increase in Profits: " + "$" + str(max(pl_change)) + "\n"
        "Greatest Decrease in Profits: " + "$" + str(min(pl_change))
    )
