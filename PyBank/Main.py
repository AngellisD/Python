
import os
import csv
"----------------------------------------------------"
# Set List To Store Data
months=0
total_months=[] 
net_profit_losses=0
total_net_profit_losses=[]
prof_loss_average=[]
total_prof_loss_averages=[]
average=0
total_average=[]
monthly_change=[]
# Look up the path route
file_dir=os.path.join('budget_data.csv')
with open(file_dir, newline='') as newfile:
    budget_data_reader=csv.reader(newfile,delimiter=',')
# Skip the header - bring only values
    next(budget_data_reader)

# Looking for total months and total net profit and losses
    for x in budget_data_reader:
        months=months+1
        total_months.append(x[0])
        net_profit_losses=net_profit_losses+int(x[1])
        total_net_profit_losses.append(int(x[1]))
        average=round(net_profit_losses / int(x[1]), 2)
        total_average.append(average)



print("Financial Analysis")
print("------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_profit_losses}")
print(f"Average Change: ${average}")


