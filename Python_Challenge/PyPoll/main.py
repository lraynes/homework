#import as a list of dictionaries
#{["Voter ID": ____, "County": _____, "Candidate": _____]}
import os
import csv

def percentage_calc(part,whole):
    return(str(part/whole * 100) + "%")


vote_count = 0
candidate_list = []
can_0_count = 0
can_1_count = 0
can_2_count = 0
can_3_count = 0

#INSTEAD, MAKE THE CANDIDATE LIST INTO A DICTIONARY -> {"Candidate Name": number of votes}

election_data_1_path = os.path.join(".", "election_data_1.csv")
with open(election_data_1_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        vote_count += 1

        if row["Candidate"] not in candidate_list:
            candidate_list.append(row["Candidate"])

        if row["Candidate"] == candidate_list[0]:
            can_0_count += 1

        elif row["Candidate"] == candidate_list[1]:
            can_1_count += 1

        elif row["Candidate"] == candidate_list[2]:
            can_2_count += 1

        elif row["Candidate"] == candidate_list[3]:
            can_3_count += 1

#The total number of votes cast
#A complete list of candidates who received votes
print(candidate_list)
print("Vote count: " + str(vote_count))
print(candidate_list[0] + ": " + percentage_calc(can_0_count,vote_count) + " (" + str(can_0_count) + ")")
print(candidate_list[1] + ": " + percentage_calc(can_1_count,vote_count) + " (" + str(can_1_count) + ")")
print(candidate_list[2] + ": " + percentage_calc(can_2_count,vote_count) + " (" + str(can_2_count) + ")")
print(candidate_list[3] + ": " + percentage_calc(can_3_count,vote_count) + " (" + str(can_3_count) + ")")
print("Winner: ")


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.

