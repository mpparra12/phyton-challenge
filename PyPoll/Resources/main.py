import csv

# Path to the election_data.csv file
file_path = "C:\\Users\\chris\\RICE DATA\\Module 3 - Python\\phyton-challenge\\PyPoll\\Resources\\election_data.csv"

# Initialize variables
total_votes = 0
candidates_votes = {}

# Open and read the CSV file
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip header row
    next(csv_reader)

    # Loop through each row in the dataset
    for row in csv_reader:
        candidate = row[2]

        # Increment the total votes
        total_votes += 1

        # If the candidate is not in the dictionary, add them with a vote, else increment their vote count
        if candidate not in candidates_votes:
            candidates_votes[candidate] = 1
        else:
            candidates_votes[candidate] += 1

# Calculate the results
winner = max(candidates_votes, key=candidates_votes.get)

# Display the results
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-------------------")

for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------")
print(f"Winner: {winner}")
print("-------------------")