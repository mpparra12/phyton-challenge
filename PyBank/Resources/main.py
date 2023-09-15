import csv

# Path to the budget_data.csv file
file_path = r'C:\Users\chris\RICE DATA\Module 3 - Python\phyton-challenge\PyBank\Resources\budget_data.csv'

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_month_profit_losses = None
changes = []
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}

# Open and read the CSV file
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip header row
    next(csv_reader)

    # Loop through each row in the dataset
    for row in csv_reader:
        date = row[0]
        profit_losses = int(row[1])

        total_months += 1
        total_profit_losses += profit_losses

        # If there's a previous month's profit/losses, calculate the change
        if previous_month_profit_losses is not None:
            change = profit_losses - previous_month_profit_losses
            changes.append(change)

            # Check if the change is the greatest increase or decrease
            if change > greatest_increase['amount']:
                greatest_increase['date'] = date
                greatest_increase['amount'] = change
            
            if change < greatest_decrease['amount']:
                greatest_decrease['date'] = date
                greatest_decrease['amount'] = change
        
        previous_month_profit_losses = profit_losses

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Display the results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")