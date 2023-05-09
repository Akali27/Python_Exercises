import csv

# File path
electiondata = "election_data.csv"

# Open CSV file
with open(electiondata) as csvelectiondata:

    # Initialize variables
    total_votes = 0
    candidates_dictionary = {}

    # Use the CSV module to read the data in the file
    csv_reader = csv.reader(csvelectiondata, delimiter=",")

    # Skip the header row
    next(csv_reader, None)

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Increment the total vote count
        total_votes += 1

        # Get the candidate name from the third column of the row
        candidate_name = row[2]

        # If the candidate name is already in the dictionary increment their vote count
        if candidate_name in candidates_dictionary:
            candidates_dictionary[candidate_name] += 1
        # Otherwise, add the candidate to the dictionary with a vote count of 1
        else:
            candidates_dictionary[candidate_name] = 1

    # Print the election results
    print("Election Results")
    print("--------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("--------------------------------------")
    
    # Initialize variables for storing the winner and their vote count
    winner = ""
    winner_votes = 0
    
    for key, value in candidates_dictionary.items():
        # Calculate the percentage of votes each candidate received and print it with their name and vote count
        percentage_votes = (value / total_votes) * 100
        print(f"{key}: {percentage_votes:.3f}% ({value})")
        
        # Update the winner variables if the current candidate has more votes than the current winner
        if value > winner_votes:
            winner = key
            winner_votes = value
       
    print("----------------------------------------")
    print(f"Winner: {winner}")

# Write the results to a text file
with open("election_results.txt", "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("--------------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("--------------------------------------\n")
    
    for key, value in candidates_dictionary.items():
        # Calculate the percentage of votes each candidate received and write it with their name and vote count to the text file
        percentage_votes = (value / total_votes) * 100
        textfile.write(f"{key}: {percentage_votes:.3f}% ({value})\n")
    
    textfile.write("----------------------------------------\n")
    textfile.write(f"Winner: {winner}\n")
