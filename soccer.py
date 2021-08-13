"""
Problem:
    Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

Note:
    In contrast to the Temperature probelem, this solution is intentinally less dynamic to showcase a simpler more direct approach to solving these problems.
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


df = pd.read_csv('./soccer.csv')                # create the dataframe using the new soccer.csv file
df['difForAgainst'] = (df['F'] - df['A']).abs() # Calculate the difference in ‘for’ and ‘against’ goals for each team
minForAgainstIdx = df['difForAgainst'].idxmin() # Get index of the team with the min goal difference

print(df.loc[minForAgainstIdx, 'Team'])         