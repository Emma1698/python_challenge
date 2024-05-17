# Creating the file/cvs file
import os
import csv

# All Variable
voters_receive = {}
votes = []
Charles = 0
Raymon = 0
Diana = 0

# Setting a path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Opening cvs file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

# Looping through the data store and calculating total votes
    for row in csvreader:
        votes.append(row[1])
        totalvotes = len(votes)
        
        if row[2] == "Charles Casper Stockham":
            Charles += 1
        elif row[2] == "Diana DeGette":
            Diana += 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon += 1
        
 # Getting average totals for each candidate
    Candidate_1 = round((Charles / totalvotes)*100,3)
    Candidate_2 = round((Diana / totalvotes)*100,3)
    Candidate_3 = round((Raymon / totalvotes)*100,3)
    
    voters_receive = {"Charles Casper Stockham": Charles,
                      "Diana DeGette": Diana,
                      "Raymon Anthony Doane": Raymon}
    
    electionresult = max(voters_receive, key = voters_receive.get)
    
# Printing the Election Results
print("Election Results") 
print("----------------------------") 
print(f"Total Votes: {totalvotes}") 
print("----------------------------") 
print(f"Charles Casper Stockgam: {Candidate_1}% ({Charles})") 
print(f"Diana DeGette: {Candidate_2}% ({Diana})") 
print(f"Raymon Anthony Doane: {Candidate_3}% ({Raymon})") 
print("----------------------------") 
print(f"Winner: {electionresult}")
print("----------------------------") 

# Setting a path for file to print Election result and export to a text file
dpath = "PyPoll/Analysis"
os.makedirs(dpath, exist_ok=True)
with open("Analysis/election_reults.txt", "w") as file:
    file.write("Election Results\n")
    file.write("----------------------------\n") 
    file.write(f"Total Votes: {totalvotes}\n") 
    file.write("----------------------------\n") 
    file.write(f"Charles Casper Stockgam: {Candidate_1}% ({Charles})\n")
    file.write(f"Diana DeGette: {Candidate_2}% ({Diana})\n")
    file.write(f"Raymon Anthony Doane: {Candidate_3}% ({Raymon})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {electionresult}\n")
    file.write("----------------------------\n")

