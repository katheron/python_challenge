import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    months = []
    nettotal = 0
    increase = 0
    decrease = 0

    for row in csvreader:
        months.append(row[0])
        
        nettotal = nettotal + int(row[1])

        if (increase < float(row[1])):
            increase = float(row[1])
            increasemonth = row[0]

        if (decrease > float(row[1])):
            decrease = float(row[1])
            decreasemonth = row[0]
    
    print("Financial Analysis")
    print("------------------")
    print(f"Total Month: {len(months)}")
    print(f"Total Revenue : ${nettotal}")
    print(f"Average Change : ${round(nettotal/len(months),2)}")
    print(f"Greatest Increase in Profits : {increasemonth} (${increase})")
    print(f"Greatest Decrease in Profits : {decreasemonth} (${decrease})")