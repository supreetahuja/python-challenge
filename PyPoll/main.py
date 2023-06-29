
import csv

# Reading data from given csv file with path mentioned
edatafile = "Resources/election_data.csv"

with open(edatafile, 'r') as file:
    reader = csv.reader(file)
    header = next(reader) # Skip the header row
    data = list(reader)

# naming few variables which will be used further
total_votes = len(data)
candidates = {}
winner = ""
winner_votes = 0

# Counting of votes for all candidates
for row in data:
    candidate = row[2]

    if candidate in candidates:
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1

# Percentage of votes for all candidates
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Printing the final count!!!!!!!!!
output = f"Election Results\n"
output += f"-------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += f"-------------------------\n"
for candidate, percentage, votes in results:
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"
output += f"-------------------------\n"
output += f"Winner: {winner}\n"
output += f"-------------------------\n"

print(output)

# Export the results to a text file
export_file = "analysis/election_results.txt"
with open(export_file, 'w') as output_file:
    output_file.write(output)

# Printing the text file export message with folder name
print(f"Election Results data exported to folder {export_file} file.")
