import os
import csv


budgetData = os.path.join('Resources', "budget_data.csv")

# Read in the CSV file
with open(budgetData, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip Header
    header = next(csvreader)

    Date = []
    P_L = []
    MonthlyChange = []

    for row in csvreader:
        Date.append(row[0])
        P_L.append(int(row[1]))

    # Total months
    totalValue = 0
    for row in P_L:
        totalValue += row

    # Total months
    totalMonths = 0
    for row in Date:
        totalMonths += 1

    # Total Month Changes
    for row in range(len(P_L)-1):
        MonthlyChange.append(P_L[row+1] - P_L[row])
    
    # Greatest Increase and Month
    #   prev_value = 0
    #   gInc = 0
    #   for row in P_L:
    #       change = row - prev_value
    #       if change > gInc:
    #           gInc = change
    #       prev_value = row
    gInc = max(MonthlyChange)
    gIncMonth = MonthlyChange.index(max(MonthlyChange)) + 1

    # Greatest Decrease
    #   prev_value = 0
    #   gInc = 0
    #   for row in P_L:
    #       change = row - prev_value
    #       if change > gInc:
    #           gInc = change
    #       prev_value = row
    gDec = min(MonthlyChange)
    gDecMonth = MonthlyChange.index(min(MonthlyChange)) + 1

    avgChange = sum(MonthlyChange) / (totalMonths - 1)
        
# Print out the budget's name and their percentage stats
print(f"Financial Analysis")
print(f"------------------------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${int(totalValue)}")
print(f"Average Change: ${round(avgChange, 2)}")
print(f"Greatest Increase in Profits: {Date[gIncMonth]} (${gInc})")
print(f"Greatest Decrease in Profits: {Date[gDecMonth]} (${gDec})")

# Output Results to txt File
outputAnalysis = os.path.join("Analysis", "BudgetAnalysis.txt")

with open(outputAnalysis, 'w') as txtfile:

    print(f"Financial Analysis", file=txtfile)
    print(f"------------------------------------------------", file=txtfile)
    print(f"Total Months: {totalMonths}", file=txtfile)
    print(f"Total: ${int(totalValue)}", file=txtfile)
    print(f"Average Change: ${round(avgChange, 2)}", file=txtfile)
    print(f"Greatest Increase in Profits: {Date[gIncMonth]} (${gInc})", file=txtfile)
    print(f"Greatest Decrease in Profits: {Date[gDecMonth]} (${gDec})", file=txtfile) 