#Add our dependencies. 
import csv
import os 

#Assign a variable to load a file from path.
file_to_load = os.path.join("election_analysis", "Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("election_analysis","analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0 

# Establish Candidates and candidate votes
candidate_options = []

#Declare dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print header row
    headers = next(file_reader)

    #Print each row in the CSV file. 
    for row in file_reader:

        #2. Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name =row[2]

        #If candidate name does not match any existing candidate
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list 
            candidate_options.append(candidate_name)
            
            #Track the candidate's vote count 
            candidate_votes[candidate_name] = 0

        #Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

#Determine percentage of votes for each candidate looping through the counts 
#1. Interate through the candidate list.
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes.
    vote_percentage = float(votes)/ float(total_votes) * 100
    #4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if the vote count is greater than the winning count.
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent = vote_percentages.
       winning_count = votes
       winning_percentage = vote_percentage
       #And set the winning_candidate equal to the candidate's name 
       winning_candidate = candidate_name
       
#Print the winning candidate, vote count and percentage. 
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
        

#Print the candidate list. 
#print (candidate_options)

#3. Print the total votes. 
#print(total_votes)

#print(candidate_votes)


#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write three counties to the file.
    txt_file.write("Counties in the Election\n ------------------------\nArapahoe\nDenver\nJefferson")




    #Print each row in the CSV file. 
    #for row in file_reader:
     #   print(row)

    #print(election_data)

#Close the file.
election_data.close()

#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote
 