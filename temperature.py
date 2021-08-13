"""
Problem:
    Write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).
"""
import pandas as pd
import re

# The getColWidths function takes in the data file and the line number of the header row that data file. Though this entire problem could have been completed by hardcoding the column widths from the .dat file, the  getColWidths function allows my code the flexibility to work with other "dirty" .dat files with varying columns widths.
def getColWidths(file, header_row):
    line_number = 0
    cur_length = 0
    col_widths = []
    header_row -=1

    with open(file) as dat_file:
        for line in dat_file:
            if line_number == header_row:
                for idx, char in enumerate(line):
                    if line[idx] == ' ' and line[idx -1].isalpha():
                        col_widths.append(cur_length)
                        cur_length = 0
                    cur_length += 1
            elif line_number > header_row:
                break
            line_number += 1
    
    return col_widths

# the setDataFrame takes in the data file, the previously calculated column widths, the row of the headers in the .dat file, and the number of footer rows to ignore. We create a full dataframe of the .dat file using these paramaters. Again, this whole problem could have been solved without creating a functional datafram for the entire .dat file, but this function allows us the flexibility to work with other columns/data series in the future.
def setDataFrame(file, col_widths, header_row, footer_rows):
 return pd.read_fwf((file), skiprows=(header_row - 1), skipfooter=footer_rows, widths=col_widths, usecols=[*range(0, len(col_widths))], index_col='Dy')

# The getMinSpreadDay takes our dataframe in and returns the day with  the smallest temperature spread.
def getMinSpreadDay(df):
    for index, row in df.iterrows():
        row["MnT"] = float(re.sub('\D', '', row["MnT"]))
        row["MxT"] = (float((row['MxT'])))
        if int(index) == 1:
            min_spread = abs(row["MnT"] - row["MxT"])
            day = 1
        else:
            cur_spread = abs(row["MnT"] - row["MxT"])
            if cur_spread < min_spread:
                day = index
                min_spread = cur_spread
    return day



# User needs to declare the following three variables
file = './w_data.dat'
header_row = 5
footer_rows = 2

# Main Program
col_widths = getColWidths(file, header_row)
df = setDataFrame(file, col_widths, header_row, footer_rows)
print(getMinSpreadDay(df))
    
    

