import os

import csv
total_net = 0
total_months = 0
previous_change = 1088993
net_change = []
greatest_increase_month = ''
greatest_increase_amount = 0
greatest_decrease_month = ''
greatest_decrease_amount = 0
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    data = csv.reader(csvfile)
    header = next(data)
    for row in data:
        total_net = total_net + int(row[1])  
        total_months = total_months + 1
        current_change = int(row[1]) - previous_change
        previous_change = int(row[1])
        net_change.append(current_change)
        if greatest_increase_amount < int(row[1]) :
            greatest_increase_amount = int(row[1])
            greatest_increase_month = row[0]
        if greatest_decrease_amount > int(row[1]) :
            greatest_decrease_amount = int(row[1])
            greatest_decrease_month = row[0]
print(total_net) 
print(total_months) 
print(net_change)

monthly_average = sum(net_change) / total_months

print(monthly_average)
print(greatest_increase_month)
print(greatest_increase_amount)
print(greatest_decrease_month)
print(greatest_decrease_amount)

print("Hello World")

# Get first Month+year  data[1]
# Get last Month+year  data[-1]
# Convert to months

print("Financial Analysis")

print("-------------------------")





