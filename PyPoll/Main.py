import os
import csv
output=os.path.join("Analysis", "PyPoll_results.txt")
with open('Resources/election_data.csv', 'r') as my_data:
    csv_reader=csv.reader(my_data)
    header=next(csv_reader)
    row_count=0
    percentage=0
    candidates={}
    for row in csv_reader:
        row_count+=1 # 1. The total number of votes cast      
        candidate_name=row[2] # candidate name is in 3rd column
        if candidate_name not in candidates.keys(): # encounter new name 
            candidates[candidate_name]=1 # 2. A complete list of candidates who received votes
        else:
            candidates[candidate_name]+=1 # 4. The total number of votes each candidate won

maxvalue = 0
winner = ""

# 6a. Print the analysis to the terminal
print("Election Results")
print("------------------")
print("Total Votes: "+str(row_count))
print("------------------")
for key in candidates:
    # candidates[key] = number of votes for that candidate
    percentage=(candidates[key]/row_count)*100 # 3. The percentage of votes each candidate won  
    print(key, ':', "{:.3f}".format(percentage),'%', candidates[key])
    if candidates[key] > maxvalue:
        maxvalue = candidates[key]
        winner=key # 5. The winner of the election based on popular vote (use if statement like pybank, not max)
print("------------------")
print('Winner:', winner)
print("------------------")
# 6b. Export a text file with the results
with open(output, 'w', newline='') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------\n")
    txtfile.write(f"Total Votes: {row_count}\n")
    txtfile.write(f"------------------\n")
    for key in candidates:
        percentage=(candidates[key]/row_count)*100
        txtfile.write(f"{key}: {'{:.3f}'.format(percentage)},% {candidates[key]}\n")
    txtfile.write(f"------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"------------------\n")