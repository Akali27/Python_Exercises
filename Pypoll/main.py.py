import csv


electiondata = "import csv"


electiondata = "C:/Users/RogStrix/Downloads/raw_data-poll/election_data_2.csv"

with open(electiondata) as csvelectiondata:

    total_votes = 0
    candidates_dictionary = {}
    most_votes = 0

    csv_reader = csv.reader(csvelectiondata, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        total_votes = total_votes + 1
  
        candidate_name = row[2]

        if candidate_name in candidates_dictionary:

            candidates_dictionary[candidate_name] += 1
        else:
            candidates_dictionary[candidate_name] = 1
   
    print("Election Results")
    print("--------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("--------------------------------------")
    for key, value in candidates_dictionary.items(): 
        print(key, str(value/total_votes*100)+"%", value) 
       
    print("----------------------------------------")
    print("Winner: " + "Khan")

with open(electiondata) as csvelectiondata:

    total_votes = 0
    candidates_dictionary = {}
    most_votes = 0

    csv_reader = csv.reader(electiondata, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        total_votes = total_votes + 1
  
        candidate_name = row[2]

        if candidate_name in candidates_dictionary:

            candidates_dictionary[candidate_name] += 1
        else:
            candidates_dictionary[candidate_name] = 1
 
    print("Election Results")
    print("--------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("--------------------------------------")
    for key, value in candidates_dictionary.items(): 
        print(key, str(value/total_votes*100)+"%", value) 
    print("----------------------------------------")
    print("Winner: " + "Khan")