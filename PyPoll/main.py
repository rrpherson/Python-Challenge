import os
import csv

PollCSV = os.path.join("PyPoll" , "election_data.csv")


total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""

with open(PollCSV, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")