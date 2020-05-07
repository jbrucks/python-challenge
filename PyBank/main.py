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

    for row in csvreader:
        Date.append(row[0])
        P_L.append(int(row[1]))

    # Total months
    totalValue = 0
    for row in P_L:
        totalValue = totalValue + row

    # Total months
    totalMonths = 0
    for row in Date:
        totalMonths += 1

    # Greatest Decrease
    gDec = 0
    for row in P_L:
        if row < gDec:
            gDec = row

    # Greatest Increase
    gInc = 0
    for row in P_L:
        if row > gInc:
             gInc = row

    data = zip(Date, P_L)
    
    # Greatest Info
    gIncAll = 0
    gDecAll = 0
    for row in data:

        if gInc == row[1]:
            gIncAll = row 

        elif gDec == row[1]:
            gDecAll = row 

    # calculate average change
    avgChange = (gDec - gInc) / totalMonths
        
# Print out the budget's name and their percentage stats
print(f"Financial Analysis")
print(f"------------------------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${int(totalValue)}")
print(f"Average Change: ${round(avgChange, 2)}")
print(f"Greatest Increase in Profits: {gIncAll[0]} (${gIncAll[1]})")
print(f"Greatest Decrease in Profits: {gDecAll[0]} (${gDecAll[1]})")

#Output Results to txt File
outputAnalysis = os.path.join("Analysis", "BudgetAnalysis.txt")

with open(outputAnalysis, 'w') as txtfile:

    print(f"Financial Analysis", file=txtfile)
    print(f"------------------------------------------------", file=txtfile)
    print(f"Total Months: {totalMonths}", file=txtfile)
    print(f"Total: ${int(totalValue)}", file=txtfile)
    print(f"Average Change: ${round(avgChange, 2)}", file=txtfile)
    print(f"Greatest Increase in Profits: {gIncAll[0]} (${gIncAll[1]})", file=txtfile)
    print(f"Greatest Decrease in Profits: {gDecAll[0]} (${gDecAll[1]})", file=txtfile) 

#Alternate Version
# with open(budgetData, newline='',) as csvfile:

#     csvreader = csv.reader(csvfile, delimiter=',')

#     header = next(csvreader)
    
#     Date = []
#     profitLosses = []

#     for row in csvreader:
#         Date.append(row[0])
#         profitLosses.append(int(row[1]))

#     total = sum(profitLosses)

#     average = total / len(profitLosses)

#     greatInc = max(profitLosses)

#     greatDec = min(profitLosses)

#     averageChange = (greatDec - greatInc) / len(Date)

#     data = zip(Date, profitLosses)
    
#     for row in data:

#         if greatInc == row[1]:
#             greatIncFinal = row 

#         elif greatDec == row[1]:
#             greatDecFinal = row 

#     print('Financial Analysis')
#     print('--------------------------------------------')
#     print(f'Total Months: {len(Date)}') 
#     print(f'Total: ${int(total)}') 
#     print(f'Average Change: ${round(averageChange, 2)}') 
#     print(f'Greatest Increase in Profits: {greatIncFinal[0]} (${greatIncFinal[1]})') 
#     print(f'Greatest Decrease in Profits: {greatDecFinal[0]} (${greatDecFinal[1]})') 


#Output Results to txt File
# outputAnalysis = os.path.join("Analysis.txt")
      
# with open(outputAnalysis, 'w') as txtfile:

#     print('Financial Analysis', file=txtfile)
#     print('--------------------------------------------', file=txtfile)
#     print(f'Total Months: {len(Date)}', file=txtfile) 
#     print(f'Total: {int(total)}', file=txtfile) 
#     print(f'Average Change: ${round(averageChange, 2)}', file=txtfile) 
#     print(f'Greatest Increase in Profits: {greatIncFinal[0]} (${greatIncFinal[1]})', file=txtfile) 
#     print(f'Greatest Decrease in Profits: {greatDecFinal[0]} (${greatDecFinal[1]})', file=txtfile) 
