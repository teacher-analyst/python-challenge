import os
import csv
from collections import Counter 

#Lists to store data
candidates_votes=[]


with open('election_data.csv', encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter= ',') 
    csv_header = next(csvfile)

    #read each row of data after header in csv file & append to list 
    for row in csvreader:
        candidates_votes.append(row[2])

    #count # of votes
    no_votes = len(candidates_votes)

    #count the votes for each candidate and store in dictionary 
    vote_count=Counter(candidates_votes) 
    vote_count_dict=dict(vote_count)
    winner=max(vote_count_dict, key=vote_count_dict.get)
    
    #Print to terminal
    print("Election Results")
    print("---------------------")
    print("Total Votes: " + str(no_votes))

    
    #Loop throug the dictionary, determine percentage of values and return candidate names and percentage votes 
    for candidates,count in vote_count.items():
        percentage=(count/no_votes)*100
        rounded_number=round(percentage, 3)
        print(candidates, ":", rounded_number , "% ", "(", count, ")")
    
    #Print winner to terminal
    print("---------------------\n Winner: " + winner + "\n---------------------")

#Write results to text file   
with open('analysis.txt', 'w') as outfile:

    outfile.write(
        "Election Results\n"
        "---------------------\n"
        "Total Votes: " + str(no_votes) + "\n"
        )

with open('analysis.txt', 'a') as outfile:
    for candidates,count in vote_count.items():
        percentage=(count/no_votes)*100
        rounded_number=round(percentage, 3)
        outfile.write(candidates + ": "+ str(rounded_number) + "% "+ "(" + str(count) +")\n")
    
    outfile.write("---------------------\nWinner: " + winner + "\n---------------------")




        

    
    

    
    
    

    
