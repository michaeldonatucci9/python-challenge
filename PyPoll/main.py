# import
import os
import csv

OUT_PATH = "election_data.csv"
# join path
path = os.path.join("Resources", "election_data.csv")

# variables
votes = []
candidates = []
khan = []
correy = []
li = []
otooley = []
decrease_month = []
increase_month = []

# open reader
with open(path, "r") as file:
    csv_reader = csv.reader(file)
    #skip header
    csv_header= next(csv_reader)
    
    for row in csv_reader:
        votes.append(int(row[0]))
        candidates.append(row[2])
        total_votes = (len(votes))
        
# votes for candidates                     
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        elif candidate == "O'Tooley":
            otooley.append(candidates)
            otooley_votes = len(otooley)

# calculation of percentage votes
    total_votes = khan_votes + correy_votes + li_votes + otooley_votes
    khan_percent = (khan_votes / total_votes) * 100
    correy_percent = (correy_votes / total_votes) * 100
    li_percent = (li_votes / total_votes) * 100
    otooley_percent = (otooley_votes / total_votes) * 100

# if else to declare winner    
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"
    

print(f"Election Results")
print("----------------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------------")      
print(f"Khan: {khan_percent}  {khan_votes}")
print(f"Correy: {correy_percent}  {correy_votes}")
print(f"Li: {li_percent}  {li_votes}")
print(f"OTooley: {otooley_percent}  {otooley_votes}")
print("----------------------------------------------")
print(f"Winner: {winner}")

with open(OUT_PATH, "w+") as file:
    file.write(f"Election Results \n")
    file.write("----------------------------------------------\n")
    file.write(f"Total Votes: {total_votes}" + "\n")
    file.write("----------------------------------------------\n")      
    file.write(f"Khan: {khan_percent}  {khan_votes}" + "\n")
    file.write(f"Correy: {correy_percent}  {correy_votes}" + "\n")
    file.write(f"Li: {li_percent}  {li_votes}" + "\n")
    file.write(f"OTooley: {otooley_percent}  {otooley_votes}" + "\n")
    file.write("----------------------------------------------\n")
    file.write(f"Winner: {winner}" + "\n")
    file.write("----------------------------------------------\n")
file.close