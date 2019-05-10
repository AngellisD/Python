#import the os module and csv module
import os
import csv

# Reading and delimiting CSV data
election_csv = os.path.join("election_data.csv")
with open(election_csv) as newfile:
  csvreader = csv.reader(newfile, delimiter=',')
  reader_file=next(csvreader)

# Set list to storage info
  candidate = []

# Read each row of data  
  for row in csvreader:
    candidate.append(row[2])

# print frame
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(len(candidate)))
print("----------------------------")

# calculate total info candidates, percentage and votes
Khan = candidate.count("Khan")
kpercent = int((Khan) / len(candidate) * 100)

Correy = candidate.count("Correy")
cpercent = int((Correy) / len(candidate) * 100)

Li = candidate.count("Li")
Lpercent = int((Li) / len(candidate) * 100)

OTooley = candidate.count("O'Tooley")
Opercent = int((OTooley) / len(candidate) * 100)

# Print percentages for each candidate
print("Khan: " + str(kpercent) + "% (" + str(Khan) + ")")
print("Correy: " + str(cpercent) + "% (" + str(Correy) + ")")
print("Li: " + str(Lpercent) + "% (" + str(Li) + ")")
print("O'Tooley " + str(Opercent) + "% (" + str(OTooley) + ")")


# Print dataframe
print("----------------------------")

if kpercent > .50:
	print("Winner: Khan")
elif cpercent > .50:
	print("Winner: Correy")
elif Lpercent > .50:
	print("Winner: Li")
else:
	print("Winner: O'Tooley")			

# Exporting to text file
f = open("pypoll.txt","w")   
f.write("Khan: " + str(kpercent) + "% (" + str(Khan) + ")")
f.write("Correy: " + str(cpercent) + "% (" + str(Correy) + ")")
f.write("Li: " + str(Lpercent) + "% (" + str(Li) + ")")
f.write("O'Tooley " + str(Opercent) + "% (" + str(OTooley) + ")")
f.close()			