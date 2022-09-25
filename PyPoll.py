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

#Save the results to our election_analysis text file 
with open(file_to_save, "w") as txt_file:
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Determine percentage of votes for each candidate looping through the counts 
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        #calculate vote percentage 
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        
        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
    #Print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


    #Close the file.
    election_data.close()

    
