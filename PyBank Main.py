import csv
row_count=0
total_sum=0
total_change=0
largest_increase=[' ',0]
largest_decrease=[' ',0]
with open('Resources/budget_data.csv', 'r') as my_data: #only works when saving the budget_data file as csv; cannot push changes into github
    csv_reader=csv.reader(my_data)

# 1. finding the total number of months
    row_count=0
    for row_count in csv_reader:
        row_count=row_count + 1
        print (row_count) #do i need to print this?

# 2. finding the net total amount of "Profit/Losses" over the entire period
    header=next(csv_reader)
    first_row=next(csv_reader) #dealing with first row at first to be able to calculate the changes in "Profit/Losses" correctly
    last_month_value=first_row[1] #to start first row without getting an error since the first row's value doesn't exist
    row_count+=1 #i dont know why this has to be here when it's already at the bottom
    total_sum+=int(first_row[1])

#Not sure where it is that #3 was solved "Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes"

    # 4. The greatest increase in profits (date and amount) over the entire period
    for row in csv_reader:
        monthly_change=int(row[1])-last_month_value
        total_change+=monthly_change
        if monthly_change > largest_increase:
            largest_increase[1]=monthly_change
            largest_increase[0]=row[0]
        row_count+=1
        total_sum+=int(row[1])
        last_month_value=int(row[1])

    # 5. The greatest decrease in losses (date and amount) over the entire period
        for row in csv_reader:
            monthly_change=int(row[1])-last_month_value
            total_change+=monthly_change
            if monthly_change < largest_decrease:
                largest_decrease[1]=monthly_change
                largest_decrease[0]=row[0]
            row_count+=1
            total_sum+=int(row[1])
            last_month_value=int(row[1])