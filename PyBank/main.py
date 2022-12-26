#import modules
import os
import csv

#set path for file
csvpath = os.path.join("C:\\Users\\cryst\\OneDrive\\Documents\\Bootcamp Class\\Week3 Python\\python-challenge\\PyBank\\Resources\\budget_data.csv")

#set the output of the text file
text_file = "output.txt"

#set variables
total_months = 0
net_total_profit = 0
change_months = 0
profit_change = 0
previous_profit = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
profit_change_list = []
profit_average = 0



#open the csv file using CSV module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# enter loop
    for row in csvreader:
#calculate total months and net total profit
        total_months += 1
        net_total_profit = net_total_profit + int(row[1])
 
 # calculate average change (can't get the correct answer)   
        profit_change_list.append(float(row[1]))
        if total_months >1:
                change_months +=1
                profit_change = profit_change + (profit_change_list[total_months-1]- profit_change_list[total_months -2])
    
                profit_average = profit_change / change_months  
# calculate greatest increse and decrese in profits
        profit_change = int(row[1])- previous_profit
        previous_profit = int(row[1])
        profit_change_list = profit_change_list + [profit_change]

        if profit_change > greatest_increase [1]:
                greatest_increase[1]= profit_change
                greatest_increase[0] = row [0]
        if profit_change < greatest_decrease[1]:
                greatest_decrease[1]= profit_change
                greatest_decrease[0] = row [0]


with open(text_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total: $%d\n" % net_total_profit)
    file.write("Average Change $%d\n" % profit_average)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
