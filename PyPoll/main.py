import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline="") as csvfile:
    polldata = csv.reader(csvfile, delimiter=",")
    
    khanvotes = 0
    correyvotes = 0
    livotes = 0
    otooleyvotes = 0

    for row in polldata:
        if row[2] == "Khan":
            khanvotes = khanvotes + 1
        elif row[2] =="Correy":
            correyvotes = correyvotes + 1
        elif row[2] == "Li":
            livotes = livotes + 1
        elif row[2] == "O'Tooley":
            otooleyvotes = otooleyvotes + 1

# The total number of votes cast

    total = khanvotes + correyvotes + livotes + otooleyvotes

# #A complete list of candidates who received votes
# #The percentage of votes each candidate won
# #The total number of votes each candidate won
    khan=f"Khan: {(round((khanvotes/total)*100,3))}% ({khanvotes})"
    correy=f"Correy: {(round((correyvotes/total)*100,3))}% ({correyvotes})"
    li=f"Li: {(round((livotes/total)*100,3))}% ({livotes})"
    otooley=f"O'Tooley: {(round((otooleyvotes/total)*100,3))}% ({otooleyvotes})"
    

# #The winner of the election based on popular vote.
    if khanvotes > correyvotes and khanvotes > livotes and khanvotes > otooleyvotes:
        winner = "Khan"
    elif correyvotes > khanvotes and correyvotes > livotes and correyvotes > otooleyvotes:
        winner = "Correy"
    elif livotes > khanvotes and livotes > correyvotes and livotes > otooleyvotes:
        winner = "Li"
    elif otooleyvotes > khanvotes and otooleyvotes > correyvotes and otooleyvotes > livotes:
        winner = "O'Tooley"

    print("Election Results")
    print("-----------------")
    print("Total Votes: ", (total))
    print("-----------------")
    print(khan)
    print(correy)
    print(li)
    print(otooley)
    print("-----------------")
    print("Winner: ", (winner))
    print("-----------------")
