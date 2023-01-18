import os

import csv

csvpath = os.path.join('PyBank','Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    data = list(csv.reader(csvfile))

print("Hello World")

# Get first Month+year  data[1]
# Get last Month+year  data[-1]
# Convert to months

print("Financial Analysis")

print("-------------------------")

print(f"Total Months: " + str(len(data)-1))

for row in range(2,len(data)):
    total += data [2]


