
import csv

# Read the budget data from the CSV file
filename = "Resources/budget_data.csv"

with open(filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    data = list(reader)

# Initialize variables
total_months = len(data)
net_total = 0
changes = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Calculate the net total amount and find the greatest increase and decrease
for i in range(total_months):
    date = data[i][0]
    profit_loss = int(data[i][1])
    net_total += profit_loss

    if i > 0:
        change = profit_loss - int(data[i - 1][1])
        changes.append(change)

        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = date

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = date

# Calculate the average change
average_change = sum(changes) / len(changes)

# Printing the financial analysis summary
output = f"Financial Analysis\n"
output += f"-----------------------------\n"
output += f"Total Months: {total_months}\n"
output += f"Total: ${net_total}\n"
output += f"Average Change: ${average_change:.2f}\n"
output += f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
output += f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"

print(output)

# Export the results to a text file
output_filename = "analysis/financial_analysis.txt"
with open(output_filename, 'w') as output_file:
    output_file.write(output)

# Printing the file export message
print(f"Financial Analysis data exported to folder {output_filename} file.")


