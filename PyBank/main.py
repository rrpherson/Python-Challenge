import os
import csv

TotalMonths = 0
NetTotal = 0
Value = 0
Change = 0
Dates = []
Profits = []

BudgetCSV = os.path.join("PyBank", "budget_data.csv")
Results_File = os.path.join("PyBank", "Results.txt")

with open(BudgetCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    FirstRow = next(csvreader) 
    NetTotal += int(FirstRow[1])
    Value = int(FirstRow[1])
    TotalMonths = 1

    for row in csvreader:
        TotalMonths = TotalMonths + 1
        Dates.append(row[0])

        Change = int(row[1])-Value
        Profits.append(Change)
        Value = int(row[1])

        NetTotal = NetTotal + int(row[1])

        GreatestIncrease = max(Profits)
        IncreaseIndex = Profits.index(GreatestIncrease)
        IncreaseDates = Dates[IncreaseIndex]
 
    GreatestDecrease = min(Profits)
    DecreaseIndex = Profits.index(GreatestDecrease)
    DecreaseDates = Dates[DecreaseIndex]

    ChangeAve = sum(Profits)/len(Profits)
    
# print("Financial Analysis")
# print("---------------------")
# print(f"Total Months: {str(TotalMonths)}")
# print(f"Total: ${str(NetTotal)}")
# print(f"Average Change: ${str(round(ChangeAve,2))}")
# print(f"Greatest Increase in Profits: {IncreaseDates} (${str(GreatestIncrease)})")
# print(f"Greatest Decrease in Profits: {DecreaseDates} (${str(GreatestDecrease)})")

text = (f"""
Financial Analysis
---------------------
Total Months: {str(TotalMonths)}
Total: ${str(NetTotal)}
Average Change: ${str(round(ChangeAve,2))}
Greatest Increase in Profits: {IncreaseDates} (${str(GreatestIncrease)})
Greatest Decrease in Profits: {DecreaseDates} (${str(GreatestDecrease)})
""")

print(text)
with open(Results_File, "w") as text_file:
    print(text, file=text_file)