#Add our dependencies. 
import csv
import os 

#Assign a variable to load a file from path.
file_to_load = os.path.join("03","election_analysis", "Resources", "election_results.csv")
print(os.getcwd())

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("03", "election_analysis","analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0 

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

#3. Print the total votes 
print(total_votes)

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write three counties to the file.
    txt_file.write("Counties in the Election\n ------------------------\nArapahoe\nDenver\nJefferson")

    #print(election_data)

#Close the file.
election_data.close()

#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote
 