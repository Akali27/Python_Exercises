import os 
import csv 

budgetCSV = ("C:/Users/RogStrix/Downloads/03-Python/Instructions/PyBank/raw_data")


with open(budgetCSV, 'r') as csvfile: 
  
        csvreader = csv.reader(csvfile, delimiter=",")
  
        month = 0
        total_revenue = 0
        increased_value = ["", 0]
        decreased_value = ["", 0]
   
        for row in csvreader:
        #print(row[1])
         month += 1
         if month != 1:
             total_revenue = total_revenue + int(row[1])
         if lastmonth_value != 0 and (increased_value[1] < int(row[1]) - lastmonth_value[1]):
             increased_value[0] = row[0]
             increased_value[1] = int(row[1]) - lastmonth_value[1]
               
           
         # print(row[0])
        if lastmonth_value != 0 and (decreased_value[1] > int(row[1]) - lastmonth_value[1]):
            decreased_value[0] = row[0]
            decreased_value[1] = int(row[1]) - lastmonth_value[1]
               
        lastmonth_value[1] = int(row[1])
        lastmonth_value[0] = row[0]

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month - 1))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(round(total_revenue / (month -1),2)))
print("Greatest Increase in Revenue: " + str(increased_value[0]) + " " +
                                         ("($" + (str(increased_value[1]) + ")")))
print("Greatest Decrease in revenue: " + str(decreased_value[0]) + " " +
                                         ("($" + (str(decreased_value[1]) + ")")))