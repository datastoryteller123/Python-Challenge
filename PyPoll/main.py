# Python Challenge

# Import module that will enable file paths across the operating systems
import os

#Import module for reading csv file
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # CSV Header
    csv_header = next(csvreader)
        
    political_candidate = []
    total_votes = 0
    votes_count = []
    csv_reader = ['1', '2']

    
    for row in csvreader:
        #print(row)

        # A complete list of candidates who received votes
        total_votes += 1

        candidate = row[2]

        if candidate in political_candidate:
            candidate_index = political_candidate.index(candidate)
            votes_count[candidate_index] += 1
        else:
            political_candidate.append(candidate)
            votes_count.append(1)

# The percentages
percentages = []
greatest_votes = votes_count[0]
greatest_votes_index = 0
for count in range(len(political_candidate)):
    percentage_vote = votes_count[count] / total_votes * 100
    percentages.append(percentage_vote)

    if votes_count[count] > greatest_votes:
        print(greatest_votes)
        greatest_votes_index = count

# The winner of the election based on popular vote.
winner = political_candidate[greatest_votes_index]
percentages = [round (a,2) for a in percentages]

# Print election results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for count in range(len(political_candidate)):
    print(f"{political_candidate[count]}: {percentages[count]}% ({votes_count[count]})")
print("--------------------------")
print(f"Winner:  {winner}")
print("--------------------------")

pathout = os.path.join("Analysis", "election_analysis.txt")


