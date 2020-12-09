import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)
max_increase_month = monthly_profit_change.index(
    max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(
    min(monthly_profit_change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

outfilename = "C:\\Users\\heung\\python-challenge\\PyBank\\analysis\\Financial_Analysis.txt"
outfile = open(outfilename, 'w')
outfile.write("Financial Analysis")
outfile.write("\n")
outfile.write("----------------------------")
outfile.write("\n")
outfile.write(f"Total Months: {len(total_months)}")
outfile.write("\n")
outfile.write(f"Total: ${sum(total_profit)}")
outfile.write("\n")
outfile.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
outfile.write("\n")
outfile.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
outfile.write("\n")
outfile.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
outfile.close()
