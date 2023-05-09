# Import Dependencies 
import os
import csv

# Input file path
budgetCSV = ('budget_data.csv')

# Open the input csv file
with open(budgetCSV, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Initialize variables to store the analysis results
    month = 0
    total_revenue = 0
    increased_value = ["", 0]
    decreased_value = ["", 0]
    lastmonth_value = [0, 0]  
    
    # Loop through each row in file
    for row in csvreader:
        month += 1
        if month != 1:
            # add the profit/loss value to the total revenue
            total_revenue = total_revenue + int(row[1])
            
            # Check if the current month has the greatest increase or decrease in profit/loss value compared to the previous month
            if lastmonth_value != 0 and (increased_value[1] < int(row[1]) - lastmonth_value[1]):
                increased_value[0] = row[0]
                increased_value[1] = int(row[1]) - lastmonth_value[1]
            if lastmonth_value != 0 and (decreased_value[1] > int(row[1]) - lastmonth_value[1]):
                decreased_value[0] = row[0]
                decreased_value[1] = int(row[1]) - lastmonth_value[1]
                
        # Update the lastmonth_value to store the profit/loss value from the current row
        lastmonth_value[1] = int(row[1])
        lastmonth_value[0] = row[0]

# Write the results to a text file
with open("financial_analysis.txt", "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write("Total Months: " + str(month - 1) + "\n")
    textfile.write("Total Revenue: $" + str(total_revenue) + "\n")
    textfile.write("Average Revenue Change: $" + str(round(total_revenue / (month -1),2)) + "\n")
    textfile.write("Greatest Increase in Revenue: " + str(increased_value[0]) + " " + ("($" + (str(increased_value[1]) + ")")) + "\n")
    textfile.write("Greatest Decrease in revenue: " + str(decreased_value[0]) + " " + ("($" + (str(decreased_value[1]) + ")")) + "\n")

# Print the results to the console
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month - 1))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(round(total_revenue / (month -1),2)))
print("Greatest Increase in Revenue: " + str(increased_value[0]) + " " + ("($" + (str(increased_value[1]) + ")")))
print("Greatest Decrease in revenue: " + str(decreased_value[0]) + " " + ("($" + (str(decreased_value[1]) + ")")))
