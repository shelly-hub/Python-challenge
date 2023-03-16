import os
import csv

#Create path for in-file and out-file
csvpath = os.path.join('Resources','budget_data.csv')
outpath = os.path.join('Analysis','budget_report.txt')

# Create list to store the variables
date = []
profit_loss = []
change_profit = []

#Open the file to read
with open(csvpath,'r') as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=",")

    csvheader = next(csvreader) 
    #print(f"Headers: {csvheader}")
    
    #Iterate the CSV values into the lists   
    for row in csvreader:

        date.append(row[0])
        profit_loss.append(int(row[1]))

    
#Calculate differences in Profit/Losses
#Need to substract last row since no values for monthly change
    for j in range(len(profit_loss) - 1):
        monthly_change = float(profit_loss[j+1])-float(profit_loss[j])
        change_profit.append(monthly_change)


#Calculate total number of Months
total_months = len(date)
#print(total_months)

#Calculate net profit/loss
net_total = sum(profit_loss)
#print(net_total)

#Calculate average monthly changes
average_changes = round(sum(change_profit)/len(change_profit),2)
#print(average_changes)

#Find Greatest Increase in Profits
max_profits = max(change_profit)

#Find Greatest Decrease in Profits
min_profits = min(change_profit)

#Find corresponding months location with Greatest Increase in Profits
#Need to add 1 to the month index value since it is counted from zero

max_month = change_profit.index(max_profits) + 1
min_month = change_profit.index(min_profits) + 1

#Print Values

# print(f"Total months: {total_months}")
# print(f"Net total: ${net_total}")
# print(f"Average Change : ${average_changes}")
# print(f"Greatest Increase in Profits: {date[max_month]} (${(str(max_profits))}) ")
# print(f"Greatest Decrease in Profits: {date[min_month]} (${(str(min_profits))}) ")

output = (
    f"Financial Analysis\n"

    f"------------------------------\n"

    f"Total months: {total_months}\n"

    f"Net total: ${net_total}\n"

    f"Average Change : ${average_changes}\n" 

    f"Greatest Increase in Profits: {date[max_month]} (${(str(max_profits))})\n"  
    
    f"Greatest Decrease in Profits: {date[min_month]} (${(str(min_profits))})\n"   )

# print(output)
   
#Export to output file
with open(outpath, 'w') as textfile:
    textfile.write(output)