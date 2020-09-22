# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#file path

csvpath = os.path.join('Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csvwriter = csv.writer(csvfile, delimiter=',')
    

    print(csvreader)

    print("Financial Analysis")
    print("----------------------------")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    row_count = sum(1 for row in csvreader)

    for row in csvreader:
        print(row)

    # The total number of months included in the dataset



    # The net total amount of "Profit/Losses" over the entire period


    # The average of the changes in "Profit/Losses" over the entire period


    # The greatest increase in profits (date and amount) over the entire period


    # The greatest decrease in losses (date and amount) over the entire period