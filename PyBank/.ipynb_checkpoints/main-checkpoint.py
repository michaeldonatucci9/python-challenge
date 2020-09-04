# import library
import os
import csv

# creating path
OUT_PATH = "budget_data.csv"

# index to rows
DATE_IDX = 1
PROFIT_LOSSES_IDX = 2

OUT_HEADER = [
    "Total Months",
    "Net Profit/Losses",
    "Average Change",
    "Greatest increase in Profit",
    "Greatest Decrease in Profit"
]
# joining path
path = os.path.join("Resources", "budget_data.csv")

# count
total_months = []
net_profit_losses = []
average_change = []
revenue_change = []
greatest_increase_in_profit = []
greatest_decrease_in_profit = []

# open path
with open(path, "r") as file:
    csv_reader = csv.reader(file)
    # skip header
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        

# The total number of months included in the dataset
        total_months.append(row[0])

# The net total amount of "Profit/Losses" over the entire period
        net_profit_losses.append(int(row[1]))

# The average of the changes in "Profit/Losses" over the entire period
# calculate average revenue change
for i in range(len(net_profit_losses)-1):
    average_change.append(int(net_profit_losses[i+1])-int(net_profit_losses[i]))
    revenue_change = sum(average_change) / len(average_change)
    
# find the greatest increase and decrease $
    greatest_increase_in_profit = max(average_change)
    greatest_decrease_in_profit = min(average_change)
    
# print the Results
print("Profit Loss Margin Analysis")
print("---------------------------------")      
print(f"Total Months:" + str(len(total_months)))
print(f"Total:"  + "$" + str(sum(net_profit_losses)))
print(f"Average Change:" + "$" + str(round(revenue_change, 2))) 
print(f"Greatest Increase in Profits:" + str(total_months[average_change.index(max(average_change))+1]) + " $ " + str(greatest_increase_in_profit))
print(f"Greatest Decrease in Profits:" + str(total_months[average_change.index(min(average_change))+1]) + " $ " + str(greatest_decrease_in_profit))

#output to text file
with open(OUT_PATH, "w+") as file:
    file.write("Profit Loss Margin Analysis\n")
    file.write("---------------------------------\n") 
    file.write(f"Total Months:" + str(len(total_months)) + "\n")
    file.write(f"Total:"  + "$" + str(sum(net_profit_losses)) + "\n")
    file.write(f"Average Change:" + "$" + str(round(revenue_change, 2)) + "\n") 
    file.write(f"Greatest Increase in Profits:" + str(total_months[average_change.index(max(average_change))+1]) + " $ " + str(greatest_increase_in_profit) + "\n")
    file.write(f"Greatest Decrease in Profits:" + str(total_months[average_change.index(min(average_change))+1]) + " $ " + str(greatest_decrease_in_profit) + "\n")
file.close