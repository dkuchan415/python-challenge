# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    vote_count = 0

    for row in csvreader:
        vote_count = vote_count + 1
        
#Print header

    print("Election Results")
    print("-------------------------")        
# The total number of votes cast
    print(f"Total Votes: {vote_count}")
    print("-------------------------")

# A complete list of candidates who received votes


# The percentage of votes each candidate won
# The total number of votes each candidate won
    # print("Khan: ")
    # print("Correy: ")
    # print("Li: ")
    # print("O'Tooley: ")
    # print("-------------------------")


# The winner of the election based on popular vote.




