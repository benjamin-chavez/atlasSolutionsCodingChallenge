"""
Problem:
    The attached soccer.dat file contains the results from the English Premier League. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). 
    
    Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
"""
import pandas as pd
import re
import csv

lineNumber = 0

# Open soccer.dat file and convert the data into csv format
with open(r'./soccer.dat') as dat_file, open('soccer.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    for line in dat_file:
        row = [field.strip() for field in re.split("\s+", line.replace('-', ' '))]
        if len(row) > 2:             
            csv_writer.writerow(row[1:-1])

# create the dataframe using the new soccer.csv file
df = pd.read_csv('./soccer.csv')

# Add a column to the datafram for each teams absolute  difference in ‘for’ and ‘against’ goals
df['difForAgainst'] = (df['F'] - df['A']).abs()

# Find the index of the team with the minimum difference
minForAgainstIdx = df['difForAgainst'].idxmin()

# print the name of team
print(df.loc[minForAgainstIdx, 'Team'])