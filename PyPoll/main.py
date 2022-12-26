<<<<<<< HEAD
#import modules
import os
import csv

#set path for file
csvpath = os.path.join("C:\\Users\\cryst\\OneDrive\\Documents\\Bootcamp Class\\Week3 Python\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#set variables
total_vote = 0
candidates_list = []
unique_candidate = []
percentage_vote = 0.00
total_vote_won = 0
winner = []
Raymon_Anthony_Doane_votes = 0
Diana_DeGette_votes = 0
Charles_Casper_Stockham_votes = 0

#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#enter loop
    for row in csvreader:

# calculate Total Votes and votes for 
        total_vote +=1    

        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_votes +=1 
           

        candidates_list.append(row[2])
    for x in set(candidates_list):
        unique_candidate.append(x)


        Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/total_vote) *100
        Diana_DeGette_percent = (Diana_DeGette_votes/total_vote) *100
        Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/total_vote) *100

    votes = [Charles_Casper_Stockham_votes,Diana_DeGette_votes, Raymon_Anthony_Doane_votes]
    total_vote_won = max(votes)
winner = unique_candidate[votes.index(total_vote_won)]

output_file = "output.txt"

with open(output_file, 'w') as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_vote}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
=======
#import modules
import os
import csv

#set path for file
csvpath = os.path.join("C:\\Users\\cryst\\OneDrive\\Documents\\Bootcamp Class\\Week3 Python\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#set variables
total_vote = 0
candidates_list = []
unique_candidate = []
percentage_vote = 0.00
total_vote_won = 0
winner = []
Raymon_Anthony_Doane_votes = 0
Diana_DeGette_votes = 0
Charles_Casper_Stockham_votes = 0

#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#enter loop
    for row in csvreader:

# calculate Total Votes and votes for 
        total_vote +=1    

        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_votes +=1 
           

        candidates_list.append(row[2])
    for x in set(candidates_list):
        unique_candidate.append(x)


        Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/total_vote) *100
        Diana_DeGette_percent = (Diana_DeGette_votes/total_vote) *100
        Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/total_vote) *100

    votes = [Charles_Casper_Stockham_votes,Diana_DeGette_votes, Raymon_Anthony_Doane_votes]
    total_vote_won = max(votes)
winner = unique_candidate[votes.index(total_vote_won)]

output_file = "output.txt"

with open(output_file, 'w') as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_vote}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
>>>>>>> 32226df4a10e5e530692ad15033504528918c227
    file.write(f"----------------------------")