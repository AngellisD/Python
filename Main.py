#importing data
import os
import csv

# Opening  CSV file
csvpath = os.path.join("budget_data.csv")

# Set variables
months = 0
net_profit_losses = 0
value = 0
move = 0
total_months = []
profits_losses = []


# Reading and delimiting the CSV file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Skip header
    header = next(csvreader)

 # Set total months and total net profit and lossses
    first_row = next(csvreader)
    months += 1
    net_profit_losses += int(first_row[1])
    value = int(first_row[1])
    
 #  Read each row of data after the header 
    for row in csvreader:
        total_months.append(row[0])
        
# Calculate the changes, total months and profit and losses 
        move = int(row[1])-value
        profits_losses.append(move)
        value = int(row[1])
        months +=1
        net_profit_losses = net_profit_losses + int(row[1])
        
# Greatest increase in profits
    greatest_increase = max(profits_losses)
    greatest_index = profits_losses.index(greatest_increase)
    greatest_month = total_months[greatest_index]

# Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits_losses)
    worst_index = profits_losses.index(greatest_decrease)
    worst_month = total_months[worst_index]

# Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits_losses)/len(profits_losses)
    

#Display information

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(months)}")
print(f"Total: ${str(net_profit_losses)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_month} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_month} (${str(greatest_decrease)})")

#Exporing to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(months)}")
line4 = str(f"Total: ${str(net_profit_losses)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_month} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_month} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))