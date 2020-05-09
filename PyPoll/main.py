import os
import csv


electionData = os.path.join('Resources', "election_data.csv")

# Read in the CSV file
with open(electionData, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip Header
    header = next(csvreader)

    VoterID = []
    County = []
    Candidate = []

    for row in csvreader:
        VoterID.append(int(row[0]))
        County.append(row[1])
        Candidate.append(row[2])

    # Total Votes
    totalVotes = 0
    for row in VoterID:
        totalVotes += 1

    # Check for unique values
    # CandidateSet = set(Candidate)
    # print(CandidateSet)

    # Votes for Khan
    KhanVotes = 0
    for row in Candidate:
        if row == "Khan":
            KhanVotes += 1

    # Khan Vote Percentage
    KhanPer = KhanVotes / totalVotes * 100

    # Khan Info
    Khan = ("Khan", KhanPer, KhanVotes)

    # Votes for Correy
    CorreyVotes = 0 
    for row in Candidate:
        if row == "Correy":
            CorreyVotes += 1
    
    # Correy Vote Percentage
    CorreyPer = CorreyVotes / totalVotes * 100

    # Correy Info
    Correy = ("Correy", CorreyPer, CorreyVotes)

    # Votes for Li
    LiVotes = 0
    for row in Candidate:
        if row == "Li":
            LiVotes += 1

    # Li Vote Percentage
    LiPer = LiVotes / totalVotes * 100

    # Li Info
    Li = ("Li", LiPer, LiVotes)

    # Votes for O'Toole
    OtooleyVotes = 0
    for row in Candidate:
        if row == "O'Tooley":
            OtooleyVotes += 1

    # O'Tooley Vote Percentage
    OtooleyPer = OtooleyVotes / totalVotes * 100

    # O'Tooley Info
    OTooley = ("O'Tooley", OtooleyPer, OtooleyVotes)
    
    # Run conditionals to see Winner
    if Khan[2] > Correy[2] and Li[2] and OTooley[2]:
        First = Khan
    
    elif Correy[2] > Khan[2] and Li[2] and OTooley[2]:
        First = Correy

    elif Li[2] > Khan[2] and Correy[2] and OTooley[2]:
        First = Li

    elif OTooley[2] > Khan[2] and Li[2] and Correy[2]:
        First = OTooley

    # Check Winner
    # print(First)

    # Check Results
    # print(OTooley)
    # print(Correy)
    # print(Li)
    # print(Khan)

# Print out the election results and analysis
print(f"Election Results")
print(f"------------------------------------------------")
print(f"Total Votes: {totalVotes}")
print(f"------------------------------------------------")
print(f"{First[0]}: {First[1]:.3f}% ({First[2]})")
print(f"{Correy[0]}: {Correy[1]:.3f}% ({Correy[2]})")
print(f"{Li[0]}: {Li[1]:.3f}% ({Li[2]})")
print(f"{OTooley[0]}: {OTooley[1]:.3f}% ({OTooley[2]})")
print(f"------------------------------------------------")
print(f"Winner: {First[0]}")
print(f"------------------------------------------------")

#Output Results to txt File
outputAnalysis = os.path.join("Analysis", "ElectionsAnalysis.txt")

with open(outputAnalysis, 'w') as txtfile:

    print(f'Election Results', file=txtfile)
    print(f'------------------------------------------------', file=txtfile)
    print(f'Total Votes: {totalVotes}', file=txtfile)
    print(f'------------------------------------------------', file=txtfile)
    print(f'{First[0]}: {First[1]:.3f}% ({First[2]})', file=txtfile)
    print(f'{Correy[0]}: {Correy[1]:.3f}% ({Correy[2]})', file=txtfile)
    print(f'{Li[0]}: {Li[1]:.3f}% ({Li[2]})', file=txtfile)
    print(f'{OTooley[0]}: {OTooley[1]:.3f}% ({OTooley[2]})', file=txtfile) 
    print(f'------------------------------------------------', file=txtfile)
    print(f'Winner: {First[0]}', file=txtfile)
    print(f'------------------------------------------------', file=txtfile)
