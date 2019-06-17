#Import Modules

import os
import csv

#Set variables

months = []
revenue = []
revenue_change = []

# Set path for file

file_path = os.path.join("budget_data.csv")

with open(file_path,'r') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

# Read the header row first
    
    next(csv_reader, None)

# Read each row of data after the header
    
    for row in csv_reader:

        months.append(row[0])
        revenue.append(int(row[1]))

    unique_months = set(months)    
    total_revenue = sum(revenue)
    
# Calculate Change in Revenue 
    
    for i in range(0,len(revenue) -1): 

        revenue_change.append(int(revenue[i+1]) - int(revenue[i]))
        avg_rev_change = sum(revenue_change)/len(revenue_change)

# find maximum and minimum revenue
    
    max_revenue = max(revenue)
    min_revenue = min(revenue)

# find the associated date of maximum and minimm revenue
    
    max_revenue_date = months[revenue.index(max_revenue)]
    min_revenue_date = months[revenue.index(min_revenue)]
 
# Per instructions, print analysis to terminal  

print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(len(unique_months)))
print("Total Revenue: $" + str(total_revenue)) 
print("Average Revenue Change: $" + str(avg_rev_change))
print("Greatest Increase in Revenue: " + max_revenue_date + " ($" + str(max_revenue)+ ")")
print("Greatest Decrease in Revenue: " + min_revenue_date + " ($" + str(min_revenue)+ ")")

# Export to text file
#'.2f' formats decimals to 2 places

f = open("budget_data_results.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(unique_months) + "\n")
f.write("Total: $" + str(total_revenue) + "\n")
f.write("Average Change: $" + str(format(avg_rev_change, '.2f')) + "\n")
f.write("Greatest Increase in Profits: " + max_revenue_date + " ($" + str(max_revenue) + ")\n")
f.write("Greatest Decrease in Profits: " + min_revenue_date + " ($" + str(min_revenue) + ")\n")
f.close()




