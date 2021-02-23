import csv
import os
output=os.path.join("Analysis", "PyBank_results.txt")
reader=0
header=0
first_row=0
row_count=0
total_sum=0
row=0
last_month_value=0
total_change=0
largest_increase=[' ',0] #[date,monthly_change] <-- positions of date and profit loss
largest_decrease=[' ',0]

with open('Resources/budget_data.csv', 'r') as my_data:
    reader=csv.reader(my_data)
    header=next(reader) #skipping column headers
    first_row=next(reader)
    last_month_value=int(first_row[1])
    row_count+=1
    total_sum+=int(first_row[1])

    for row in reader:
        monthly_change=int(row[1])-last_month_value # 3a. Calculate the changes in "Profit/Losses" over the entire period
        total_change+=monthly_change
        if monthly_change > largest_increase[1]:
            largest_increase[1]=monthly_change # 4b. The greatest increase in profits amount over the entire period
            largest_increase[0]=row[0]# 4a. The greatest increase in profits date over the entire period
        
        if monthly_change < largest_decrease[1]:
            largest_decrease[1]=monthly_change # 5b. The greatest decrease in profits amount over the entire period
            largest_decrease[0]=row[0]# 5a. The greatest decrease in profits date over the entire period

        row_count+=1 # 1. Find the total number of months
        total_sum+=int(row[1]) #2. Find the net total amount of "Profit/Losses" over the entire period
        last_month_value=int(row[1])

average_of_change=total_change/(row_count-1) # 3b. Find the average of those changes

# 6a. Print the analysis to the terminal
print("Financial Analysis")
print("------------------")
print(f"Total months: "+str(row_count))
print("Total: $"+str(total_sum))
print("Average Change: $"+str(round(average_of_change,2)))
print("Greatest Increase in Profits: "+str(largest_increase[0])+" $("+str(largest_increase[1])+")")
print("Greatest Decrease in Profits: "+str(largest_decrease[0])+" $("+str(largest_decrease[1])+")")

# 6b. Export a text file with the results
with open(output, 'w', newline='') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"------------------\n")
    txtfile.write(f"Total months: {row_count}\n")
    txtfile.write(f"Total: ${total_sum}\n")
    txtfile.write(f"Average Change: $ {round(average_of_change,2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {largest_increase[0]} $({largest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {largest_decrease[0]} $({largest_decrease[1]})\n")