import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
outpath = os.path.join('Analysis','election_report.txt')

# Create list to store the variables
voterID = []
candidate = []
num_votes =[]
percent_votes = []

#Create dictionary to store name + values
dict = {}

#Set initial value
sum_votes = 0


with open(csvpath,'r') as electiondata:
    csvreader = csv.reader(electiondata, delimiter=",")

    csvheader = next(csvreader) 
    #print(f"Headers: {csvheader}")
    
    #Iterate the CSV values into the list   
    for row in csvreader:

        voterID.append(int(row[0]))
        # candidate.append(row[2])

    #Create Dictionary to filter (and add up) duplicate candidate names
        sum_votes += 1
        if row[2] in dict.keys():
            dict[row[2]] = dict[row[2]] + 1

        else:
            dict[row[2]] = 1
        
#Calculate total number of Votes
total_voters = len(voterID)
# print(total_voters)

#Create lists to input candidates with their votes respectively from Dictionary

for key, value in dict.items():
    candidate.append(str(key))
    num_votes.append(value)

# print(candidate)
# print(num_votes)

#Calculate percentages
for i in num_votes:
    percentage = round((i/total_voters)*100,3)
    percent_votes.append(percentage)

#Need to change into list dictionary after zipping
new_data = list((zip(candidate,percent_votes,num_votes)))

# for c,p,n in new_data:
#     print("{}: {}% ({})".format(c,p,n))
    
#Find Greatest Votes
max_votes = max(num_votes)

# print(max_votes)

#Find correspondent candidates for greatest votes
for win_index in range(len(num_votes)):
    win_count = num_votes.index(max_votes)
    win_name = candidate[win_count]

# print(win_count)
# print(win_name)
    

# # # Export to output file
with open(outpath, 'w') as textfile:
    textfile.writelines( f"Election Results\n"

    f"------------------------------\n"

    f"Total votes : {total_voters}\n"

    f"------------------------------\n")
        
    for c,p,n in new_data:
        textfile.writelines("{}: {}% ({})    ".format(c,p,n))

    
    textfile.writelines(
    f"            \n"
        
    f"------------------------------\n"

    f"Winner: {win_name}\n"

    f"------------------------------\n")
    
      

        