import csv
with open('Resources/election_data.csv', 'r') as my_data:
    csv_reader=csv.reader(my_data)

    header=next(csv_reader)
    row_count=0
    candidates={}
    for row in csv_reader:
        # 1 The total number of votes cast
        row_count+=1
    

        # 2 A complete list of candidates who received votes        
        candidate_name=row[2] # candidate name is in 3rd column
        if candidate_name not in candidates.keys(): # encounter new name
            print (candidate_name)
            candidates[candidate_name]=1

        # 4 The total number of votes each candidate won
        else:
            candidates[candidate_name]+=1

# 3 The percentage of votes each candidate won
        (candidates)/(candidate_name)
    
# 5 The winner of the election based on popular vote.    

    # final answers
    print (row_count)
    print (candidates)