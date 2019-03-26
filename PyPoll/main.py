import os
import csv

PollCSV = os.path.join("election_data2.csv")

with open(PollCSV, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
