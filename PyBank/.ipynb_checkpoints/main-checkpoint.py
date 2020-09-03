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
greatest_increase_in_profit = []
greatest_decrease_in_profit = []

        
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
    average_change = sum(average_change) / len(average_change)
    
#find the greatest increase and decrease month/yr and $
greatest_increase_in_profit = max(average_change)
print(average_change)
i = average_change.index(greatest_increase)
month_increase = month[i +1]
    
greatest_decrease_in_profit = min(average_change)
print(average_change)
d = average_change.index(greatest_decrease)
month_decrease = month[d+1]

# print the Results
print("Profit Loss Margin Analysis")
print("---------------------------------------------------------------------------------------------------")                                   
print(len(total_months))
print(sum(net_profit_losses))
print(average_change)
print("f Greatest Increase in Profits: {month_increase} {greatest_increase}")
print("f Greatest Decrease in Profits: {month_decrease} {greatest_decrease}")