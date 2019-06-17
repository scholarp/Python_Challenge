#Import Modules

import os
import csv


#Set variables

total_votes = 0
candidate_name = ""
candidates_list = []
votes_list = []
percent_list = []
winner = ""

#Choose path for file

file_path = os.path.join("election_data.csv")

with open(file_path,'r') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=",")
    
#Read the header row first
    
    next(csv_reader, None)
    
#Read each row of data after the header
    
    for row in csv_reader:
        
#Count the total number of months
        
        total_votes += 1
        
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            votes_list.append(1)
        else:
            votes_list[candidates_list.index(row[2])] += 1

#Compute percent of votes            

percent_list = [(100/total_votes) * x for x in votes_list]

#Determine the winner

winner = candidates_list[votes_list.index(max(votes_list))]

#Per instructions, print analysis to terminal         

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for x in candidates_list:
#'.3f' formats decimal to 3 places    
    
    print(x + ": " + str(format(percent_list[candidates_list.index(x)], '.3f')) 
        + "% (" + str(votes_list[candidates_list.index(x)]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#Per instructions, export to .txt file

f = open("election_data_results.txt", "w")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")

for x in candidates_list:
#'.3f' formats decimal to 3 places 
    
    f.write(x + ": " + str(format(percent_list[candidates_list.index(x)], '.3f')) 
        + "% (" + str(votes_list[candidates_list.index(x)]) + ")\n")
f.write("-------------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-------------------------\n")
f.close()