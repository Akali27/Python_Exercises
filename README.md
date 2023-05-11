## Election Analysis and Financial Analysis in Python

This repository contains two Python scripts that analyze election and financial data. Both scripts read data from CSV files, process the data, print the results before writing the data to text files.

## Scripts

1) budget_calc.py: The script analyzes a company's financial records and calculates the following:
 - The total number of months included in the dataset.
 - The total amount of revenue gained over the entire period.
 - The average change in revenue between months over the entire period.
 - The greatest increase in revenue over the entire period.
 - The greatest decrease in revenue over the entire period.


2) election_calc.py: The script analyzes poll data and calculates the following: 
- The total number of votes cast.
- A complete list of candidates who received votes.
- The percentage of votes each candidate won.
- The total number of votes each candidate won.
- The winner of the election based on popular vote.

## Datasets

budget_data.csv contains two columns: `Date` and `Revenue`.
election_data.csv contains three columns: `Voter ID`, `County`, and `Candidate`. 
