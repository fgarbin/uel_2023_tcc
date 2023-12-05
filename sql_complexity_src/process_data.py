import csv
import os
import pandas as pd

cwd = os.getcwd()

def readCSV():
  # opening the CSV file
  with open(cwd + '\data\graylog-search-result-relative-2592000.csv', mode ='r') as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
 
    # displaying the contents of the CSV file
    for lines in csvFile:
      print(lines)

def readCSV_pandas():
  csv_file = pd.read_csv(cwd + '\data\graylog-search-result-relative-2592000.csv', header=0)
  return csv_file

def DF_DropDup(df_ori, fields_tocheck):
  df_no_dup = df_ori.drop_duplicates(subset=fields_tocheck)

  return df_no_dup

csv_df = readCSV_pandas()

print(csv_df.columns)
print(csv_df.loc[[1]])
print(csv_df['query_out'])
print(csv_df.describe)
print(csv_df.count)

#csv_df_no_dup = csv_df.drop_duplicates(subset=['query_out'])
csv_df_no_dup = DF_DropDup(csv_df, ['query_out'])
print(csv_df_no_dup)
csv_df_no_dup.to_csv(cwd + '\data\qry_nodup_query_out.csv')

csv_df_no_dup = DF_DropDup(csv_df, ['source'])
print(csv_df_no_dup)
csv_df_no_dup.to_csv(cwd + '\data\qry_nodup_source.csv')