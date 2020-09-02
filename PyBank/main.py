import os
import csv

OUT_PATH = "budget_data.csv"

DATE_IDX = 1
PROFIT_LOSSES_IDX = 2

OUT_HEADER = [
    "Total Months",
    "Net Profit/Losses",
    "Average Change",
    "Greatest increase in Profit",
    "Greatest Decrease in Profit"
]

path = os.path.join("Resources", "budget_data.csv")

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

# The greatest increase in profits (date and amount) over the entire period
    greatest_increase_in_profit = (max(average_change)

# The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease_in_profit = (min(average_change)
                                   
# print the Results
print("Profit Loss Margin Analysis")
print("
      ")                                   
print(len(total_months))
print(sum(net_profit_losses))
print(average_change)
# show month/year and total
print("greatest_increase_in_profit:" str(total_months[average_change.index(max(average_change))+1]) + " " + "$" + str(greatest_increase_in_profit))
# show month/year and total
print("greatest_decrease_in_profit:" str(total_months[average_change.index(min(average_change))+1]) + " " + "$" + str(greatest_decrease_in_profit))     # output to a text file

    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("
               " + "\n")

    file.write("len(total_months)"+ "\n")

    file.write("sum(net_profit_losses)" + "\n")

    file.write("average_change": " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Profit Margin Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Profit Margin Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()

